from langchain_ollama import OllamaLLM 

model =OllamaLLM(model='qwen3:4b')

#invoke方法：一次性返回完整结果
#stream方法：逐段返回结果，流式输出
res =model.invoke(input='你是谁呀能做什么？')

print(res)




