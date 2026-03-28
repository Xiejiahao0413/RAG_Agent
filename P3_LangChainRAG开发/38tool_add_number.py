from langchain.tools import tool
@tool
def add_number(a:int,b:int)->int:
    """两个整数相加"""
    return a + b
print(f"name = {add_number.name}")
print(f"args = {add_number.args}")
print(f"description = {add_number.description}")
print(f"return_direct = {add_number.return_direct}")
res = add_number.invoke({"a":10,"b":20})
print(res)
"""
name = add_number
args = {'a': {'title': 'A', 'type': 'integer'}, 'b': {'title': 'B', 'type': 'integer'}}
description = add_number(a: int, b: int) -> int - 两个整数相加
return_direct = False
30

return_direct参数 的默认值是False。当return_direct=False时，工具执行结果会返回给
Agent，让Agent决定下一步操作；而return_direct=True则会中断这个循环，直接结束流程，返回结
果给用户。
"""





from langchain.tools import tool
@tool(name_or_callable="add_two_number",description="two numberadd",return_direct=True)
def add_number(a:int,b:int)->int:
    """两个整数相加"""
    return a + b
print(f"name = {add_number.name}")
print(f"description = {add_number.description}")
print(f"args = {add_number.args}")
print(f"return_direct = {add_number.return_direct}")
res = add_number.invoke({"a":10,"b":20})
print(res)
"""
name = add_two_number
description = two number add
args = {8a8: {8title8: 8A8, 8type8: 8integer8}, 8b8: {8title8: 8B8, 8type8: 8integer8}}
return_direct = True
30
"""





from langchain.tools import tool
from pydantic import BaseModel, Field
class FieldInfo(BaseModel):
    a :int = Field(description="第1个参数")
    b :int = Field(description="第2个参数")
@tool(name_or_callable="add_two_number",description="two numberadd",args_schema=FieldInfo,return_direct=True)
def add_number(a:int,b:int)->int:
    """两个整数相加"""
    return a + b
print(f"name = {add_number.name}")
print(f"description = {add_number.description}")
print(f"args = {add_number.args}")
print(f"return_direct = {add_number.return_direct}")
res = add_number.invoke({"a":10,"b":20})
print(res)
"""
name = add_two_number
description = two number add
args = {8a8: {8description8: '第1个参数', 8title8: 8A8, 8type8: 8integer8}, 8b8: {8description8: '第2个参数',
8title8: 8B8, 8type8: 8integer8}}
return_direct = True
30
"""




