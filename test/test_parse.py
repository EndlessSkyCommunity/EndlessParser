from unittest import TestCase

from endlessparser import parse


class Test(TestCase):
    def test__indent_level(self):
        cases = [
            (0, "asdf"),
            (1, " 1 spaces"),
            (2, "  2 spaces"),
            (3, "   3 spaces"),
            (4, "    4 spaces"),
            (1, "	1 tab"),
            (2, "		2 tabs"),
            (3, "			3 tabs"),
            (4, "				4 tabs"),
        ]
        for expected, s in cases:
            assert expected == parse._indent_level(s)

    def test__split_respect_quotes(self):
        cases = [
            (["galaxy", '"Milky Way"'], 'galaxy "Milky Way"'),
            (["galaxy", "'Milky Way'"], "galaxy 'Milky Way'"),
            (["galaxy", "`Milky Way`"], "galaxy `Milky Way`"),
            (["galaxy", "Milky", "Way"], "galaxy Milky Way"),
            (["fleet", '"Large Militia"', "18"], '		fleet "Large Militia" 18'),
            (
                ["description", '"This is wolfy\'s Place"'],
                'description "This is wolfy\'s Place"',
            ),
            (["planet", '"Ablub\'s Invention"'], 'planet "Ablub\'s Invention"'),
        ]
        for expected, s in cases:
            assert expected == list(parse._split_respect_quotes(s))
