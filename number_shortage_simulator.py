"""
https://github.com/RyanSkonnord/number-shortage-simulator

Inspired by https://xkcd.com/3009/
"""

# Copyright (c) 2024 Ryan Skonnord
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this
# software and associated documentation files (the "Software"), to deal in the Software
# without restriction, including without limitation the rights to use, copy, modify,
# merge, publish, distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to the following
# conditions:
#
# The above copyright notice and this permission notice shall be included in all copies
# or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
# INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
# PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF
# CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE
# OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


import string
from typing import Iterable, Mapping

SINGLE_DIGITS = frozenset(string.digits)


class OutOfNumbersError(Exception):
    """Indicate that a reserve cannot self-report due to insufficient numbers."""


class NumberReserve:
    """Stateful representation of a self-reporting reserve of numbers."""

    def __init__(self, quantities: Mapping[int, int]) -> None:
        self._quantities = {str(k): v for (k, v) in quantities.items()}
        if not all(k in SINGLE_DIGITS for k in self._quantities.keys()):
            raise ValueError

        self._digits_tracked = sorted(self._quantities.keys())

    def _spend(self, digit):
        self._quantities[digit] -= 1
        if self._quantities[digit] < 0:
            raise OutOfNumbersError

    def _report(self) -> str:
        """Report the reserve's state, deducting consumed digits."""

        tokens = []
        for digit in self._digits_tracked:
            quantity = self._quantities[digit]
            if quantity > 0:
                self._spend(digit)
                for qty_digit in str(quantity):
                    if qty_digit in self._quantities:
                        self._spend(qty_digit)
                suffix = "" if quantity == 1 else "s"
                tokens.append(f"{quantity} {digit}{suffix}")

        if len(tokens) <= 1:
            return "".join(tokens)
        tokens[-1] = "and " + tokens[-1]  # Avoid Princeton comma (xkcd.com/2995)
        return (" " if len(tokens) == 2 else ", ").join(tokens)

    def simulate_number_shortage(self) -> Iterable[str]:
        first = True
        while True:
            try:
                message = self._report()
            except OutOfNumbersError:
                return
            if not message:
                return

            if first:
                yield f"We have only {message} left."
                first = False
            else:
                yield f"No, wait, {message}."

    def print_nubmer_shortage(self) -> None:
        for line in self.simulate_number_shortage():
            print(line)


def demo():
    print("From https://www.xkcd.com/3009/:")
    NumberReserve({2: 15, 3: 12}).print_nubmer_shortage()

    print("\nStaring with 100 of each:")
    NumberReserve({int(d): 100 for d in SINGLE_DIGITS}).print_nubmer_shortage()


if __name__ == "__main__":
    demo()
