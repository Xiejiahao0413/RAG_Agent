from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.messages import HumanMessage,AIMessage

#创建历史对象
history = InMemoryChatMessageHistory()

#添加信息
history.add_user_message("LangChain是什么?")
history.add_ai_message("LangChain是一个开发LLM应用的框架")

#查看所有信息
for msg in history.messages:
    print(f"{msg.type}:{msg.content}")

#获取最近N条信息
recent = history.messages[-4]

#清空历史
history.clear()

# 多会话管理
class SessionManager:
    def __init__(self):
        self.sessions = {}
    
    def get_history(self, session_id: str):
        if session_id not in self.sessions:
            self.sessions[session_id] = InMemoryChatMessageHistory()
        return self.sessions[session_id]

manager = SessionManager()
history1 = manager.get_history("user_123")
history2 = manager.get_history("user_456")

