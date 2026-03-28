from langchain_community.document_loaders import JSONLoader

loader = JSONLoader(
    file_path='./P3_LangChainRAG开发/data/stu.json',
    jq_schema='.',
    text_content=False,    #告知JSONLoader，我抽取的内容不是字符串
)

document = loader.load()
print(document)