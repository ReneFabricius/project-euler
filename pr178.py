from dataclasses import dataclass


@dataclass
class Point:
    no_edge: int
    top: int
    bottom: int
    both: int


def pr178(cif_num):
    A = [[Point(0, 0, 0, 0) for n in range(10)] for k in range(cif_num)]
    A[0][9].top = 1
    for j in range(1, 9):
        A[0][j].no_edge = 1

    sum = 0
    for e in range(1, cif_num):
        for n in range(10):
            if n == 0:
                A[e][n].bottom = A[e - 1][n + 1].bottom + A[e - 1][n + 1].no_edge
                A[e][n].both = A[e - 1][n + 1].top + A[e - 1][n + 1].both

            elif n == 9:
                A[e][n].top = A[e - 1][n - 1].top + A[e - 1][n - 1].no_edge
                A[e][n].both = A[e - 1][n - 1].bottom + A[e - 1][n - 1].both

            else:
                A[e][n].no_edge = A[e - 1][n - 1].no_edge + A[e - 1][n + 1].no_edge
                A[e][n].top = A[e - 1][n - 1].top + A[e - 1][n + 1].top
                A[e][n].bottom = A[e - 1][n - 1].bottom + A[e - 1][n + 1].bottom
                A[e][n].both = A[e - 1][n - 1].both + A[e - 1][n + 1].both

            sum += A[e][n].both

    return sum