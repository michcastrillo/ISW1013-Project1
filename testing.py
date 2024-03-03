import unittest
from main import Utilidades

class TestUtilidades(unittest.TestCase):

    def setUp(self):
        self.utilidades = Utilidades()

    def tearDown(self):
        pass
    #Pruebas unitarias
    # 1. Prueba división normal de el resultado correcto. 
    def test_division_normal(self):
        # Prueba división normal
        resultado = self.utilidades.division(150, 4)
        self.assertEqual(resultado, 37.5)

     # 2. Prueba division por 0. 
    def test_division_por_cero(self):
        resultado = self.utilidades.division(10, 0)
        self.assertEqual(resultado, 0)

    # 3. Prueba de argumentos correctos
    def test_argumentos_no_numericos(self):
        with self.assertRaises(ValueError):
            self.utilidades.division("abc", 2)

        # Verifica que la función maneje adecuadamente un divisor no numérico
        with self.assertRaises(ValueError):
            self.utilidades.division(10, "xyz")

        # Verifica que la función maneje adecuadamente ambos argumentos no numéricos
        with self.assertRaises(ValueError):
            self.utilidades.division("abc", "xyz")

    #  # 4. Prueba número de cadena de texto
    def test_extraer_numero_encontrado(self):
        cadena = "La temperatura actua1 es 25 grados Celsius"
        numero = self.utilidades.extraerNumero(cadena)
        self.assertEqual(numero, 1)

    # #Modificacion de parametros para que falle.
    def test_division_normal_fallo(self):
        # Prueba división normal
        resultado = self.utilidades.division(150, 4)
        self.assertEqual(resultado, 40.5, "La división de 150 por 4 debería ser 40.5")

    def test_division_por_cero_fallo(self):
        resultado = self.utilidades.division(10, 0)
        self.assertEqual(resultado, 1, "La división de 10 por 0 debería ser 1")

    def test_extraer_numero_encontrado_fallo(self):
        cadena = "La temperatura actua1 es 25 grados Celsius"
        numero = self.utilidades.extraerNumero(cadena)
        self.assertEqual(numero, 25, f"El primer número extraido de la cadena: [{cadena}] es 25")

if __name__ == '__main__':
    unittest.main()
