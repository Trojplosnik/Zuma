from sequence import Sequence
import unittest
from ball import Ball

d = {
    "R": "RED", "G": "GREEN", "B": "BLUE", "Y": "YELLOW"
}

d1 = {
    "RED": "R", "GREEN": "G", "BLUE": "B", "YELLOW": "Y"
}

def seq_maker(arr: str) -> Sequence:
    res = Sequence(None, [(0, 0), (1, 1)])
    for i in arr:
        res.push(Ball(None, 0, 0, d[i]))
    return res


def ball_maker(color: str) -> Ball:
    return Ball(None, 0, 0, d[color])

class TestSuggest(unittest.TestCase):
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
            "YGGYYY", "GYGYYY", "", "", ""
        ]
    }

    start_subsequence_case = {
        "seq": "YYYGG",
        "blt": "Y",
        "ans": [
            "", "", "", "", "YYYGYG"
        ]
    }

    def setUp(self) -> None:
        pass

    def test_no_subsequence(self):
        blt = ball_maker(self.no_subsequence_case["blt"])

        for i in range(4):
            seq = seq_maker(self.no_subsequence_case["seq"])
            seq.balls_arr = seq.balls_arr[1:]
            seq.insert(blt, i)
            self.assertEqual(self.no_subsequence_case["ans"][i], "".join([d1[i.color] for i in seq.balls_arr]))
