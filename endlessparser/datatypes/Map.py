from typing import Tuple, List, Dict, Iterable, Optional

from endlessparser.datatypes import (
    Node,
    HasName,
    HasSprite,
    HasMusic,
    HasDescription,
)

from endlessparser.globals import QUOTES


class HasPosition(Node):
    def position(self) -> Optional[Tuple[float, float]]:
        child = self._find_child("pos")
        if child and len(child.tokens) >= 2:
            return float(child.tokens[0]), float(child.tokens[1])


class HasObjects(Node):
    def objects(self) -> Iterable["ObjectNode"]:
        return self._find_children_by_class(ObjectNode)


class HasGovernment(Node):
    def government(self) -> Optional[str]:
        return self._child_tokens_as_type("government")


class GalaxyNode(HasName, HasSprite, HasPosition):
    node_type = "galaxy"


class SystemNode(HasName, HasPosition, HasObjects, HasMusic, HasGovernment):
    node_type = "system"

    def asteroids(self) -> Dict[str, Tuple[float, float]]:
        d = {}
        for child in self._find_children("asteroids"):
            if len(child.tokens) >= 3:
                d[child.tokens[0]] = (float(child.tokens[1]), float(child.tokens[2]))
        return d

    def belt(self) -> Optional[float]:
        return self._child_tokens_as_type("belt", lambda x: float(x))

    def fleets(self) -> Dict[str, float]:
        d = {}
        for child in self._find_children("fleet"):
            if len(child.tokens) >= 2:
                d[child.tokens[0]] = float(child.tokens[1])
        return d

    def habitable(self) -> Optional[float]:
        return self._child_tokens_as_type("habitable", lambda x: float(x))

    def haze(self) -> Optional[str]:
        return self._child_tokens_as_type("haze")

    def links(self) -> List[str]:
        return [child.tokens_as_string() for child in self._find_children("link")]

    def planets(self) -> List[str]:
        l = []
        for object in self.objects():
            if object.tokens: l.append(object.tokens_as_string())
            for o in object.objects(): #To include stations
                if o.tokens: l.append(o.tokens_as_string())
        return l
    
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
        return self._child_tokens_as_type("distance", lambda x: float(x))

    def offset(self) -> Optional[float]:
        return self._child_tokens_as_type("offset", lambda x: float(x))

    def period(self) -> Optional[float]:
        return self._child_tokens_as_type("period", lambda x: float(x))


class PlanetNode(HasName, HasMusic, HasDescription, HasGovernment):
    node_type = "planet"

    def attributes(self) -> Optional[List[str]]:
        child = self._find_child("attributes")
        return child.tokens if child else None

    def bribe(self) -> Optional[float]:
        return self._child_tokens_as_type("bribe", lambda x: float(x))

    def outfitters(self) -> List[str]:
        return [child.tokens_as_string() for child in self._find_children("outfitter")]

    def required_reputation(self) -> Optional[float]:
        return self._child_tokens_as_type("required reputation")

    def security(self) -> Optional[float]:
        return self._child_tokens_as_type("security", lambda x: float(x))

    def shipyards(self) -> List[str]:
        return [child.tokens_as_string() for child in self._find_children("shipyard")]

    def spaceport(self) -> str:
        buffer = ""
        for child in self._find_children("spaceport"):
            s = child.tokens_as_string()
            if s[0] in QUOTES:
                s = s.strip(s[0])
            buffer += s + "\n"
        return buffer.rstrip("\n")

    def tribute(self) -> Optional[float]:
        return self._child_tokens_as_type("tribute", lambda x: float(x))
