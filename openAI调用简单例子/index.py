import os
from openai import OpenAI
from dotenv import load_dotenv

# 加载 .env 文件中的环境变量
load_dotenv()

# Retrieve the API key from an environment variable
api_key = os.getenv("OPENAI_API_KEY")
base_url = os.getenv("BASE_URL")
model = os.getenv("MODEL", "gpt-3.5-turbo")
# 检查环境变量是否存在
if not api_key:
    raise ValueError("API key not found. Please set the OPENAI_API_KEY environment variable.")
if not base_url:
    raise ValueError("Base URL not found. Please set the BASE_URL environment variable.")

# 创建 OpenAI 客户端
# 如果使用代理服务,请设置 BASE_URL 环境变量,否则请删除此行
client = OpenAI(
    api_key = api_key,
    base_url = base_url  # 网络代理服务地址
)

# 创建一个聊天完成请求
content = "请向我解释一下大模型是黑箱的吗？并给出一些例子。"
chat_completion = client.chat.completions.create(
    messages = [
        {
            "role": "user",
            "content": content,
        }
    ],
    model = model,  # 此处更换其它模型,请参考模型列表 eg: google/gemma-7b-it
)
print(chat_completion.choices[0].message.content)
