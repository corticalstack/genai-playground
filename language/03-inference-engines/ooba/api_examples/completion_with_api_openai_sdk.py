from openai import OpenAI

client = OpenAI(api_key="...", base_url="http://127.0.0.1:5000/v1")

user_prompt = """
What is the capital of Spain?
"""
response = client.chat.completions.create(
    model="",
    messages=[{"role": "user", "content": user_prompt}],
    temperature=0.2,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
    stream=False,
)
print(response.choices[0].message.content)