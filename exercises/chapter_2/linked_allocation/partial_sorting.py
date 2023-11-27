import uuid
from dataclasses import dataclass
from typing import List


@dataclass
class K:
    count: int
    top: str


@dataclass
class P:
    value: int
    next: str


@dataclass
class Relation:
    j: int
    k: int


relations: List[Relation] = [
    Relation(9, 2),
    Relation(3, 7),
    Relation(7, 5),
    Relation(5, 8),
    Relation(8, 6),
    Relation(4, 6),
    Relation(1, 3),
    Relation(7, 4),
    Relation(9, 5),
    Relation(2, 8),
]

# T1
n = len(relations)

ks = []
successors = {}

for relation in relations:
    ks.append(K(count=0, top=str(uuid.uuid4())))

# T2
for relation in relations:
    # T3
    ks[relation.k].count += 1
    p_location = str(uuid.uuid4())
    successors[p_location] = P(value=relation.k, next=ks[relation.j].top)
    ks[relation.j].top = p_location

# Display Linked List
for k in ks:
    print()
    print(k.count)

    if not successors.get(k.top):
        continue

    successor = successors.get(k.top)
    print(successor.value)

    while successors.get(successor.next):
        successor = successors.get(successor.next)
        print(successor.value)
