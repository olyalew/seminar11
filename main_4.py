import numpy as np

def weighted_sum(weights, grades, normalize=False):
    if normalize:
        weights = weights.astype(float)
        weights /= np.sum(weights)
    return np.dot(weights, grades)

def test(w, g, out, normalize=False):
    q = weighted_sum(np.array(w), np.array(g), normalize)
    assert np.isclose(q, out)

test([0.3, 0.3, 0.4], [7, 9, 8], 8)
test([0.1, 0.2, 0.3, 0.4], [1, 5, 3, 2], 2.8)
test([1, 2, 3, 4], [1, 5, 3, 2], 28)
test([1, 2, 3, 4], [1, 5, 3, 2], 2.8, normalize=True)

N = 1000000

test([1, 2, 3, 4], [1, 5, 3, 2], 28)

from timeit import timeit

benchmark = timeit("sum([x/x for x in np.array([1]*N)])", "from __main__ import N, np", number=1)
otherbenchmark = timeit("weighted_sum(np.array([1.1]*N), np.array([1]*N), True)",
                        "from __main__ import N, weighted_sum, np", number=1)

print(benchmark/otherbenchmark)
assert benchmark > otherbenchmark * 1.7, "Код работает слишком медленно — вы точно использовали методы numpy?"
