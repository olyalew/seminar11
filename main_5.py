from timeit import timeit
import numpy as np


def mean_by_gender(grades, genders):
    unique_genders = np.unique(genders)
    result = {}

    for gender in unique_genders:
        mask = genders == gender
        result[gender] = np.mean(grades[mask])

    return result

def test(grades, genders, outp):
    ret = mean_by_gender(np.array(grades), np.array(genders))
    assert np.isclose(ret['female'], outp['female'])
    assert np.isclose(ret['male'], outp['male'])

test([5, 4, 3, 5, 2], ["female", "male", "male", "female", "male"], {'male': 3.0, 'female': 5.0})
test([1, 0] * 10, ['female', 'male'] * 10, {'female': 1, 'male': 0})
test(range(100), ['female', 'male'] * 50, {'female': 49.0, 'male': 50.0})
test(list(range(100)) + [100], ['male'] * 100 + ['female'], {'male': 49.5, 'female': 100.0})

N = int(1E5)
grades = np.array([1.1] * N + [2.2] * N)
genders = np.array(['male'] * N + ['female'] * N)

benchmark = timeit("assert np.isclose(mean_by_gender(grades, genders)['male'], 1.1)",
                   "from __main__ import np, mean_by_gender, grades, genders",
                   number=1)

def benchmark_test(a, b):
    xx = 0
    yy = 0
    im = 0
    fi = 0
    for x, y in zip(a, b):
        if x != y:
            xx += x
            yy += x
            im += 1
            fi += 1

    return xx + yy

reference_benchmark = timeit("benchmark_test(grades, genders)",
                             "from __main__ import benchmark_test, grades, genders",
                             number=1)
assert reference_benchmark > benchmark * 10, "Код работает слишком медленно — вы точно использовали методы numpy?"

print("Время выполнения функции:", benchmark)
print("Время выполнения эталонной функции:", reference_benchmark)
