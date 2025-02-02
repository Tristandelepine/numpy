from numpy.linalg._linalg import (
    matrix_power as matrix_power,
    solve as solve,
    tensorsolve as tensorsolve,
    tensorinv as tensorinv,
    inv as inv,
    cholesky as cholesky,
    outer as outer,
    eigvals as eigvals,
    eigvalsh as eigvalsh,
    pinv as pinv,
    slogdet as slogdet,
    det as det,
    svd as svd,
    svdvals as svdvals,
    eig as eig,
    eigh as eigh,
    lstsq as lstsq,
    norm as norm,
    qr as qr,
    cond as cond,
    matrix_rank as matrix_rank,
    multi_dot as multi_dot,
    trace as trace,
    diagonal as diagonal,
    cross as cross,
)

from numpy._pytesttester import PytestTester

__all__: list[str]
test: PytestTester

class LinAlgError(Exception): ...
