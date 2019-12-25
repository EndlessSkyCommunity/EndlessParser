from dataclasses import dataclass
from typing import Tuple, List, Dict, Iterable

from endlessparser.datatypes import Node, HasName, HasSprite


class HasPosition(Node):
    def position(self) -> Tuple[float, float]:
        pos = self._find_child("pos")
        if pos:
            return float(pos.tokens[0]), float(pos.tokens[1])


class HasObjects(Node):
    def objects(self) -> Iterable["ObjectNode"]:
        return self._find_children_by_class(ObjectNode)


class GalaxyNode(HasName, HasSprite, HasPosition):
    node_type = "galaxy"


class SystemNode(HasName, HasPosition, HasObjects):
    node_type = "system"

    def government(self) -> str:
        return self._get_tokens(self._find_child("government"))

    def habitable(self) -> float:
        return float(self._get_tokens(self._find_child("habitable")))

    def belt(self) -> float:
        return float(self._get_tokens(self._find_child("belt")))

    def links(self) -> List[str]:
        return [self._get_tokens(n) for n in self._find_children("link")]

    def asteroids(self) -> Dict[str, Tuple[float, float]]:
        d = {}
        for child in self._find_children("asteroids"):
            d[child.tokens[0]] = (float(child.tokens[1]), float(child.tokens[2]))
        return d

    def minables(self) -> Dict[str, Tuple[float, float]]:
        d = {}
        for child in self._find_children("minables"):
            d[child.tokens[0]] = (float(child.tokens[1]), float(child.tokens[2]))
        return d

    def trades(self) -> Dict[str, float]:
        d = {}
        for child in self._find_children("trade"):
            d[child.tokens[0]] = float(child.tokens[1])
        return d

    def fleets(self) -> Dict[str, float]:
        d = {}
        for child in self._find_children("fleet"):
            d[child.tokens[0]] = float(child.tokens[1])
        return d


class ObjectNode(HasName, HasSprite, HasObjects, Node):
    node_type = "object"

    def distance(self) -> float:
        child = self._find_child("distance")
        if child:
            return float(self._get_tokens(child))

    def period(self) -> float:
        child = self._find_child("period")
        if child:
            return float(self._get_tokens(child))


class PlanetNode(HasName):
    node_type = "planet"
    # TODO
