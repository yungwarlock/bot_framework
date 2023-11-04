from queue import Queue
from typing import List, Dict, Callable

from colorama import Fore, Style


class Pipeline:
    """Pipeline is a class that holds the nodes."""

    def __init__(self):
        self.documentation = None
        self.nodes: List[Node] = []

        self._named_cache: Dict[str, Queue[str]] = {}

    def write(self, message: str):
        """A channel that which nodes can input to."""

        print(message)

    def read(self, prompt: str = None, key: str = "default"):
        """A channel that which nodes can output to."""

        if key not in self._named_cache:
            self._named_cache[key] = Queue()

        cache = self._named_cache[key]

        if not cache.empty():
            return cache.get()

        data = input(prompt)
        cache.put(data)

        return data

    def run(self, debug=False):
        """Runs the node."""

        if debug and self.documentation:
            print(Fore.YELLOW + "[" + self.documentation + "]" + Style.RESET_ALL)

        for node in self.nodes:
            if debug and node.documentation:
                print(Fore.YELLOW + "[" + node.documentation + "]" + Style.RESET_ALL, end=" ")

            node._invoke(self.read, self.write)


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

    def _invoke(self, _, write):
        """Outputs the message."""

        write(self.message)


class Input(Node):
    """Input is a node that takes an input from the user."""

    def __init__(self, prompt: str = None):
        self.prompt = prompt
        super().__init__()

    def _invoke(self, read, _):
        """Takes an input from the user."""

        user_input = read(f"{self.prompt}> ")

# Create a function type that takes two arguments: input and output and returns no value


class Lambda(Node):
    """Lambda is a node that executes a function with data from the previous node.
    
    The function takes two arguments: read which is the data from the previous node
    and write which is the data that will be passed to the next node.
    """

    def __init__(self, func: Callable[[str, str], None]):
        self.func = func
        super().__init__()

    def _invoke(self, read, write):
        """Executes the function."""

        self.func(read, write)