from timeit import timeit
import numpy as np

def wipe_even(arr, target_value=0, in_place=False):
    if in_place:
        arr[arr % 2 == 0] = target_value
        return arr
    else:
        return np.where(arr % 2 == 0, target_value, arr)

def test(inp, outp, target=0, in_place=False):
    inp = np.array(inp)
    inp_backup = np.array(inp)

    q = wipe_even(inp, target, in_place)
    assert isinstance(q, np.ndarray), "Функция должна возвращать массив numpy (np.array)"
    assert np.array_equal(q, np.array(outp)), "Ошибка для входного списка " + str(np.array(inp))
    if in_place:
        assert np.array_equal(inp, np.array(outp)), "Функция должна менять исходный список"
    else:
        assert np.array_equal(inp, inp_backup), "Исходный список должен остаться неизменным"


test([1, 2, 3, 4, 5], [1, 0, 3, 0, 5], in_place=True)
test([], [], in_place=True)
test([1, 3, 5], [1, 3, 5], in_place=True)
test([5, 4, 3, 2, 0], [5, 0, 3, 0, 0], in_place=True)
test([100, 200, 300, 199, 299, 150], [0, 0, 0, 199, 299, 0], in_place=True)

test([1, 2, 3, 4, 5], [1, 99, 3, 99, 5], target=99, in_place=True)

N = 100000
benchmark = timeit("[0 if x*2 else x for x in np.array([1]*N)]",
                   "from __main__ import np, N", number=1)
print(benchmark)

otherbenchmark = timeit("wipe_even(np.array([1]*N), in_place=True)",
                        "from __main__ import np, N, wipe_even", number=1)
print(otherbenchmark)

assert benchmark > otherbenchmark * 1.5, "Код работает слишком медленно — вы точно не пользовались циклами?"
