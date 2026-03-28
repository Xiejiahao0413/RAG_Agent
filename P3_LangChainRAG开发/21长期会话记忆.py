import os,json
from openai import OpenAI
from typing import Sequence
from langchain_core.messages import BaseMessage,message_to_dict,messages_from_dict
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_community.chat_models import ChatTongyi
from langchain_core.prompts import PromptTemplate,ChatPromptTemplate,MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import InMemoryChatMessageHistory

client = OpenAI(
    api_key="sk-b3514ee3fae4476a8f19e3643795c5f9",
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

class FileChatMessageHistory(BaseChatMessageHistory):
    def __init__(self,session_id,storage_path):
        self.session_id = session_id                #会话id
        self.storage_path = storage_path       #不同会话id的存储文件，所在在的文件路径
        #完整的文件路径
        self.file_path = os.path.join(self.storage_path,self.session_id)

        #确保文件路径是正确的
        os.makedirs(os.path.dirname(self.file_path),exist_ok=True)

    def add_messages(self, messages: Sequence[BaseMessage]) -> None:
        #Sequence序列类似list，tuple
        all_messages = list(self.messages)       #已有的消息列表
        all_messages.extend(messages)            #新的和已有的融合成一个list

        # new_messages = []
        # for message in all_messages:
        #     d = message_to_dict(message)
        #     new_messages.append(d)
        new_messages = [message_to_dict(message) for message in all_messages]
        #将数据写入文件
        with open(self.file_path,'w',encoding='utf-8') as f :
            json.dump(new_messages,f)

    @property       #@property装饰器将messages方法变成成员方法属性用
    def messages(self) -> list[BaseMessage]:
        #当前文件内：；list[字典]
        try:
            with open (self.file_path,'r',encoding='utf-8') as f:
                messages_data = json.load(f)   #返回值就是list[字典]
                return messages_from_dict(messages_data) 
        except FileNotFoundError:
            return []
        
    def clear(self) -> None:
        with open(self.file_path,'w',encoding='utf-8') as f:
            json.dump([],f)

model = ChatTongyi(model='qwen3-max')

prompt = ChatPromptTemplate.from_messages(
    [
        ('system','你需要根据会话历史回应用户问题，对话历史。'),
        MessagesPlaceholder('chat_history'),
        ('human','请回答如下问题，{input}')
    ]
)

str_parser = StrOutputParser()

def print_prompt(full_prompt):
    print('='*20,full_prompt.to_string(),'='*20)
    return full_prompt

base_chain = prompt | print_prompt | model | str_parser

chat_history_store = {}              #存放多个回话的id所对应的历史会话记录

def get_history(session_id):
    return FileChatMessageHistory(session_id,"./P3_LangChainRAG开发/chat_history")

#通过RunnableWithMessagestory获取一个新的带有历史记录功能的chain
conversation_chain = RunnableWithMessageHistory(
    base_chain,                                #被附加的历史消息的Runnable,通常是chain
    get_history,                               #获取历史对话的函数
    input_messages_key='input',                #声明用户输入消息在模版中占位符
    history_messages_key='chat_history'        #声明历史消息在模版中的占位符
)

if __name__ =='__main__': 
    #如下固定格式，配置当前的会话id         
    session_config = {'configurable':{'session_id':'user_001'}}
    print(conversation_chain.invoke({'input':'小明有一直猫'},session_config))
    print(conversation_chain.invoke({'input':'小花有两只狗'},session_config))
    print(conversation_chain.invoke({'input':'共有几只宠物'},session_config))

