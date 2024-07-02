import os

import chainlit as cl

from query import chat_response


@cl.on_chat_start
async def on_chat_start():
    cl.user_session.set("history", [])
    await cl.Message(
        content="Hello, kindly write your queries related to electoral bond."
    ).send()


@cl.on_message
async def factory(message: str):
    question = message.content
    response = chat_response(question)

    await cl.Message(content=response).send()
