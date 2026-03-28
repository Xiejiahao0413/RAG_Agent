md5_path = "./md5.text"


#Chroma
collection_name = "rag"
#persist_directory = "./chroma_db"
import os
persist_directory = os.path.join(os.path.dirname(__file__), "chroma_db")

#spliter
chunk_size = 1000
chunk_overlap = 100
separators = ["\n\n","\n",",",".","?","!","，","。","！","？",""]
max_split_char_number = 1000    #文本分割阈值


similary_thredshold = 2    #返回的文件数量


