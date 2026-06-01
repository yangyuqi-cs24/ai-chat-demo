import os
import openai
from dotenv import load_dotenv

# 加载 .env 文件中的环境变量
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def chat_with_ai(prompt):
    """调用 OpenAI API 进行对话"""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "你是一个友好、简洁的AI助手，回答问题时尽量清晰易懂。"},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=500
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"出错了：{str(e)}"

if __name__ == "__main__":
    print("🤖 AI 对话小工具（输入 'exit' 可退出）")
    while True:
        user_input = input("你：")
        if user_input.lower() == "exit":
            print("再见！")
            break
        reply = chat_with_ai(user_input)
        print(f"AI：{reply}\n")
