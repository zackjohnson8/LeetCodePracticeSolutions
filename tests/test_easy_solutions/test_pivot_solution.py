import solutions.easy.pivot_solution as pivot_solution


def test_case_1():
    assert pivot_solution.solution([1, 7, 3, 6, 5, 6]) == 3


def test_case_2():
    assert pivot_solution.solution([1, 2, 3]) == -1


def test_case_3():
    assert pivot_solution.solution([2, 1, -1]) == 0
