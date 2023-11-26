#!/usr/bin/env python
from mpi4py import MPI
import numpy
import sys

#  inicia un nuevo conjunto de procesos MPI,
#  ejecutando el script cpi.py en cada uno de ellos.
#  maxprocs indica n procesos MPI para ejecutar el script.
comm = MPI.COMM_SELF.Spawn(sys.executable,
                           args=['child.py'],
                           maxprocs=6)

N = numpy.array(10, 'int64')

# envía el valor de N a todos los procesos MPI
# desde el proceso raíz (MPI.ROOT) 
# asegura que todos los procesos tengan 
# el mismo valor de N para su cálculo.
comm.Bcast([N, MPI.INT], root=MPI.ROOT)


PI = numpy.array(0.0, 'float64')

# reduce los valores de PI calculados por cada proceso
# en un solo valor, sumando los valores de PI
comm.Reduce(None, [PI, MPI.DOUBLE],
            op=MPI.SUM, root=MPI.ROOT)
print(PI)

# desconecta el comunicador
comm.Disconnect()