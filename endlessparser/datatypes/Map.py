from typing import Tuple, List, Dict, Iterable, Optional

from endlessparser.datatypes import Node, HasName, HasSprite, HasMusic


class HasPosition(Node):
    def position(self) -> Optional[Tuple[float, float]]:
        pos = self._find_child("pos")
        if pos:
            return float(pos.tokens[0]), float(pos.tokens[1])


class HasObjects(Node):
    def objects(self) -> Optional[Iterable["ObjectNode"]]:
        return self._find_children_by_class(ObjectNode)


class GalaxyNode(HasName, HasSprite, HasPosition):
    node_type = "galaxy"


class SystemNode(HasName, HasPosition, HasObjects, HasMusic):
    node_type = "system"

    def government(self) -> Optional[str]:
        return self._get_tokens(self._find_child("government"))

    def habitable(self) -> float:
        return float(self._get_tokens(self._find_child("habitable")))

    def belt(self) -> Optional[float]:
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
            if len(child.tokens) >= 3:
                d[child.tokens[0]] = (float(child.tokens[1]), float(child.tokens[2]))
        return d

    def trades(self) -> Dict[str, float]:
        d = {}
        for child in self._find_children("trade"):
            if len(child.tokens) >= 2:
                d[child.tokens[0]] = float(child.tokens[1])
        return d

    def fleets(self) -> Dict[str, float]:
        d = {}
        for child in self._find_children("fleet"):
            if len(child.tokens) >= 2:
                d[child.tokens[0]] = float(child.tokens[1])
        return d

    def haze(self):
        child = self._find_child("haze")
        if child:
            return self._get_tokens(child)


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


class PlanetNode(HasName, HasMusic):
    node_type = "planet"
    # TODO
