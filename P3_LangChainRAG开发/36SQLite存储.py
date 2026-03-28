import sqlite3
import json
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.messages import BaseMessage, message_to_dict, messages_from_dict

class SQLiteChatHistory(BaseChatMessageHistory):
    """SQLite 持久化存储"""
    
    def __init__(self, session_id: str, db_path: str = "chat_history.db"):
        self.session_id = session_id
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self._create_table()
    
    def _create_table(self):
        cursor = self.conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS chat_history (
                session_id TEXT,
                messages TEXT,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                PRIMARY KEY (session_id)
            )
        """)
        self.conn.commit()
    
    @property
    def messages(self):
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT messages FROM chat_history WHERE session_id = ?",
            (self.session_id,)
        )
        row = cursor.fetchone()
        if row:
            messages_dict = json.loads(row[0])
            return messages_from_dict(messages_dict)
        return []
    
    def add_message(self, message: BaseMessage):
        messages = self.messages
        messages.append(message)
        
        messages_dict = [message_to_dict(m) for m in messages]
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT OR REPLACE INTO chat_history (session_id, messages)
            VALUES (?, ?)
        """, (self.session_id, json.dumps(messages_dict)))
        self.conn.commit()
    
    def clear(self):
        cursor = self.conn.cursor()
        cursor.execute(
            "DELETE FROM chat_history WHERE session_id = ?",
            (self.session_id,)
        )
        self.conn.commit()
    
    def __del__(self):
        self.conn.close()

# 使用
def get_session_history(session_id: str):
    return SQLiteChatHistory(session_id, "my_chat_history.db")