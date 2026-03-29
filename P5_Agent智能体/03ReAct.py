from langchain.agents import create_agent
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.tools import tool


@tool(description="获取体重，返回值是整数，单位是千克")
def get_weigth() -> str:
    return 90


@tool
def get_heigth(name:str) -> str:
    return 172


agent = create_agent(
    model = ChatTongyi(model = "qwen3-max"),
    tools = [get_heigth,get_weigth],
    system_prompt = """你是一个严格遵循ReAct框架的智能体，必须按【思考-行动-观察-再思考】的流程来解决问题，且**每轮仅能思考并且调用一个工具**，
    禁止单词调用多个工具。并且告知我你的思考过程，工具的调用原因，按思考，行动，管擦三个结构告知我"""
)

for chunk in agent.stream(
    {"messages":[{"role":"user","content":"明计算我的BMI"}]
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


