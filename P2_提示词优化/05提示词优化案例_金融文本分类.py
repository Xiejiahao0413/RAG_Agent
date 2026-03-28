from openai import OpenAI
import os

client = OpenAI(
    # 如果没有配置环境变量，请用阿里云百炼API Key替换：api_key="sk-xxx"
    #api_key="sk-b3514ee3fae4476a8f19e3643795c5f9",
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

# 示例数据
examples_data = {
    '新闻报道':'今日,股市经历了一轮震荡,受到宏观经济数据和全球贸易紧张局势的影响。投资者密切关注美联储可能的政策调整,以适应市场的不确定性。',
    '财务报告':'本公司年度财务报告显示,去年公司实现了稳步增长的盈利,同时资产负债表呈现强劲的状况。经济环境的稳定和管理层的有效战略执行为公司的健康为展提供了坚实的基础。',
    '公司公告':'本公司高兴地宣布成功完成最新一轮并购交易,收购了一家在人工智能领域领先的公司。这一战略举措将有助于扩大我们的业务领域,提高市场竞争力,并为股东创造更大的价值。我们期待着与新团队的合作,共同推动公司的未来发展。',
    '分析师报告':'最新的行业分析报告指出,科技公司的创新将成为未来增长的主要推动力。云计算、人工智能和数字化转型被认为是引领行业发展的关键因素,投资者应该密切关注这些领域的投资机会。分析师建议投资者在选择科技股票时,要考虑公司的创新能力、市场份额和财务健康状况。'
}
# 分类列表
examples_types =['新闻报道','财务报道','公司公告','分析师报告']

#提问数据
questions = [
    '今日,央行发布公告宣布降低利率,以刺激经济增长。这一降息举措将影响贷款利率,并在未来几个季度内对金融市场产生影响。',
    '小明喜欢小新哟',
    'ABC公司今日发布公告称,已成功完成对XYZ公司股权的收购交易。本次交易是ABC公司在抗大业务范围、加强市场竞争力方面的重要举措。据悉,此次收购将进一步成功整合双方资源,提升公司的创新能力和市场份额。',
    '公司资产负债表显示,公司偿债能力强劲,现金流充足,为未来投资和扩张提供了坚实的财务基础。',
    '最新的分析报告指出,可再生能源行业预计将在未来几年经历持续增长,投资者应该关注这一领域的投资机会'
    
]


"""
question=[
    {"role": "system", "content": "你是一个金融专家,负责将文本分类到以下类别中: ['新闻报道', '财务报告', '公司公告', '分析师报告']。如果无法确定分类,请回答'不清楚'。"},
    
    {"role": "user", "content": '今日，央行发布公告宣布降低...'},
    {"role": "assistant", "content": "新闻报道"},
    {"role": "user", "content": 'ABC公司今日发布公告称,已成功完成对XYZ公司股权的收购交易...'},
    {"role": "assistant", "content": "财务报告"},
    {"role": "user", "content": '公司资产负债表显示,公司偿债能力强劲,现金流充足...'},
    {"role": "assistant", "content": "分析师报告"},
    {"role": "user", "content": '要提问的问题'},

    {"role": "assistant", "content": "不清楚"}
]
"""


messages = [
    {"role": "system", "content": "你是一个金融专家,负责将文本分类到以下类别中: ['新闻报道', '财务报告', '公司公告', '分析师报告']。如果无法确定分类,请回答'不清楚'。"}
]

for key,value in examples_data.items():
    messages.append({'role':'user','content':value})
    messages.append({'role':'assistant','content':key})

# for x in messages:
#     print(x)

#向模型提问
for q in questions:
    response = client.chat.completions.create(
        model = 'qwen3-max',
        messages = messages+[{'role':'user','content':f'按照实例，回答这段文本的分类类别:{q}'}]
    )

    print(response.choices[0].message.content)

