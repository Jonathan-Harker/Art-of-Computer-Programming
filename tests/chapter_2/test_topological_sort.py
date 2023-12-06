import unittest
from typing import List

from exercises.chapter_2.linked_allocation.topological_sort import Relation, TopologicalSort


class TestPartialSorting(unittest.TestCase):
    def test_partial_sort_answers_question_17(self):
        sort = TopologicalSort()
        out = sort.sort(relations=self._build_input())

        self.assertEqual(out, [9, 1, 2, 3, 7, 4, 5, 8, 6, 0])

    def test_adding_extra_inputs_does_not_change_the_answer(self):
        example_input = self._build_input()
        example_input.append(Relation(9, 8))

        sort = TopologicalSort()
        out = sort.sort(relations=self._build_input())

        self.assertEqual(out, [9, 1, 2, 3, 7, 4, 5, 8, 6, 0])

    def _build_input(self):
        example_input: List[Relation] = [
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

        return example_input
