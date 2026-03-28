from openai import OpenAI
import os

client = OpenAI(
    api_key="sk-b3514ee3fae4476a8f19e3643795c5f9",
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)


completion = client.chat.completions.create(
    model="qwen3-max", 
    messages = [
    {"role": "system", "content": "you a helpful assistant."},
    {"role": "user", "content": "你是谁,你能做什么?"},
    ],
    stream=True
)

for chunk in completion:
        print(chunk.choices[0].delta.content, end="", flush=True)
