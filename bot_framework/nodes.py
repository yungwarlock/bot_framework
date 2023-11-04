from colorama import Fore, Style


class Node:
    """
    Base single unit of conversation.
    """
    
    def __init__(self):
        self.nodes = []
        self.documentation = None

    def invoke(self, debug=False, *args, **kwargs):
        """
        Invoke the node.
        """
        if debug and self.documentation:
            print(Fore.YELLOW + "[" + self.documentation + "]" + Style.RESET_ALL, end=" ")

        print(self.message)
        for node in self.nodes:
            node.invoke(debug=debug, *args, **kwargs)

    def _add_node(self, node):
        """
        Add a node to the current node.
        """
        self.nodes.append(node)
        return self

    def __rrshift__(self, other):
        """
        Adds documenation to the node.
        """
        self.documentation = other
        return self

    def __or__(self, other):
        """
        Add two nodes together.
        """
        return self._add_node(other)


class Output(Node):
    """
    Output is a node that outputs a message.
    """

    def __init__(self, message: str):
        self.message = message
        super().__init__()


class Input(Node):
    """
    Input is a node that takes an input from the user.
    """

    def __init__(self, prompt: str = None):
        self.prompt = prompt
        super().__init__()

    def invoke(self, debug=False, *args, **kwargs):
        """
        Invoke the node.
        """
        if debug and self.documentation:
            print(Fore.YELLOW + "[" + self.documentation + "]" + Style.RESET_ALL, end=" ")

        user_input = input(f"{self.prompt}> ")
        for node in self.nodes:
            node.invoke(user_input, *args, **kwargs)
