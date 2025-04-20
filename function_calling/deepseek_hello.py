import time

from deepseek_client import client, DEEPSEEK_REASONER_MODEL, DEEPSEEK_CHAT_MODEL

start_time = time.time()

completion = client.chat.completions.create(
    model=DEEPSEEK_REASONER_MODEL,
    messages=[
        {'role': 'system', 'content': '你是一个足球领域的专家，请尽可能地帮我回答与足球相关的问题。'},
        {'role': 'user', 'content': 'C罗是哪个国家的足球运动员？'},
        {'role': 'assistant', 'content': 'C罗是葡萄牙足球运动员。'},
        {'role': 'user', 'content': '内马尔呢？'},
    ]
)

end_time = time.time()

print(f"耗时: {end_time - start_time} 秒")

# 通过reasoning_content字段打印思考过程
print("思考过程：")
print(completion.choices[0].message.reasoning_content)

# 通过content字段打印最终答案
print("最终答案：")
print(completion.choices[0].message.content)
