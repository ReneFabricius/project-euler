from math import prod
from copy import copy
import heapq


class SubsetIterator:
    def __init__(
        self, candidates: list[int], limit: int, set_size: int, combinator=prod
    ):
        """
        Generates all subsets of the size num_gen of the sorted list P_gen which combine by combinator at most to limit.

        Args:
            candidates (list[int]): A list of increasing integers.
            limit (int): Upper limit for combination value.
            set_size (int): Number of elements in the subset.
            combinator: A callable that takes a list of integers and returns an integer.
                Must be increasing in every list mamber. Defaults to prod.
        """
        self.candidates = candidates
        self.limit = limit
        self.set_size = set_size
        self.pick = list(range(set_size))
        self.combinator = combinator
        self.first = True

    def __iter__(self):
        return self

    def _pick_pick(self):
        return [self.candidates[i] for i in self.pick]

    def __next__(self):
        if self.first:
            self.first = False
            if self.combinator(self._pick_pick()) <= self.limit:
                return self._pick_pick()
            raise StopIteration

        ind_to_incr = len(self.pick) - 1
        while ind_to_incr >= 0:
            if self.pick[ind_to_incr] == len(self.candidates) - (
                self.set_size - ind_to_incr
            ):
                ind_to_incr -= 1
                continue

            cand_pick = copy(self.pick)
            cand_pick[ind_to_incr] += 1
            for i in range(ind_to_incr + 1, self.set_size):
                cand_pick[i] = cand_pick[i - 1] + 1

            if self.combinator([self.candidates[i] for i in cand_pick]) > self.limit:
                ind_to_incr -= 1
                continue

            self.pick = cand_pick
            break

        if ind_to_incr < 0:
            raise StopIteration

        return self._pick_pick()


class BoundedCustomSmoothIterator:
    def __init__(self, primes: list[int], limit: int):
        self.primes = primes
        self.limit = limit
        self.heap = [(1, 0)]

    def __iter__(self):
        return self

    def __next__(self):
        if not self.heap:
            raise StopIteration

        x, s_i = heapq.heappop(self.heap)

        for i in range(s_i, len(self.primes)):
            nx = x * self.primes[i]

            if nx > self.limit:
                break

            heapq.heappush(self.heap, (nx, i))

        return x
