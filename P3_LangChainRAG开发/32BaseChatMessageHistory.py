
# from langchain_core.chat_history import BaseChatMessageHistory
# from langchain_core.messages import BaseMessage, HumanMessage, AIMessage
# from typing import List

# class BaseChatMessageHistory:
#     """会话历史基类"""
    
#     @property
#     def messages(self) -> List[BaseMessage]:
#         """获取所有消息"""
#         pass
    
#     def add_message(self, message: BaseMessage) -> None:
#         """添加单条消息"""
#         pass
    
#     def add_user_message(self, message: str) -> None:
#         """添加用户消息（便捷方法）"""
#         pass
    
#     def add_ai_message(self, message: str) -> None:
#         """添加AI消息（便捷方法）"""
#         pass
    
#     def clear(self) -> None:
#         """清空历史"""
#         pass


from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.messages import HumanMessage, AIMessage

class MyCustomHistory(BaseChatMessageHistory):
    """自定义历史实现"""
    
    def __init__(self):
        self._messages = []
    
    @property
    def messages(self):
        return self._messages
    
    def add_message(self, message):
        self._messages.append(message)
    
    def clear(self):
        self._messages.clear()

# 使用
history = MyCustomHistory()
history.add_user_message("你好")
history.add_ai_message("你好！有什么可以帮助你的？")
print(history.messages)
