from math_series.series import fibonacci, lucas, sum_series


def test_fibonacci_0():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected


def test_fibonacci_1():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected


def test_fibonacci_5():
    actual = fibonacci(5)
    expected = 5
    assert actual == expected


def test_lucas_0():
    actual = lucas(0)
    expected = 2
    assert actual == expected

def test_lucas_1():
    actual = lucas(1)
    expected = 1
    assert actual == expected

def test_lucas_5():
    actual = lucas(5)
    expected = 11
    assert actual == expected

def test_sum_series_as_fibo_5():
    actual = sum_series(5)
    expected = 5
    assert actual == expected


def test_sum_series_as_fibo_7():
    actual = sum_series(7)
    expected = 13
    assert actual == expected

# option1 at index 0  will be 2 and option 2 at index 1 will be 1 and need the 7th element value 
def test_sum_series_as_lucas_5():
    actual = sum_series(5,2,1)
    expected = 11
    assert actual == expected
# option1 at index 0  will be 5 and option 2 at index 1 will be 7 and need the 7th element value 
def test_sum_series_as_lucas_7():
    actual = sum_series(7,5, 7)
    expected = 131
    assert actual == expected

