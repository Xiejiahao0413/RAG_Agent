from langchain_community.embeddings import DashScopeEmbeddings
from langchain_community.document_loaders import CSVLoader
from langchain_chroma import Chroma


vector_store =Chroma(
    collection_name="test",               #当前向量存储起个名字，类似数据库的表名称
    embedding_function = DashScopeEmbeddings(),    #嵌入模型
    persist_directory="./P3_LangChainRAG开发/chroma_db"  #指定数据存储的文件夹
)

loader = CSVLoader(
    file_path = "./P3_LangChainRAG开发/data/info.csv",
    encoding="utf-8",
    source_column="source",
)

documents = loader.load()

#向量存储的新增，删除，检索
vector_store.add_documents(
    documents = documents,          #被添加的论文，类型是list[documents]
    ids = ["id"+str(i) for i in range(1,len(documents)+1)]    #list[str]
)

#删除 转入[id,id...]
vector_store.delete(["id1","id2"])

#检索
result = vector_store.similarity_search(
    "python是不是简单易学",
    3
)

print(result)