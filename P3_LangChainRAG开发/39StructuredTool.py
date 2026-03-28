"""
StructuredTool.from_function 类方法提供了比 @tool 装饰器更多的可配置性，而无需太多额外的代码。
"""
from langchain_core.tools import StructuredTool
def search_function(query: str):
    return "LangChain"
search1 = StructuredTool.from_function(
    func=search_function,
    name="Search",
    description="useful for when you need to answer questions about current events"
    )
print(f"name = {search1.name}")
print(f"description = {search1.description}")
print(f"args = {search1.args}")
search1.invoke("hello")
"""
name = Search
description = Search(query: str) - useful for when you need to answer questions about current events
args = {'query': {'title': 'Query', 'type': 'string'}}
"""



from langchain_core.tools import StructuredTool
from pydantic import Field,BaseModel
class FieldInfo(BaseModel):
    query: str = Field(description="要检索的关键词")
def search_function(query: str):
    return "LangChain"
search1 = StructuredTool.from_function(
    func=search_function,
    name="Search",
    description="useful for when you need to answer questions about current events",
    args_schema=FieldInfo,
    return_direct=True,
    )
print(f"name = {search1.name}")
print(f"description = {search1.description}")
print(f"args = {search1.args}")
print(f"return_direct = {search1.return_direct}")
search1.invoke("hello")
"""
name = Search
description = useful for when you need to answer questions about current events
args = {8query8: {8description8: '要检索的关键词', 8title8: 8Query8, 8type8: 8string8}}
return_direct = True
8LangChain8
"""


