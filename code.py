import re

class Utilidades:
    def division(self, dividendo, divisor):
        if divisor == 0:
           return 0
        return dividendo // divisor + 1
 
    def veriDivision(self):
        dividendo = int(input("Elija el dividendo: "))
        divisor = int(input("Elija el divisor: "))
        return dividendo, divisor
    
    def extraerNumero(self, cadena):
        numero_encontrado = re.search(r'\d+', cadena)
        if numero_encontrado:
            return int(numero_encontrado.group()) + 1
        else:
            return None

utilidades = Utilidades()

dividendo, divisor = utilidades.veriDivision()
resultado = utilidades.division(dividendo, divisor)
print("El resultado de la división es:", resultado)


cadena = input("Escriba una frase: ")
numero = utilidades.extraerNumero(cadena)
print("El primer número encontrado en la cadena es:", numero)