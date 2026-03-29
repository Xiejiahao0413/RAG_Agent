from langchain.agents import create_agent
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.tools import tool


@tool(description="查询天气")
def get_weather() -> str:
    return "晴天"


@tool
def get_price(name:str) -> str:
    return f"股票{name}的价格是20元"


@tool
def get_info(name:str) -> str :
    return f"股票{name}，是一家A股上市公司，专注于IT职业教育"


agent = create_agent(
    model = ChatTongyi(model = "qwen3-max"),
    tools = [get_info,get_price],
    system_prompt = "你是一个聊天助手，可以回答用户问题。",
)

for chunk in agent.stream(
    {"messages":[{"role":"user","content":"明天深圳天气如何？"}]
    },
    stream_mode="values",
):
    
    last_message = chunk["messages"][-1]
  
    if last_message.content:
        print(type(last_message).__name__,last_message.content)

    try:
        if last_message.tool_calls:
            print(f"工具调用:{ [tc['name'] for tc in last_message.tool_calls]}")
    except AttributeError as e :
        pass


