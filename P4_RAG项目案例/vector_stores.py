from langchain_chroma import Chroma
import config_data as config


class VectorStoreServiece(object):
    def __init__(self,embedding):
        """
        :param embedding:嵌入模型的传入
        """
        self.embedding = embedding

        self.vector_store = Chroma(
            collection_name = config.collection_name,
            embedding_function=self.embedding,
            persist_directory=config.persist_directory,   #数据库本地存储文件夹
        )

    def get_retriever(self):
        """返回向量检索器，方便加入chain"""
        return self.vector_store.as_retriever(search_kwargs={"k":config.similary_thredshold})
    




if __name__ == '__main__':
    from langchain_community.embeddings import DashScopeEmbeddings
    retriever = VectorStoreServiece(
        DashScopeEmbeddings(model="text-embedding-v4")
    ).get_retriever()
    
    res = retriever.invoke("我的体重是180斤，尺码推荐")
    print(res)
    print(f"数据库路径: {config.persist_directory}")
    print(f"集合名称: {config.collection_name}")
