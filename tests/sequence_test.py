from sequence import Sequence, find_bounds
import unittest
from ball import Ball

d = {
    "R": "RED", "G": "GREEN", "B": "BLUE", "Y": "YELLOW", "RED": "R",
    "GREEN": "G", "BLUE": "B", "YELLOW": "Y"
}


def seq_maker(arr: str) -> Sequence:
    res = Sequence(None, [(0, 0), (1, 1)])
    for i in arr:
        res.push(Ball(None, 0, 0, d[i]))
    return res


def ball_maker(color: str) -> Ball:
    return Ball(None, 0, 0, d[color])


class TestFindBounds(unittest.TestCase):
    no_subsequence_case = {
        "seq": "GYRBG",
        "ans": [
            1, 1, 1, 1, 1
        ]
    }

    full_sequence_case = {
        "seq": "GGGGG",
        "ans": [
            5, 5, 5, 5, 5
        ]
    }

    midd_subsequence_case = {
        "seq": "GYYYG",
        "ans": [
            1, 3, 3, 3, 1
        ]
    }

    end_subsequence_case = {
        "seq": "GGYYY",
        "ans": [
            2, 2, 3, 3, 3
        ]
    }

    start_subsequence_case = {
        "seq": "YYYGG",
        "ans": [
            3, 3, 3, 2, 2
        ]
    }

    def comporator(self, target: dict):
        seq = seq_maker(target["seq"])
        seq.balls_arr = seq.balls_arr[1:]
        for i in range(4):
            l, r = find_bounds(seq.balls_arr, i)
            self.assertEqual(target["ans"][i], r - l + 1)

    def test_no_subsequence(self):
        self.comporator(self.no_subsequence_case)

    def test_full_sequence(self):
        self.comporator(self.full_sequence_case)

    def test_midd_subsequence(self):
        self.comporator(self.midd_subsequence_case)

    def test_end_subsequence(self):
        self.comporator(self.end_subsequence_case)

    def test_start_subsequence(self):
        self.comporator(self.start_subsequence_case)


class TestInsertSeq(unittest.TestCase):
    no_subsequence_case = {
        "seq": "GYRBG",
        "blt": "Y",
        "ans": [
            "YGYRBG", "GYYRBG", "GYYRBG", "GYRYBG", "GYRBYG"
        ]
    }

    full_sequence_case = {
        "seq": "GGGGG",
        "blt": "G",
        "ans": [
            "", "", "", "", ""
        ]
    }

    midd_subsequence_case = {
        "seq": "GYYYG",
        "blt": "Y",
        "ans": [
            "YGYYYG", "GG", "GG", "GG"
        ]
    }

    end_subsequence_case = {
        "seq": "GGYYY",
        "blt": "Y",
        "ans": [
            "YGGYYY", "GYGYYY", "GG", "GG", "GG"
        ]
    }

    start_subsequence_case = {
        "seq": "YYYGG",
        "blt": "Y",
        "ans": [
            "GG", "GG", "GG", "GG", "YYYGYG"
        ]
    }

    def comporator(self, target: dict):
        blt = ball_maker(target["blt"])

        for i in range(4):
            seq = seq_maker(target["seq"])
            seq.balls_arr = seq.balls_arr[1:]
            seq.insert(blt, i)
            self.assertEqual(target["ans"][i],
                             "".join([d[i.color] for i in seq.balls_arr]))

    def test_no_subsequence(self):
        self.comporator(self.no_subsequence_case)

    def test_full_sequence(self):
        self.comporator(self.full_sequence_case)

    def test_midd_subsequence(self):
        self.comporator(self.midd_subsequence_case)

    def test_end_subsequence(self):
        self.comporator(self.end_subsequence_case)

    def test_start_subsequence(self):
        self.comporator(self.start_subsequence_case)
