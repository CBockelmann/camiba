# -*- coding: utf-8 -*-
"""provides the orthogonal matching pursuit to approximate a solution
    to the l_0-minimization problem."""

import numpy as np
import numpy.linalg as npl


def recover(
    mat_A,
    arr_b,
    num_k,
):
    """do the recovery for matrix mat_A, measurement
    arr_b for a given number of steps"""

    dt_type = np.promote_types(arr_b.dtype, mat_a.dtype)

    # generate array for reweighting the matrix A
    arr_d = np.empty(mat_A.shape[1], dtype=dt_type)
    for ii in range(0, mat_A.shape[1]):
        arr_d[ii] = np.sqrt(np.conj(mat_A[:, ii]).dot(mat_A[:, ii]))

    n = mat_A.shape[0]
    m = mat_A.shape[1]
    x = np.zeros(m, dtype=dt_type)
    S = np.zeros(m, dtype=dt_type)

    for i in range(0, num_k):

        # calc correlation
        r = np.abs(A.conj().T.dot((arr_b - mat_A.dot(x))))/arr_d

        # add maximal correlation to supprt
        S[np.argmax(r*(1-S))] += 1

        # generate matrices with columns restricted to support
        mat_A_S = mat_A[:, csg.aB(S)]
        mat_B_S = csg.H(mat_A_S)

        # solve approximation problem with
        # pseudo-inverse on current support
        x_S = npl.solve(mat_B_S.dot(mat_A_S), mat_B_S.dot(arr_b))

        x.fill(0)
        x[csg.aB(S)] = x_S

    # renormalize x before returning
    return x
