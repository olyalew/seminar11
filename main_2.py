import numpy as np

def select_even(arr):
    return arr[arr % 2 == 0]

def testme(f, inp, outp):
    q = f(np.array(inp))
    assert isinstance(q, np.ndarray), "Функция должна возвращать массив numpy (np.array)"
    assert np.array_equal(q, np.array(outp)), "Ошибка для входного списка " + str(np.array(inp))

def test(inp, outp):
    testme(select_even, inp, outp)

test([1, 2, 3, 4, 5], [2, 4])
test([], [])
test([1, 3, 5], [])
test([5, 4, 3, 2, 0], [4, 2, 0])
test([100, 200, 300, 199, 299, 150], [100, 200, 300, 150])

from timeit import timeit

N = 100000
benchmark = timeit("[x for x in np.array([1]*N) if x*2]", "from __main__ import N, np", number=1)
otherbenchmark = timeit("select_even(np.array([1]*N))",
                        "from __main__ import N, select_even, np", number=1)

print(benchmark, otherbenchmark)
assert benchmark > otherbenchmark * 2, "Код работает слишком медленно — вы точно не пользовались циклами?"
