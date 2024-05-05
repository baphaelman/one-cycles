## FUNCTIONS ##
def factorial(n):
    if n == 0:
        return 1
    else:
        return int(n * factorial(n-1))

def combinations(n, k):
    return int(factorial(n) / (factorial(k) * factorial(n - k)))

## FIRST AWFUL CODE ##
def permutations(n):
    """Yields permutations of length n"""
    s = []
    def permutations_starting_with_s(n, s):
        if len(s) == n - 1:
            for i in range(1, n + 1):
                if i not in s:
                    s.append(i)
                    yield s
        else:
            for i in range(1, n + 1):
                if i not in s:
                    new_s = list(s)
                    new_s.append(i)
                    yield from permutations_starting_with_s(n, new_s)
    yield from permutations_starting_with_s(n, s)

def one_cycle_test(s):
    """Returns a list if it contains one cycle (or fewer)"""
    first = 1
    for i in s: # select the first element that isn't in its place
        if i != s[i - 1]:
            first = i
            break

    working_list = []
    while first not in working_list: # goes through cycle, adds elements hit to working_list
        working_list.append(first)
        first = s[first - 1]

    for i in s:
        if i not in working_list and i != s[i - 1]: # all elements not hit must be already in their positions
            return
    return s

def perms_that_work(n):
    """Returns the permutations length n that have one cycle (or cycle)"""
    working_list = []
    for perm in permutations(n):
        if one_cycle_test(perm):
            working_list.append(perm)
    return working_list

def number(n):
    """Counts with perms_that_work"""
    return len(perms_that_work(n))

def better_number(n):
    """Counts with perms_that_work, but slightly better"""
    count = 0
    for perm in permutations(n):
        if one_cycle_test(perm):
            count += 1
    return count


## FINAL COMPUTATIONAL FUNCTION ##
def one_cycles(n):
    """Uses math to count wayyy faster"""
    if n == 1:
        return 1
    count = 1 + factorial(n - 1)
    for i in range(2, n):
        count += combinations(n, i) * factorial(i - 1)
    return count

def prob(n):
    print(str(one_cycles(n) / factorial(n) * 100) + '%')

## COMPLICATED RUBIK'S FUNCTION, CONSIDERING FLIPPED EDGES ##
def hard_cycle(n):
    """Uses math to count one-cycles on a real rubik's cube"""
    if n == 1:
        return 1
    count = 1 + (factorial(n - 1) * 2 ** (n - 1))
    for i in range(2, n):
        count += combinations(n, i) * factorial(i - 1) * (2 ** (i - 1))
    return count

def hard_prob(n):
    print(str(hard_cycle(n) / (factorial(n) * 2 ** (n - 1)) * 100) + '%')