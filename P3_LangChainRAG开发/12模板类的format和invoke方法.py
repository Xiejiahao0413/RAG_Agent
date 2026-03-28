from langchain_core.prompts import PromptTemplate
from langchain_core.prompts import FewShotPromptTemplate
from langchain_core.prompts import ChatPromptTemplate

template =PromptTemplate.from_template('我的令居是：{lastname},最喜欢{hobby}')

res = template.format(lastname='张大妈',hobby='唱歌')
print(res,type(res))                                         #<class 'str'>


res2 =template.invoke({'lastname':'周杰伦','hobby':'唱歌'})
print(res2,type(res2))                                       #<class 'langchain_core.prompt_values.StringPromptValue'>