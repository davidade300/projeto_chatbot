from openai import OpenAI
import os

openai = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

response = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{
        "role": "system",
        "content": "you are a helpful assistant,"
                   + " you will have conversations in brazilian portuguese and you will not hallucinate"
    }, {"role": "user",
        "content": "você entende português?"
        }],
)

print(response.choices[0].message.content)
