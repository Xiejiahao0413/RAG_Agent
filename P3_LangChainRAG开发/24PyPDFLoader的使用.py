from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader(
    file_path='./P3_langChainRAG开发/data/pdf2.pdf',
    mode ="page",             #mode: Literal["single", "page"] = "page",single:不管有多少页，只返回1个Document对象
    password = "itheima",
)

i  = 0
for doc in loader.lazy_load():
    i += 1
    print(doc)
    print("="*20,i)