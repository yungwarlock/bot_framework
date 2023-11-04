from bot_framework import Output, Input

graph =(
    "Entry point" >> Output(message="Hello")
    | "Asks for my name" >> Input("What is your name?")
    | "Prints Hello World" >> Output(message="World")
    | Output(message="From")
    | Output(message="Output")
    | Output(message="JS")
)

if __name__ == "__main__":

    graph.run(debug=True)
