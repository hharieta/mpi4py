# Aproximación del número PI con el método de Montecarlo ⛰️

![círculo](assets/circulo_inscrito.jpeg)

## ⚜️ Teoría ⚜️

1. Considera un cuadrado de lado 2u, centrado en el origen (0,0). Este cuadrado tiene un área de 4u cuadradas.
2. Dentro de este cuadrado se haya inscrito un círculo de radio 1u, también centrado en el origen. El área de este círculo es π unidades cuadradas.
3. Genera puntos aleatorios uniformemente distribuidos dentro del cuadrado.
4. Cuenta cuántos de estos puntos están dentro del círculo inscrito.
5. La razón entre el número de puntos dentro del círculo y el total de puntos generados se aproxima a la razón entre el área del círculo y el área del cuadrado. $ Razón =  \frac{puntos dentro del círculo}{puntos totales}$
6. Multiplicando esta razón por 4, obtenemos una estimación de π. $ Razón \times 4 \approx PI $

## ⚜️ Aplicación con Interfaz de paso de mensajes (MPI) ⚜️

**MPI** es un estándar de comunicación utilizado en programación paralela para permitir que procesos en un clúster se comuniquen entre sí y coordinen su trabajo. MPI se utiliza comúnmente en aplicaciones de alto rendimiento y cómputo distribuido.

En Python 🐍 la biblioteca __mpi4py__ proporciona una interfaz para utilizar MPI en scripts Python


### 🧩 Características 

* **Comunicadores**: En MPI, los procesos se organizan en grupos llamados "comunicadores". Cada comunicador tiene un conjunto específico de procesos.
* **Envío/Recepción de Mensajes**: MPI permite que los procesos se comuniquen enviando y recibiendo mensajes entre sí. Los mensajes pueden contener datos, como matrices o valores escalares.
* **Operaciones Colectivas**: MPI admite operaciones colectivas que involucran a todos los procesos en un comunicador. Estas operaciones incluyen difusión `(Bcast)`, reducción `(Reduce)`, dispersión `(Scatter)`, recopilación `(Gather)`, entre otras.
* **Inicio/Fin MPI**: Se debe inicializar el entorno MPI y se debe finalizar al final del programa.
* **Proceso Raíz**: En operaciones colectivas como la reducción, hay un proceso que actúa como el "proceso raíz" que coordina la operación. En `mpi4py`, se puede especificar el proceso raíz mediante el parámetro root en las funciones colectivas.
* **Ejecución Paralela**: Cuando se ejecuta un programa MPI en un clúster o en una máquina con múltiples núcleos, cada proceso MPI se ejecuta de manera independiente en su propio espacio de memoria, y la comunicación entre procesos se realiza a través de MPI.

👨‍🏫 **Ejemplo:**

```python
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

data = 5
result = comm.reduce(data, op=MPI.SUM, root=0)

if rank == 0:
    print(f"La suma total es: {result}")

``````

para ejecutar el script 

```bash
mpirun --oversubscribe -n 6 python suma.py
```