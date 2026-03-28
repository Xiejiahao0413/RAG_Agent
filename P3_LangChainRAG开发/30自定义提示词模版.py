from typing import List, Dict, Any
from langchain.prompts import BasePromptTemplate
from langchain.prompts import PromptTemplate
from langchain.schema import PromptValue

# 2.自定义提示词模版
class SimpleCustomPrompt(BasePromptTemplate):
    """简单自定义提示词模板"""
    template: str
    
    def __init__(self, template: str, **kwargs):
        # 使用PromptTemplate解析输入变量
        prompt = PromptTemplate.from_template(template)

        super().__init__(
            input_variables=prompt.input_variables,
            template=template,
            **kwargs
        )
    def format(self, **kwargs: Any) -> str:
        """格式化提示词"""
        # print("kwargs:", kwargs)
        # print("self.template:", self.template)
        return self.template.format(**kwargs)
    
    def format_prompt(self, **kwargs: Any) -> PromptValue:
        """实现抽象方法"""
        return PromptValue(text=self.format(**kwargs))
    
    @classmethod
    def from_template(cls, template: str, **kwargs) -> "SimpleCustomPrompt":
        """从模板创建实例"""
        return cls(template=template, **kwargs)

# 3.使用自定义提示词模版
custom_prompt = SimpleCustomPrompt.from_template(
    template="请回答关于{subject}的问题：{question}"
)

# 4.格式化提示词
formatted = custom_prompt.format(
    subject="人工智能",
    question="什么是LLM？"
)

print(formatted)