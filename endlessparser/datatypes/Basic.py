from dataclasses import dataclass
from typing import List, Iterable, Type, TypeVar


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

    T = TypeVar("T", bound="Node")

    def _find_child_by_class(self, clazz: Type[T]) -> T:
        for child in self._find_children(clazz):
            return child

    def _find_children_by_class(self, clazz: Type[T]) -> Iterable[T]:
        for child in self.children:
            if child.__class__ == clazz:
                yield child

    def _get_tokens(self, child: "Node") -> str:
        if child and child.tokens and not len(child.tokens) == 0:
            return " ".join(child.tokens)

    def write(self) -> str:
        buffer = self.node_type
        if self.tokens and not len(self.tokens) == 0:
            buffer += " " + " ".join(self.tokens)

        for child in self.children:
            buffer += "\n" + _indent(child.write())

        return buffer


class HasName(Node):
    def name(self) -> str:
        return " ".join(self.tokens)


class HasSprite(Node):
    def sprite(self) -> str:
        return self._get_tokens(self._find_child("sprite"))
