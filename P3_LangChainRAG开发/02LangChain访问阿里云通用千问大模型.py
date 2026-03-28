from langchain_community.llms.tongyi import Tongyi

model = Tongyi(model='qwen-max')

#调用invoke向模型提问
res = model = model.invoke(input='你是谁呀你能做什么？')
print(res)


