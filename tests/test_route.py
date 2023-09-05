import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# Importamos nosso app
from app import app

# Importamos a biblioteca de testes
import unittest


class TestHomeView(unittest.TestCase):

    '''
      Como todos os 3 casos de teste fazem um get na home "/"
      da nossa aplicacao, definimos a funcao setUp. Ela e executada
      automaticamente sempre que o Pytest instancia a classe TestHomeView.
      A funcao setUp e semelhante a um metodo construtor.
    '''

    def setUp(self):
        ap = app.test_client()
        self.response = ap.get('/')
        self.response_P1 = ap.get('/projeto1')

    # Testamos se a resposta e 200 ("ok")
    def test_get(self):
        self.assertEqual(200, self.response.status_code)
        self.assertEqual(200, self.response_P1.status_code)

    # Testamos se o content_type da resposta da home esta correto
    def test_content_type(self):
        self.assertIn('text/html', self.response.content_type)
        self.assertIn('text/html', self.response_P1.content_type)