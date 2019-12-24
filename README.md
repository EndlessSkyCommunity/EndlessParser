# EndlessParser
A robust Parser for Endless Sky's data files

## Usage
````bash
$ pip install endlessparser
````

````python
>>> from endlessparser import parse
>>> with open("map.txt", "r") as f:
...     nodes = parse(f.read())
...
>>> nodes[0]
GalaxyNode(node_type='galaxy', tokens=['"Milky Way"'], children=[Node(node_type='pos', tokens=['0', '0'], children=[]), Node(node_type='sprite', tokens=['ui/galaxy'], children=[])])
>>> nodes[0].name()
'"Milky Way"'
>>> nodes[0].sprite()
'ui/galaxy'
>>> nodes[0].position()
(0.0, 0.0)
````

## Contributing
Requirements:
- Python >= 3.7 for syntactic sugar
- [black](https://github.com/psf/black) for formatting (please use it before commiting - it also integrates into most editors)
