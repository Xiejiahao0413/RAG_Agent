"""
提示词：用户的提问 + 向量库中检索到的参考资料
"""


from langchain_community.chat_models import ChatTongyi
from langchain_community.vectorstores import InMemoryVectorStore
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

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

#检索向量库
result = vector_store.similarity_search(input_text,2)
#print(result)   
#[Document(page_content='减肥就是少吃多练'), Document(page_content='在减脂期间吃东西很重要，清淡减少控制卡路里的摄入并且需要运动起来')]

reference_text = "["
for doc in result:
    reference_text += doc.page_content
reference_text += "]"

print(reference_text)    #[减肥就是少吃多练在减脂期间吃东西很重要，清淡减少控制卡路里的摄入并且需要运动起来]

def print_prompt(prompt):
    print(prompt.to_string())
    print("="*20)
    return prompt

chian = prompt | print_prompt | model | StrOutputParser()
res = chian.invoke({"input":input_text,"content":reference_text})
print(res)
print(type(prompt))   #<class 'langchain_core.prompts.chat.ChatPromptTemplate'>