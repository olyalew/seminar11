from timeit import timeit
import numpy as np

def calculate_tax(income):
    base_rate = 0.13
    higher_rate = 0.20
    threshold = 1000

    cumulative_income = np.cumsum(income)
    annual_tax = np.zeros_like(income, dtype=float)

    for i in range(len(income)):
        if cumulative_income[i] > threshold:
            annual_tax[i:] = (cumulative_income[i:] - cumulative_income[i]) * higher_rate
            break

    print("Income:", income)
    print("Cumulative Income:", cumulative_income)
    print("Annual Tax:", annual_tax)

    return np.sum(annual_tax)

test_cases = [
    (np.array([150]*12), 286.5),
    (np.array([100]*12), 163),
    (np.array([50]*12), 78),
    (np.array([1000]*12), 2260),
    (np.array(range(12))*100, 1215),
    (np.array(range(11,-1,-1))*100, 1243)
]

for income, expected_result in test_cases:
    result = calculate_tax(income)
    print(f"Income: {income}, Expected Result: {expected_result}, Actual Result: {result}")
    assert np.isclose(result, expected_result)

def dummy(x):
    z = 0
    for y in x:
        z += y
        z += y*0.12
        if z:
            z += y
    return z

print("Additional Test - Dummy Function:", dummy(np.array(range(12))*100))

N = int(1E6)
arr = np.array([1]*N)
benchmark = timeit("calculate_tax(arr)", "from __main__ import calculate_tax, arr", number=1)
reference_benchmark = timeit("dummy(arr)", "from __main__ import dummy, arr", number=1)

assert reference_benchmark > benchmark*5, "Код работает слишком медленно — вы точно использовали методы numpy?"

print("Время выполнения функции:", benchmark)
print("Время выполнения эталонной функции:", reference_benchmark)
