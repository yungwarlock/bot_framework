from bot_framework import Output, Input, Pipeline, Lambda, Router, Sleep

graph = (
    "Entry point" >> Pipeline()
    | "Prints Hello World" >> Output(message="Hello")
    | "Asks for my name" >> Input("What is your name?")
    | "Greets user" >> Lambda(lambda read, write: write(f"Hello {read()}"))
    | "Sleeps for 4 seconds" >> Sleep(seconds=4, message="Thinking...")
    | "Asks what they do" >> Input("What do you do?")
    | "Sleeps for 4 seconds" >> Sleep(seconds=4, message="Thinking...")
    | "Prints what they do" >> Lambda(lambda read, write: write(f"I see, you {read()}"))
    | "Acknowledges" >> Output(message="Cool")
    | "Multi-pipeline Router"
    >> Router(
        prompt="What would you like to buy?",
        routes={
            "Donut": (
                "Donut Pipeline" >> Pipeline()
                | "Greet user" >> Output("Great choice")
                | "Ask for quantity" >> Input("How many would you like?")
                | "Prints quantity"
                >> Lambda(lambda read, write: write(f"Here are {read()} donuts"))
                | "Peace out" >> Output("Peace out")
            ),
            "Bread": (
                "Bread Pipeline" >> Pipeline()
                | "Greet user" >> Output("Great choice")
                | "Ask for quantity" >> Input("How many would you like?")
                | "Prints quantity"
                >> Lambda(lambda read, write: write(f"Here are {read()} breads"))
                | "Peace out" >> Output("Peace out")
            ),
            "Sosa": (
                "Sosa Pipeline" >> Pipeline()
                | "Greet user" >> Output("Great choice")
                | "Ask for quantity" >> Input("How many would you like?")
                | "Prints quantity"
                >> Lambda(lambda read, write: write(f"Here are {read()} sosa"))
                | "Peace out" >> Output("Peace out")
            ),
        },
    )
    | "End" >> Output(message="Goodbye")
)

if __name__ == "__main__":
    graph.run(debug=True)
