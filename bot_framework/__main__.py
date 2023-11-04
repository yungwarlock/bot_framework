from bot_framework import Output, Input, Pipeline, Lambda

graph =(
    "Entry point" >> Pipeline()
    | "Prints Hello World" >> Output(message="Hello")
    | "Asks for my name" >> Input("What is your name?")
    | "Greets user" >> Lambda(lambda read, write: write(f"Hello {read()}"))
    | "Asks what they do" >> Input("What do you do?")
    | "Prints what they do" >> Lambda(lambda read, write: write(f"I see, you {read()}"))
    | "End" >> Output(message="Goodbye")
)

if __name__ == "__main__":

    graph.run(debug=True)
