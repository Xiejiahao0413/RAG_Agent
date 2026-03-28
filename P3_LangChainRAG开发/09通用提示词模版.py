from langchain_core.prompts import PromptTemplate
from langchain_community.llms.tongyi import Tongyi

prompt_template = PromptTemplate.from_template(
    '我的邻居姓{lastname},刚生了{gender}，帮忙其名字，请简略回答。'
)

# prompt_text = prompt_template.format(lastname='张',gender='女儿')
# model = Tongyi(model='qwen-max')
# res = model.invoke(input=prompt_text)
# print(res)

#链式输入
model = Tongyi(model='qwen-max')
chain = prompt_template | model
res = chain.invoke(input={'lastname':'张','gender':'女'})
print(res)

