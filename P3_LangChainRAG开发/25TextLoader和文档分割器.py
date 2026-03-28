from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

loader = TextLoader("./P3_LangChainRAG开发/data/Python基础语法.txt",encoding="utf-8")

docs = loader.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size = 500,                #分段最大字符数
    chunk_overlap = 50,              #分段之间允许重复字符数
    separators=["\n\n","\n",",",".","!","?","，","。","！","？"," ",""],   #文本自然段落分割的数据符号
    length_function =len,            #统计字符数的依据函数
)

split_docs = splitter.split_documents(docs)
print(len(split_docs))
for doc in split_docs:
    print("="*20)
    print(doc)
    print("="*20)