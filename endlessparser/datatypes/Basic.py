from dataclasses import dataclass
from typing import List, Iterable


def _indent(s: str) -> str:
    buffer = ""
    for line in s.splitlines():
        buffer += "\t%s\n" % line
    return buffer.rstrip()


@dataclass
class Node:
    node_type: str
    tokens: List[str]
    children: List["Node"]

    def _find_child(self, child_type: str) -> "Node":
        for child in self._find_children(child_type):
            return child

    def _find_children(self, child_type: str) -> Iterable["Node"]:
        for child in self.children:
            if child.node_type == child_type:
                yield child

    def write(self) -> str:
        buffer = self.node_type
        if self.tokens and not len(self.tokens) == 0:
            buffer += " " + " ".join(self.tokens)

        for child in self.children:
            buffer += "\n" + _indent(child.write())

        return buffer


class NamedNode(Node):
    def name(self) -> str:
        return " ".join(self.tokens)


class SpriteNode(Node):
    def sprite(self) -> str:
        child = self._find_child("sprite")
        if child:
            return " ".join(child.tokens)
