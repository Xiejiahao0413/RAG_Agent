from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms.tongyi import Tongyi

#创建基础连
prompt = ChatPromptTemplate(
    [
        ("system","你是一个有用的助手"),
        ("placeholder","{chat_history}"),    #历史信息占位符
        ("human","{input}")
    ]
)

llm = Tongyi()

chain = prompt | llm | StrOutputParser()

# 2. 创建历史存储工厂函数
def get_session_history(session_id: str):
    """根据session_id返回对应的历史对象"""
    # 这里可以连接数据库、Redis等
    return InMemoryChatMessageHistory()

# 3. 包装链
chain_with_history = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="input",      # 输入中的用户消息key
    history_messages_key="chat_history",  # 历史消息占位符key
)

# 4. 使用
result = chain_with_history.invoke(
    {"input": "你好，我叫小明"},
    config={"configurable": {"session_id": "user123"}}
)
print(result)

# 第二次对话，自动携带历史
result = chain_with_history.invoke(
    {"input": "我叫什么名字？"},
    config={"configurable": {"session_id": "user123"}}
)
print(result)  # 会记得叫小明