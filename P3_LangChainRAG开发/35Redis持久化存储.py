"""
对于你的学习项目，我推荐：

学习阶段：使用 InMemoryChatMessageHistory（最简单）

需要持久化：使用 SQLiteChatHistory（无需额外安装）

生产环境：使用 Redis 或 PostgreSQL
"""

# import redis
# import json
# from langchain_core.chat_history import BaseChatMessageHistory
# from langchain_core.messages import BaseMessage, message_to_dict, messages_from_dict

# class RedisChatHistory(BaseChatMessageHistory):
#     """Redis 持久化存储"""
    
#     def __init__(self, session_id: str, redis_client: redis.Redis, ttl: int = 3600):
#         self.session_id = session_id
#         self.redis_client = redis_client
#         self.ttl = ttl
#         self._key = f"chat_history:{session_id}"
    
#     @property
#     def messages(self):
#         """从Redis读取消息"""
#         data = self.redis_client.get(self._key)
#         if data:
#             messages_dict = json.loads(data)
#             return messages_from_dict(messages_dict)
#         return []
    
#     def add_message(self, message: BaseMessage):
#         """添加消息到Redis"""
#         messages = self.messages
#         messages.append(message)
        
#         # 序列化并存储
#         messages_dict = [message_to_dict(m) for m in messages]
#         self.redis_client.setex(
#             self._key, 
#             self.ttl, 
#             json.dumps(messages_dict)
#         )
    
#     def clear(self):
#         """清空历史"""
#         self.redis_client.delete(self._key)

# # 使用
# redis_client = redis.Redis(host='localhost', port=6379)

# def get_session_history(session_id: str):
#     return RedisChatHistory(session_id, redis_client)

# chain_with_history = RunnableWithMessageHistory(
#     chain,
#     get_session_history,
#     input_messages_key="input",
#     history_messages_key="chat_history",
# )
