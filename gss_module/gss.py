"""
Credits:
https://en.wikipedia.org/wiki/Unimodality
https://en.wikipedia.org/wiki/Golden-section_search
https://math.stackexchange.com/questions/80225/efficient-algorithm-to-find-maximum-of-a-unimodal-sequence
http://mathforcollege.com/nm/mws/gen/09opt/mws_gen_opt_txt_goldensearch.pdf
"""

from math import sqrt
import operator


class GoldenSectionSearch():
    """Golden-section search algorithm for unimodal sequences (with some
        first elements strictly monotonically decreasing (or increasing), and
        the remaining ones strictly monotonically increasing (or decreasing
        respectively).
    """

    def __init__(self):
        """Initialize Phi (inverse of the golden-section)"""
        self.phi = sqrt(5.0)/2.0 - 0.5

    def run(self, seq: list, minimum: bool = True):
        """Search for minimum or maximum
            :param seq: list containing a unimodal sequence
            :returns: the extremum of the unimodal sequence.
        """
        if minimum:
            # less-than operator (looking for the minimum)
            compare = operator.lt
        else:
            # greater-than operator (looking for the maximum)
            compare = operator.gt

        if len(seq) < 3:  # Mimimum length required for the sequence
            return None

        # Initial conditions.
        # x0 and x3: indexes for lower and upper bounds of the interval
        # x1 and x2: median points (having x1 < x2)
        x_0 = 0
        x_3 = len(seq) - 1
        dist = self.phi*(x_3 - x_0)
        x_1 = round(x_3 - dist)
        x_2 = round(x_0 + dist)

        # Iterative search
        while x_2 - x_1 > 0:
            # Comparison operator, can be operator.lt or operator.gt
            if compare(seq[x_1], seq[x_2]):
                x_3, x_2 = x_2, x_1
                x_1 = round(x_3 - self.phi*(x_3-x_0))
            else:
                x_0, x_1 = x_1, x_2
                x_2 = round(x_0 + self.phi*(x_3-x_0))

        # Finally we process the last few elements of the reduced sequence
        while x_3 - x_0 > 0:
            # Comparison operator, can be operator.lt or operator.gt
            if compare(seq[x_0], seq[x_3]):
                x_3 = x_3 - 1
            else:
                x_0 = x_0 + 1

        return seq[x_0]
