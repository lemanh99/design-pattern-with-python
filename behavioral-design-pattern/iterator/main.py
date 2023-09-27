"""
Source: https://refactoring.guru/design-patterns/iterator/python/example
"""
from collections.abc import Iterator, Iterable


class AlphabeticalIterator(Iterator):
    _position = None
    _reverse = False

    def __init__(self, collection, reverse=False):
        self._collection = collection
        self._position = -1 if reverse else 0
        self._reverse = reverse

    def __next__(self):
        try:
            value = self._collection[self._position]
            self._position += -1 if self._reverse else 1
        except IndexError:
            raise StopIteration()

        return value


class WordsCollection(Iterable):
    def __init__(self, collection=None):
        self._collection = collection or []

    def __iter__(self):
        return AlphabeticalIterator(self._collection)

    def get_reverse_iterator(self):
        return AlphabeticalIterator(self._collection, True)

    def add_item(self, item):
        self._collection.append(item)


if __name__ == "__main__":
    words_collection = WordsCollection()
    words_collection.add_item("First")
    words_collection.add_item("Second")
    words_collection.add_item("Third")

    print("Straight traversal:")
    print("\n".join(words_collection))
    print("")

    print("Reverse traversal:")
    print("\n".join(words_collection.get_reverse_iterator()), end="")
