from django.test import TestCase

from aluraflix.models import Programa


class ProgramaModelTestCase(TestCase):

    def setUp(self):
        self.programa = Programa(
            titulo='Procurando Falha',
            data_lancamento='2022-01-25'
        )

    def test_verifica_default(self):
        """Testa que verifica os atributos de um programa com valores default"""
        self.assertEqual(self.programa.titulo, 'Procurando Falha')
        self.assertEqual(self.programa.tipo, 'F')
        self.assertEqual(self.programa.data_lancamento, '2022-01-25')
        self.assertEqual(self.programa.likes, 0)
        self.assertEqual(self.programa.dislikes, 0)
