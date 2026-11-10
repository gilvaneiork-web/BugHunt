import unittest

from src.catalogo import buscar_por_categoria, listar_ativos


class TestCatalogo(unittest.TestCase):
    def test_listar_ativos_nao_retorna_inativos(self):
        resultado = listar_ativos()
        self.assertTrue(all(item["ativo"] for item in resultado))
        self.assertEqual(3, len(resultado))

    def test_buscar_categoria_administrativo(self):
        resultado = buscar_por_categoria("Administrativo")
        self.assertEqual(1, len(resultado))
        self.assertEqual("Atendimento", resultado[0]["nome"])


if __name__ == "__main__":
    unittest.main()
