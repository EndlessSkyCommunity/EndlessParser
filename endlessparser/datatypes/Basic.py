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

    def _find_children(self, child_type: str) -> Optional[Iterable["Node"]]:
        for child in self.children:
            if child.node_type == child_type:
                yield child

    T = TypeVar("T", bound="Node")

    def _find_child_by_class(self, clazz: Type[T]) -> Optional[T]:
        for child in self._find_children_by_class(clazz):
            return child

    def _find_children_by_class(self, clazz: Type[T]) -> Optional[Iterable[T]]:
        for child in self.children:
            if child.__class__ == clazz:
                yield child

    def _get_tokens(self, child: "Node") -> Optional[str]:
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
    def name(self) -> Optional[str]:
        return self._get_tokens(self)


class HasSprite(Node):
    def sprite(self) -> Optional[str]:
        child = self._find_child("sprite")
        if child:
            return self._get_tokens(child)


class HasMusic(Node):
    def music(self) -> Optional[str]:
        child = self._find_child("music")
        if child:
            return self._get_tokens(child)
