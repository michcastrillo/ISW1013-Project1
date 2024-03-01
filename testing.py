import unittest
from tested import Utilidades

class TestUtilidades(unittest.TestCase):

    def setUp(self):
        self.utilidades = Utilidades()

    def tearDown(self):
        pass

    def test_division_normal(self):
        # Prueba división normal
        resultado = self.utilidades.division(10, 2)
        self.assertEqual(resultado, 5, "La división de 10 por 2 debería ser 5")

    def test_division_por_cero(self):
        # Prueba división por cero
        with self.assertRaises(ValueError, msg="Falla en una division por cero"):
            self.utilidades.division(10, 0)

        with self.assertRaises(TypeError, msg="No se lanzó TypeError al ingresar texto como dividendo"):
            self.utilidades.division("texto", 5)

        with self.assertRaises(TypeError, msg="No se lanzó TypeError al ingresar texto como divisor"):
            self.utilidades.division(10, "texto")

        with self.assertRaises(TypeError, msg="No se lanzó TypeError al ingresar texto como dividendo y divisor"):
            self.utilidades.division("texto", "texto")

    def test_extraer_numero_encontrado(self):
        # Prueba extraer número de una cadena con número
        cadena = "La temperatura actual es 25 grados Celsius"
        numero = self.utilidades.extraerNumero(cadena)
        self.assertEqual(numero, 25, "El número extraído debería ser 25")

    def test_extraer_numero_no_encontrado(self):
        # Prueba extraer número de una cadena sin número
        with self.assertRaises(ValueError, msg="No se lanzó ValueError al no encontrar números"):
            self.utilidades.extraerNumero("No hay números aquí")

    def test_extraer_numero_cadena_vacia(self):
        # Prueba extraer número de una cadena vacía
        with self.assertRaises(ValueError, msg="No se lanzó ValueError al procesar una cadena vacía"):
            self.utilidades.extraerNumero("")

if __name__ == '__main__':
    unittest.main()
