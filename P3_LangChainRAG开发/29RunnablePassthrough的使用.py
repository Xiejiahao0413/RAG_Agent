"""
提示词：用户的提问 + 向量库中检索到的参考资料
"""

from langchain_core.documents import Document
from langchain_community.chat_models import ChatTongyi
from langchain_community.vectorstores import InMemoryVectorStore
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

def print_prompt(prompt):
    print(prompt.to_string())
    print("="*20)
    return prompt

model = ChatTongyi(model="qwen3-max")
prompt = ChatPromptTemplate.from_messages(
    [
        ("system","以我提供的已知参考资料为主，简洁和专业的回答用户问题。参考资料：{content}"),
        ("user","用户提问：{input}")
    ]
)

vector_store = InMemoryVectorStore(
    embedding =DashScopeEmbeddings(model = "text-embedding-v4")
)

#准备一下资料（向量库中的资料）
#add_texts 传入一个list[str]
vector_store.add_texts(["减肥就是少吃多练","在减脂期间吃东西很重要，清淡减少控制卡路里的摄入并且需要运动起来","跑步是很好的运动哦"])

input_text = "怎么减肥"

#langchain中向量的存储对象，有一个方法：as_retriever,可以返回一个Runnable接口的子类实例对象
retriever = vector_store.as_retriever(search_kwargs = {"k":2})

def format_func(docs: list[Document]):
    if not docs:
        return "无参考对象"
    formatted_str = "["
    for doc in docs:
        formatted_str +=doc.page_content
    formatted_str += "]"
    
    return formatted_str

#chain = retriever | prompt | model | StrOutputParser()
chain = (
    {
        "input":RunnablePassthrough(),
        "content":retriever | format_func
    } 
    | prompt 
    | print_prompt 
    | model 
    | StrOutputParser() 
)

res = chain.invoke(input_text)
print(res)

"""
retriever:
        --输入：用户的提问     str
        --输出：向量库检索结果 list[Document]
prompt:
        --输入：用户的提问+向量库检索的结果   dict
        --输出：完整的提示词                 PromptValue
"""
#----------------------------------------------------------------------------
"""
Human: 用户提问：怎么减肥
====================
减肥的关键在于“少吃多练”：  
1. **饮食方面**：选择清淡食物，控制总热量摄入，避免高糖高脂食品。
2. **运动方面**：坚持规律运动，如快走、跑步、力量训练等，有助于消耗脂肪、提升代谢。

两者结合，才能健康有效地减脂。
"""


