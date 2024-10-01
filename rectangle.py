class Rectangle:
    def __init__(self, length: int, width: int) -> None:
        self.length = length
        self.width = width

    def __iter__(self):
        yield{'length ': self.length}
        yield{'width ': self.width}

# Example usage
rect = Rectangle(10, 5)

# Iterating over the rectangle
for dimension in rect:
    print(dimension)