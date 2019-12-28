from typing import Tuple, List, Dict, Iterable, Optional

from endlessparser.datatypes import Node, HasName, HasSprite, HasMusic


class HasPosition(Node):
    def position(self) -> Optional[Tuple[float, float]]:
        child = self._find_child("pos")
        if child and len(child.tokens) >= 2:
            return float(child.tokens[0]), float(child.tokens[1])


class HasObjects(Node):
    def objects(self) -> Iterable["ObjectNode"]:
        return self._find_children_by_class(ObjectNode)


class GalaxyNode(HasName, HasSprite, HasPosition):
    node_type = "galaxy"


class SystemNode(HasName, HasPosition, HasObjects, HasMusic):
    node_type = "system"

    def asteroids(self) -> Dict[str, Tuple[float, float]]:
        d = {}
        for child in self._find_children("asteroids"):
            if len(child.tokens) >= 3:
                d[child.tokens[0]] = (float(child.tokens[1]), float(child.tokens[2]))
        return d

    def belt(self) -> Optional[float]:
        child = self._find_child("belt")
        return float(child.tokens_as_string()) if child else None

    def fleets(self) -> Dict[str, float]:
        d = {}
        for child in self._find_children("fleet"):
            if len(child.tokens) >= 2:
                d[child.tokens[0]] = float(child.tokens[1])
        return d

    def government(self) -> Optional[str]:
        child = self._find_child("government")
        return child.tokens_as_string() if child else None

    def habitable(self) -> Optional[float]:
        child = self._find_child("habitable")
        return float(child.tokens_as_string()) if child else None

    def haze(self) -> Optional[str]:
        child = self._find_child("haze")
        return child.tokens_as_string() if child else None

    def links(self) -> List[str]:
        return [child.tokens_as_string() for child in self._find_children("link")]

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


class ObjectNode(HasName, HasSprite, HasObjects, Node):
    node_type = "object"

    def distance(self) -> Optional[float]:
        child = self._find_child("distance")
        return float(child.tokens_as_string()) if child else None

    def offset(self) -> Optional[float]:
        child = self._find_child("offset")
        return float(child.tokens_as_string()) if child else None

    def period(self) -> Optional[float]:
        child = self._find_child("period")
        return float(child.tokens_as_string()) if child else None


class PlanetNode(HasName, HasMusic):
    node_type = "planet"
    # TODO
