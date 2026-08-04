# Operaciones Discretas (Factorial, Fibonacci, Mínimo Común Múltiplo, Máximo Común Divisor) - Andrés León [Alvaro Orjuela (Factorial)]

from nucleo.operacion import Operacion
from excepciones.error_calculadora import ErrorFactorialNegativo , ErrorFibonacciNegativo

class Factorial(Operacion):
    etiqueta = 'Factorial'

    def __init__(self, numero_a):
        self._numero_a = numero_a

    def ejecutar(self):
        if self._numero_a < 0:
            raise ErrorFactorialNegativo
        if self._numero_a == 0 or self._numero_a == 1:
            return 1
        return self._numero_a * Factorial(self._numero_a-1)
    

class MCM(Operacion):
    etiqueta = "Minimo Comun Multiplo"

    def __int__(self, numero_a, numero_b):
        self._numero_a= numero_a
        self._numero_b= numero_b

    def ejecutar(self): 

        while self._numero_b !=0: 
            self._numero_a , self._numero_b = self._numero_b, self._numero_a % self._numero_b
            return self._numero_a



class MCD(Operacion):
    etiqueta = "Maximo comun divisor"

    def __int__(self, numero_a, numero_b):
        self._numero_a= numero_a
        self._numero_b= numero_b

    def ejecutar(self): 
        for i in range (min(self._numero_a , self._numero_b), 0,-1):
            if self._numero_a % i == 0 and self._numero_b % i ==0:
                return i

            

class Fibonacci(Operacion):
    etiqueta = "Fibonacci"

    def __init__(self, numero):
        self._numero = numero

    def ejecutar(self):
        n = self._numero

        if n<0: 
            raise ErrorFibonacciNegativo

        elif n==0:
            return 0

        elif n==1: 
            return 1

        a,b = 0,1

        for i in range(1,n):
            a,b = b, a+b
            return b
