from dataclasses import dataclass


@dataclass
class Card:
    color: str
    shape: str
    number: str
    shading: str

    def __str__(self):
        return 'Card({})'.format(' '.join(
            [self.number, self.color, self.shading, self.shape]))

    def encode_color(self):
        colors = ['Red', 'Purple', 'Green']
        return [1 if self.color == c else 0 for c in colors]

    def encode_shape(self):
        shapes = ['Oval', 'Squiggle', 'Diamond']
        return [1 if self.shape == s else 0 for s in shapes]

    def encode_number(self):
        numbers = ['1', '2', '3']
        return [1 if self.number == n else 0 for n in numbers]

    def encode_shading(self):
        shadings = ['Solid', 'Striped', 'Outlined']
        return [1 if self.shading == s else 0 for s in shadings]
