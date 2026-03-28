from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.messages import HumanMessage,SystemMessage,AIMessage

chat = ChatTongyi(model = 'qwen3-max')

'''
messages = [
    SystemMessage(content = '你是以为来自边塞的诗人'),
    HumanMessage(content='给我写一首唐诗'),
    AIMessage(content='锄禾日当午，汗滴禾下土，谁知盘中餐，粒粒皆辛苦。'),
    HumanMessage(content='给予你上一首诗的格式，再来一首')
]
'''
messages = [
    ('system','你是以为来自边塞的诗人'),
    ('human','给我写一首唐诗'),
    ('ai','锄禾日当午，汗滴禾下土，谁知盘中餐，粒粒皆辛苦。'),
    ('human','给予你上一首诗的格式，再来一首')
]

for chunk in chat.stream(input=messages):
    print(chunk.content,end='',flush=True)

