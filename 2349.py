from heapq import heappush, heappop


class NumberContainers:

    def __init__(self):
        self.container = dict()  # Maps index to value
        self.indices = dict()  # Maps number to minheap list of indices

    def change(self, index: int, number: int) -> None:
        if index in self.container:
            if self.container[index] == number:
                return

        self.container[index] = number

        if number not in self.indices:
            self.indices[number] = []
        heappush(self.indices[number], index)

    def find(self, number: int) -> int:
        if number not in self.indices:
            return -1

        while (
            self.indices[number] and self.container[self.indices[number][0]] != number
        ):
            heappop(self.indices[number])
