# from langchain_community.tools.tavily_search import TavilySearchResults
# from langchain.agents import create_tool_calling_agent, AgentExecutor
# from langchain import hub
# from langchain_community.chat_models import ChatTongyi
# import os

# # 1. 设置搜索 API 密钥
# os.environ["TAVILY_API_KEY"] = "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"

# # 2. 初始化搜索工具
# search = TavilySearchResults(max_results=3)

# # 3. 初始化 Qwen3-Max 模型（使用系统环境变量中的 DASHSCOPE_API_KEY）
# llm = ChatTongyi(
#     model="qwen3-max",  # Qwen3-Max 模型
#     temperature=0,
#     # 可选参数
#     # top_p=0.8,
#     # max_tokens=2000
# )

# # 4. 创建 Agent（使用 tool calling）
# agent = create_tool_calling_agent(
#     llm=llm,
#     tools=[search],
#     prompt=hub.pull("hwchase17/openai-tools-agent")
# )

# # 5. 创建 AgentExecutor
# agent_executor = AgentExecutor(
#     agent=agent,
#     tools=[search],
#     verbose=True,
#     handle_parsing_errors=True
# )

# # 6. 测试查询
# if __name__ == "__main__":
#     query = "今天北京的天气怎么样？"
#     result = agent_executor.invoke({"input": query})
#     print(f"查询结果: {result['output']}")


# 40tavily搜索工具.py - 使用 ReAct Agent
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub
from langchain_community.chat_models import ChatTongyi
from langchain_core.prompts import PromptTemplate
import os

# 1. 设置 API 密钥
os.environ["TAVILY_API_KEY"] = "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"

# 2. 初始化搜索工具
search = TavilySearchResults(max_results=3)

# 3. 初始化 Qwen 模型
llm = ChatTongyi(
    model="qwen-max",
    temperature=0,
)

# 4. 定义 ReAct 提示词模板
react_prompt = PromptTemplate.from_template("""你是一个有用的AI助手，可以使用工具来回答问题。

你可以使用以下工具：
{tools}

工具名称: {tool_names}

使用以下格式回答：
Question: 用户的问题
Thought: 思考需要做什么
Action: 要使用的工具名称，必须是 [{tool_names}] 中的一个
Action Input: 工具的输入参数
Observation: 工具返回的结果
... (这个 Thought/Action/Action Input/Observation 可以重复多次)
Thought: 我现在知道最终答案了
Final Answer: 对用户问题的最终回答

开始！

Question: {input}
Thought: {agent_scratchpad}""")

# 5. 创建 ReAct Agent
agent = create_react_agent(
    llm=llm,
    tools=[search],
    prompt=react_prompt
)

# 6. 创建 AgentExecutor
agent_executor = AgentExecutor(
    agent=agent,
    tools=[search],
    verbose=True,
    handle_parsing_errors=True,
    max_iterations=5
)

# 7. 测试查询
if __name__ == "__main__":
    print("="*50)
    print("开始查询...")
    print("="*50)
    
    query = "今天北京的天气怎么样？"
    print(f"问题: {query}\n")
    
    try:
        result = agent_executor.invoke({"input": query})
        print(f"\n回答: {result['output']}")
    except Exception as e:
        print(f"查询出错: {e}")
        print("\n尝试直接搜索...")
        try:
            search_result = search.invoke(query)
            print(f"搜索结果: {search_result}")
        except Exception as e2:
            print(f"搜索失败: {e2}")


# # test_connection.py
# import requests
# import time

# print("测试网络连接...\n")

# # 1. 测试阿里云（Qwen）
# print("1. 测试阿里云连接...")
# try:
#     start = time.time()
#     r = requests.get("https://dashscope.aliyuncs.com", timeout=5)
#     print(f"   ✓ 连接成功 ({time.time()-start:.2f}秒)")
# except Exception as e:
#     print(f"   ✗ 连接失败: {e}")

# # 2. 测试 Tavily
# print("\n2. 测试 Tavily 连接...")
# try:
#     start = time.time()
#     r = requests.get("https://api.tavily.com", timeout=5)
#     print(f"   ✓ 连接成功 ({time.time()-start:.2f}秒)")
# except Exception as e:
#     print(f"   ✗ 连接失败: {e}")

# # 3. 测试 GitHub (LangChain Hub)
# print("\n3. 测试 GitHub 连接...")
# try:
#     start = time.time()
#     r = requests.get("https://raw.githubusercontent.com", timeout=5)
#     print(f"   ✓ 连接成功 ({time.time()-start:.2f}秒)")
# except Exception as e:
#     print(f"   ✗ 连接失败: {e}")

# print("\n建议：")
# print("- 如果阿里云通，Tavily不通 → 需要代理或检查Tavily API Key")
# print("- 如果Tavily通，GitHub不通 → 需要代理或使用本地提示词")
# print("- 如果都不通 → 检查网络或开启代理")
