from django.test import TestCase

from aluraflix.models import Programa
from aluraflix.serializers import ProgramaSerializer


class ProgramaSerializerTestCase(TestCase):

    def setUp(self):
        self.programa = Programa(
            titulo='Test Serializer',
            data_lancamento='2021-01-01',
            tipo='F',
            likes=230,
            dislikes=100
        )
        self.serialize = ProgramaSerializer(instance=self.programa)

    def test_campos_serializer(self):
        """Verifica os campos serializados"""
        data = self.serialize.data
        self.assertEqual(set(data.keys()), set(['titulo', 'data_lancamento', 'tipo', 'likes']))

    def test_retorno_setializer(self):
        """Verifica os retornos do serialize"""
        data = self.serialize.data

        self.assertEqual(data['titulo'], self.programa.titulo)
        self.assertEqual(data['data_lancamento'], self.programa.data_lancamento)
        self.assertEqual(data['tipo'], self.programa.tipo)
        self.assertEqual(data['likes'], self.programa.likes)
