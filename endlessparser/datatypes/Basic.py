from dataclasses import dataclass
from typing import List, Iterable, Type, TypeVar, Optional, Callable, Any

from endlessparser.globals import QUOTES


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

    def _child_tokens_as_type(
        self, child_type: str, format_to: Callable = lambda x: str(x)
    ) -> Optional[Any]:
        child = self._find_child(child_type)
        if child:
            return format_to(child.tokens_as_string())

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
        return self._child_tokens_as_type("sprite")


class HasMusic(Node):
    def music(self) -> Optional[str]:
        return self._child_tokens_as_type("music")


class HasDescription(Node):
    def description(self) -> [str]:
        buffer = ""
        for child in self._find_children("description"):
            s = child.tokens_as_string()
            if s[0] in QUOTES:
                s = s.strip(s[0])
            buffer += s + "\n"
        return buffer.rstrip("\n")
