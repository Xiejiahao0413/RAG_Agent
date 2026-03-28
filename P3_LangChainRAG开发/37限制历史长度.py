# class LimitedHistory(BaseChatMessageHistory):
#     """限制历史长度"""
    
#     def __init__(self, max_messages: int = 10):
#         self.max_messages = max_messages
#         self._messages = []
    
#     @property
#     def messages(self):
#         return self._messages
    
#     def add_message(self, message):
#         self._messages.append(message)
#         # 限制长度
#         if len(self._messages) > self.max_messages:
#             self._messages = self._messages[-self.max_messages:]
    
#     def clear(self):
#         self._messages.clear()




# #自动摘要历史
# class SummarizingHistory(BaseChatMessageHistory):
#     """自动摘要历史"""
    
#     def __init__(self, llm, max_tokens: int = 2000):
#         self.llm = llm
#         self.max_tokens = max_tokens
#         self._messages = []
#         self._summary = ""
    
#     @property
#     def messages(self):
#         return self._messages
    
#     def add_message(self, message):
#         self._messages.append(message)
        
#         # 检查是否需要摘要
#         if len(str(self._messages)) > self.max_tokens:
#             self._summarize()
    
#     def _summarize(self):
#         """摘要历史"""
#         from langchain_core.prompts import ChatPromptTemplate
        
#         prompt = ChatPromptTemplate.from_messages([
#             ("system", "总结以下对话历史，保留关键信息："),
#             ("human", "{history}")
#         ])
        
#         chain = prompt | self.llm | StrOutputParser()
#         self._summary = chain.invoke({"history": self._messages})
        
#         # 清空详细历史，只保留摘要
#         self._messages = []
    
#     def get_context(self):
#         """获取上下文（摘要+最近消息）"""
#         context = []
#         if self._summary:
#             context.append(SystemMessage(content=f"历史摘要：{self._summary}"))
#         context.extend(self._messages[-5:])  # 最近5条
#         return context
    


# #多用户管理
# class MultiTenantHistory:
#     """多租户历史管理"""
    
#     def __init__(self, storage_backend="memory"):
#         self.storage_backend = storage_backend
#         self.histories = {}
        
#     def get_history(self, tenant_id: str, user_id: str):
#         session_key = f"{tenant_id}:{user_id}"
        
#         if session_key not in self.histories:
#             if self.storage_backend == "redis":
#                 self.histories[session_key] = RedisChatHistory(session_key, redis_client)
#             else:
#                 self.histories[session_key] = InMemoryChatMessageHistory()
        
#         return self.histories[session_key]

# # 使用
# manager = MultiTenantHistory("redis")

# def get_session_history(session_id: str):
#     # session_id 格式: tenant:user
#     tenant, user = session_id.split(":")
#     return manager.get_history(tenant, user)

# chain_with_history = RunnableWithMessageHistory(
#     chain,
#     get_session_history,
#     input_messages_key="input",
#     history_messages_key="chat_history",
# )

# # 不同租户不同用户
# result1 = chain_with_history.invoke(
#     {"input": "你好"},
#     config={"configurable": {"session_id": "companyA:user123"}}
# )

# result2 = chain_with_history.invoke(
#     {"input": "你好"},
#     config={"configurable": {"session_id": "companyB:user456"}}
# )




# #完整生产级别实现
# # 完整的生产级实现
# class ProductionChatHistory:
#     def __init__(self, redis_client, llm):
#         self.redis = redis_client
#         self.llm = llm
    
#     def create_chain(self):
#         prompt = ChatPromptTemplate.from_messages([
#             ("system", "你是一个有用的助手"),
#             ("placeholder", "{chat_history}"),
#             ("human", "{input}")
#         ])
        
#         chain = prompt | self.llm | StrOutputParser()
        
#         def get_history(session_id):
#             return RedisChatHistory(session_id, self.redis)
        
#         return RunnableWithMessageHistory(
#             chain,
#             get_history,
#             input_messages_key="input",
#             history_messages_key="chat_history",
#         )

# # 使用
# chat = ProductionChatHistory(redis_client, llm)
# chain = chat.create_chain()

# result = chain.invoke(
#     {"input": "你好"},
#     config={"configurable": {"session_id": "user123"}}
# )