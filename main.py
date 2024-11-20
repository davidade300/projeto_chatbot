import os
from typing import Annotated

from fastapi import FastAPI, Form
from openai import OpenAI
from rich.console import Console

from prompts.py_instructor import py_instructor_prompt

app = FastAPI()

openai = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

chat_log = [{"role": "system", "content": py_instructor_prompt}]

console = Console()


@app.post("/")
async def chat(user_input: Annotated[str, Form()]):
    chat_log.append({"role": "user", "content": user_input})

    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        temperature=0.7,
        messages=chat_log,
    )

    bot_response = response.choices[0].message.content
    chat_log.append({"role": "assistant", "content": bot_response})
    return bot_response
    # console.print(Markdown(bot_response))
