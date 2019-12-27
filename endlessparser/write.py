from typing import List

from endlessparser import Node


def write(nodes: List[Node]) -> str:
    buffer = ""
    for node in nodes:
        buffer += node.write() + "\n\n"
    return buffer
