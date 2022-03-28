import copy

def torres_hanoi_recur(A, B ,C, Check):
    if B == Check:
        return True


def torres_hanoi_torres(disks):
    amount = disks
    n = disks + 1
    A = []
    for i in range(0, amount):
        A.append(n - 1)
        n = n - 1

    B = []
    C = []
    Check = copy.deepcopy(A)
    torres_hanoi_recur(A, B, C, Check)
    return A, B, C


# User Input
torres_hanoi_torres(5)
