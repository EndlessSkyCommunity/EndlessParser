from dataclasses import dataclass
from typing import List, Iterable, Type, TypeVar, Optional


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

    def _find_child(self, child_type: str) -> Optional["Node"]:
        for child in self._find_children(child_type):
            return child

    def _find_children(self, child_type: str) -> Iterable["Node"]:
        for child in self.children:
            if child.node_type == child_type:
                yield child

    N = TypeVar("N", bound="Node")

    def _find_child_by_class(self, clazz: Type[N]) -> Optional[N]:
        for child in self._find_children_by_class(clazz):
            return child

    def _find_children_by_class(self, clazz: Type[N]) -> Iterable[N]:
        for child in self.children:
            if child.__class__ == clazz:
                yield child

    def tokens_as_string(self) -> Optional[str]:
        return " ".join(self.tokens) if self.tokens else ""

    def write(self) -> str:
        buffer = self.node_type
        if self.tokens and not len(self.tokens) == 0:
            buffer += " " + " ".join(self.tokens)

        for child in self.children:
            buffer += "\n" + _indent(child.write())

        return buffer


class HasName(Node):
    def name(self) -> str:
        return self.tokens_as_string()


class HasSprite(Node):
    def sprite(self) -> Optional[str]:
        child = self._find_child("sprite")
        return child.tokens_as_string() if child else None


class HasMusic(Node):
    def music(self) -> Optional[str]:
        child = self._find_child("music")
        return child.tokens_as_string() if child else None
