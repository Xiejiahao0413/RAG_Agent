from langchain_community.llms.tongyi import Tongyi
import json
import shutil
import os

# 创建模型
chat_model = Tongyi(model="qwen3-max", temperature=0)

# 定义工具函数
def move_file(source_path: str, destination_path: str) -> str:
    """移动文件"""
    try:
        source_path = os.path.expanduser(source_path)
        destination_path = os.path.expanduser(destination_path)
        
        if not os.path.exists(source_path):
            return f"错误：源文件 '{source_path}' 不存在"
        
        if not os.path.isfile(source_path):
            return f"错误：'{source_path}' 不是一个文件"
        
        # 确保目标目录存在
        dest_dir = os.path.dirname(destination_path)
        if dest_dir and not os.path.exists(dest_dir):
            os.makedirs(dest_dir, exist_ok=True)
        
        result = shutil.move(source_path, destination_path)
        return f"✅ 成功将文件移动到：{result}"
    except Exception as e:
        return f"❌ 移动失败：{str(e)}"

# 创建测试文件
test_file = "test_a.txt"
if not os.path.exists(test_file):
    with open(test_file, 'w', encoding='utf-8') as f:
        f.write("这是一个测试文件，用于测试文件移动功能。")
    print(f"✅ 创建测试文件：{test_file}")

# 获取桌面路径
desktop = os.path.join(os.path.expanduser("~"), "Desktop")
destination = os.path.join(desktop, "test_a.txt")

print(f"\n目标路径：{destination}")

# 方法1：直接使用简单的提示词（最简单可靠）
print("\n" + "="*50)
print("方法1：直接提示词方式")
print("="*50)

prompt = f"""你是一个文件操作助手。

用户请求：将文件 '{test_file}' 移动到桌面（路径：{destination}）

请判断这个请求是否合理，并给出回复。如果合理，请说明你将执行移动操作。
"""

try:
    response = chat_model.invoke(prompt)
    print(f"模型回复：\n{response}")
    
    # 询问是否执行
    user_input = input("\n是否执行文件移动？(y/n): ")
    if user_input.lower() == 'y':
        result = move_file(test_file, destination)
        print(f"\n执行结果：{result}")
    else:
        print("已取消操作")
        
except Exception as e:
    print(f"错误：{e}")

# 验证结果
print("\n" + "="*50)
print("验证结果：")
print("="*50)
if os.path.exists(destination):
    print(f"✅ 文件已成功移动到：{destination}")
    with open(destination, 'r', encoding='utf-8') as f:
        content = f.read()
    print(f"文件内容：{content}")
elif os.path.exists(test_file):
    print(f"文件仍在原位置：{test_file}")
else:
    print("文件可能已被删除或移动")