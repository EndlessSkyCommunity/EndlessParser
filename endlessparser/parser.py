from typing import List, Tuple, Iterable

from endlessparser.datatypes import Node


def _indent_level(s: str) -> int:
    return len(s) - len(s.lstrip())


def _split_respect_quotes(s: str) -> Iterable[str]:
    quotes = ('"', "'", "`")
    active_quote = None
    buffer = ""

    for char in s:

        if not active_quote and char.isspace():
            if buffer == "":
                continue  # Ignore multiple spaces in a row
            yield buffer
            buffer = ""
            continue

        if char == active_quote:
            active_quote = None
        elif char in quotes:
            active_quote = char

        buffer += char

    yield buffer


def parse(text: str) -> List[Node]:
    lines = []
    for line in text.splitlines():
        lines.append((_indent_level(line), line.strip()))
    return _read_nodes(lines)


def _read_nodes(lines: List[Tuple[int, str]]) -> List[Node]:
    if len(lines) == 0:
        return []  # JIC

    nodes = []
    base_indent_level = lines[0][0]

    while len(lines) > 0:
        indent_level, line = lines[0]
        if len(line) == 0 or line.isspace() or line.startswith("#"):
            del lines[0]
            continue
        if indent_level == base_indent_level:
            slices = line.split(" ")
            node_type = slices[0]
            tokens = (
                [] if len(slices) == 1 else _split_respect_quotes(" ".join(slices[1:]))
            )  # prevent list index out of range errors
            nodes.append(Node(node_type, tokens, [],))
            # Remove processed lines, so we always know at which line are even when doing recursive calls
            del lines[0]
        elif indent_level > base_indent_level:
            #  Indented block - call the function again, it will read lines until it hits the next elif
            nodes[-1].children += _read_nodes(lines)
        elif indent_level < base_indent_level:
            # End of our indentation level - return to the caller
            break
    return nodes


s = """

"""
n = parse(s)
print(n)
