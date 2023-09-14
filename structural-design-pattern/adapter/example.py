import math


class RoundHole:
    """RoundHole is compatible with RoundPegs only."""

    def __init__(self, radius):
        self._radius = radius

    def get_radius(self):
        return self._radius

    def fits(self, peg):
        return self.get_radius() >= peg.get_radius()


class RoundPeg:
    """RoundPegs are compatible with RoundHoles."""

    def __init__(self, radius):
        self._radius = radius

    def get_radius(self):
        return self._radius


class SquarePeg:
    """SquarePegs are not compatible with RoundHoles."""

    def __init__(self, width):
        self._width = width

    def get_width(self):
        return self._width


class SquarePegAdapter(RoundPeg):
    """SquarePegAdapter allows fitting square pegs into round holes."""

    def __init__(self, peg):
        self._peg = peg

    def get_radius(self):
        return self._peg.get_width() * math.sqrt(2) / 2


if __name__ == "__main__":
    hole = RoundHole(5)
    rpeg = RoundPeg(5)
    print(hole.fits(rpeg))  # True

    small_sqpeg = SquarePeg(5)
    large_sqpeg = SquarePeg(10)
    # hole.fits(small_sqpeg)  # TypeError: 'SquarePeg' object cannot be interpreted as an integer

    small_sqpeg_adapter = SquarePegAdapter(small_sqpeg)
    large_sqpeg_adapter = SquarePegAdapter(large_sqpeg)
    print(hole.fits(small_sqpeg_adapter))  # True
    print(hole.fits(large_sqpeg_adapter))  # False
