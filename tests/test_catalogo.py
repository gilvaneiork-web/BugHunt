import unittest

from src.catalogo import SERVICOS, buscar_por_categoria, listar_ativos


class TestCatalogo(unittest.TestCase):
    def test_listar_ativos_nao_retorna_inativos(self):
        resultado = listar_ativos()
        self.assertTrue(all(item["ativo"] for item in resultado))
        self.assertEqual(3, len(resultado))

    def test_buscar_categoria_administrativo(self):
        resultado = buscar_por_categoria("Administrativo")
        self.assertEqual(1, len(resultado))
        self.assertEqual("Atendimento", resultado[0]["nome"])

    def test_buscar_categoria_ambiental_exclui_inativos(self):
        # RN03: consultas por categoria retornam somente serviços ativos.
        resultado = buscar_por_categoria("Ambiental")
        self.assertEqual({1, 2}, {item["id"] for item in resultado})
        self.assertTrue(all(item["ativo"] for item in resultado))

    def test_inativo_permanece_cadastrado(self):
        # RN01/RN05: o inativo continua no catálogo, apenas fora das consultas.
        self.assertEqual(4, len(SERVICOS))
        self.assertIn(3, {item["id"] for item in SERVICOS})


if __name__ == "__main__":
    unittest.main()
