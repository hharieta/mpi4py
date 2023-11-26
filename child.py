#!/usr/bin/env python
from mpi4py import MPI
import numpy

# Obtiene información sobre el comunicador padre
comm = MPI.Comm.Get_parent()

# Obtiene el tamaño del proceso
size = comm.Get_size()
# Obtiene el rango del proceso
rank = comm.Get_rank()

N = numpy.array(0, dtype='int64')

# Recibe el valor de N transmitido por el script padre
comm.Bcast([N, MPI.INT], root=0)

# Calcula el valor de PI
#  con el método de Monte Carlo.
h = 1.0 / N; s = 0.0
for i in range(rank, N, size):
    print(rank, N, size, i)
    x = h * (i + 0.5)
    s += 4.0 / (1.0 + x**2)
    print(x, h, s)

# Reduce los valores de PI calculados por cada proceso
PI = numpy.array(s * h, dtype='float64')
comm.Reduce([PI, MPI.DOUBLE], None,
            op=MPI.SUM, root=0)

# Desconecta el comunicador
comm.Disconnect()