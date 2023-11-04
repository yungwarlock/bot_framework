from typing import List

from colorama import Fore, Style


class Pipeline:
    """Pipeline is a class that holds the nodes."""

    def __init__(self):
        self.documentation = None
        self.nodes: List[Node] = []

    def run(self, debug=False):
        """Runs the node."""

        if debug and self.documentation:
            print(Fore.YELLOW + "[" + self.documentation + "]" + Style.RESET_ALL)

        for node in self.nodes:
            if debug and node.documentation:
                print(Fore.YELLOW + "[" + node.documentation + "]" + Style.RESET_ALL, end=" ")

            node._invoke()

    def _add_node(self, node):
        """Adds a node to the pipeline."""

        self.nodes.append(node)
        return self

    def __rrshift__(self, other):
        """Adds documenation to the node."""

        self.documentation = other
        return self

    def __or__(self, other):
        """Adds a node to the pipeline."""

        return self._add_node(other)

class Node:
    """Base unit of conversation."""
    
    def __init__(self):
        self.documentation = None

    def __rrshift__(self, other):
        """Adds documenation to the node."""

        self.documentation = other
        return self


class Output(Node):
    """Output is a node that outputs a message."""

    def __init__(self, message: str):
        self.message = message
        super().__init__()

    def _invoke(self):
        """Outputs the message."""

        print(self.message)


class Input(Node):
    """Input is a node that takes an input from the user."""

    def __init__(self, prompt: str = None):
        self.prompt = prompt
        super().__init__()

    def _invoke(self):
        """Takes an input from the user."""

        user_input = input(f"{self.prompt}> ")
        print("User wrote:", user_input)
