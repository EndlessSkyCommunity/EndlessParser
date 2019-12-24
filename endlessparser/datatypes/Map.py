from dataclasses import dataclass
from typing import Tuple

from endlessparser.datatypes import Node, NamedNode, SpriteNode


class PositionNode(Node):
    def position(self) -> Tuple[float, float]:
        pos = self._find_child("pos")
        if pos:
            return float(pos.tokens[0]), float(pos.tokens[1])


@dataclass
class GalaxyNode(NamedNode, SpriteNode, PositionNode):
    node_type = "galaxy"


@dataclass
class SystemNode(NamedNode, PositionNode):
    node_type = "system"
    # TODO


@dataclass
class PlanetNode(NamedNode):
    node_type = "planet"
    # TODO
