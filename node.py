class HuffmanNode:
    def __init__(self, frequency=0, character=b'a', left=None, right=None):
        pass
        self.frequency = frequency
        self.character = character
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.frequency < other.frequency


class DecodeNode:
    def __init__(self, character=None, left=None, right=None, code=""):
        self.character = character
        self.left = left
        self.right = right
        self.code = code