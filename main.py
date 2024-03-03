import re

class Utilidades:

    def division(self, dividendo, divisor):
        # Verificar argumentos
        if not (isinstance(dividendo, (int)) and isinstance(divisor, (int))):
            raise ValueError("Ambos argumentos deben ser números")
        
        if divisor == 0:
            return 0
        
        return dividendo / divisor
    

    def extraerNumero(self, cadena):
        if not (isinstance(cadena, (str))):
            raise ValueError("No es una cadena de texto")
        numero_encontrado = re.search(r'\d+', cadena)
        if numero_encontrado:
            return int(numero_encontrado.group())
        else:
             return None
    