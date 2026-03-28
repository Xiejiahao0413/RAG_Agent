from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.output_parsers import JsonOutputParser

str_parser = StrOutputParser()
json_parser = JsonOutputParser()

model = ChatTongyi(model = 'qwen3-max')

frist_prompt = PromptTemplate.from_template(
    '我的邻居姓：{lastname},刚生了{gender},请起名，'
    '并封装到JSON格式返回给我,要求是key是name,value就是刚起的名字,请严格遵守格式要求。'
)


second_prompt = PromptTemplate.from_template(
    '姓名{name},请帮我解析含义'
)

chain = frist_prompt | model | json_parser | second_prompt | model | str_parser

for chunk in chain.stream({'lastname':'张',"gender":'女儿'}):
    print(chunk,end='',flush = True)
