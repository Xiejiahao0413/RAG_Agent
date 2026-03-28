from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(
    file_path = './P3_LangChainRAG开发/data/stu.csv',
    csv_args={
        'delimiter':',',                 #指定分隔符
        'quotechar':'"',                 #指定带有分隔符文本的引号包围是单引号还是双引号
        #如果数据原本有表头，就不要把下面的代码，如果没有可以使用
        'fieldnames':['a','b','c','d']
    },
    encoding='utf-8'
)

documents = loader.load()

# for document in documents:
#     print(type(document),document)


for document in loader.lazy_load():
    print(document)