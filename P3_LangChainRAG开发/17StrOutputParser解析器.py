from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

parser = StrOutputParser()
model = ChatTongyi(model = 'qwen3-max')
prompt =PromptTemplate.from_template(
    '我的邻居姓：{lastname},刚生了一个{gender},请起名，仅告知我名字无需其他内容。'
)

#chain = prompt | model | parser | model            #AIMessage
chain = prompt | model | parser | model | parser    #<class 'str'>

res = chain.invoke({'lastname':'张','gender':'男'})
print(res)
print(type(res))                      
