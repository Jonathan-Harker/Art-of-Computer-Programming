import uuid
from dataclasses import dataclass
from typing import List


@dataclass
class Relation:
    j: int
    k: int


@dataclass
class Pool:
    suc: int
    next: str


class TopologicalSort:
    def __init__(self, print_map: bool = False):
        self.count = {}
        self.top = {}
        self.pointer = ""
        self.front = 0
        self.storage_pool = {}
        self.print_map = print_map

    def sort(self, relations: List[Relation]) -> List[int]:
        items_to_output = []
        for r in relations:
            items_to_output.append(r.j)
            items_to_output.append(r.k)

        n = len(set(items_to_output))

        for relation in relations:
            self.count[relation.k] = 0
            self.top[relation.k] = "END"

        # T2
        for relation in relations:
            # T3
            self.count[relation.k] += 1
            pointer = str(uuid.uuid4())
            self.storage_pool[pointer] = (Pool(suc=relation.k, next=self.top.get(relation.j, "END")))
            self.top[relation.j] = pointer

        if self.print_map:
            self._memory_print_fig_8(n)

        # T4
        rear = 0
        q_link = {0: 0}

        for k in range(n, 0, -1):
            count_k = self.count.get(k, 0)
            if count_k == 0:
                q_link[rear] = k
                rear = k

        front = q_link[0]

        out = []
        while True:
            out.append(front)
            # T5
            if front == 0:
                # T8
                return out

            n -= 1
            pointer = self.top[front]

            # T6
            while pointer != "END":
                sp = self.storage_pool[pointer]
                successor = self.count[sp.suc]
                successor -= 1
                self.count[sp.suc] = successor
                if successor == 0:
                    q_link[rear] = sp.suc
                    rear = sp.suc

                pointer = sp.next

            # T7
            front = q_link.get(front, 0)

    def _memory_print_fig_8(self, n: int):
        print()
        for k in range(1, n + 1):
            print(k)
            print(self.count.get(k, 0))
            pointer = self.top[k]

            if pointer != "END":
                sp = self.storage_pool[pointer]
                suc = sp.suc
                print(suc)
                while sp.next != "END":
                    sp = self.storage_pool[sp.next]
                    print(sp.suc)

            print()


if __name__ == "__main__":
    sort = TopologicalSort()
    print(sort.sort(relations=[Relation(1, 3), Relation(2, 1)]))
