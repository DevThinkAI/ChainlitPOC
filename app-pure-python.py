import chainlit as cl

@cl.on_message
def main (message):

    

    # Send a response back to the user
    cl.Message(
        content=f"Received: {message}",
    ).send()

