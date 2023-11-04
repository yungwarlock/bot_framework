from bot_framework import Output, Input

if __name__ == "__main__":
    graph =(
        "Entry point" >> Output(message="Hello")
        | "Asks for my name" >> Input("What is your name?")
        | "Prints Hello World" >> Output(message="World")
        | Output(message="From")
        | Output(message="Output")
        | Output(message="JS")
    )

    graph.invoke(debug=True)
