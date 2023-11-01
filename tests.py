from main import main
import unittest
from unittest.mock import patch

class MockPokemonTranslator:
    def translate(self, text, target_language="en"):
        return 'bulbasaure'


class MockPokemonService:
    def get_pokemon_info(self, pokemon_name):
        return {"abilities":[{"ability":{"name":"overgrow"}},
                             {"ability":{"name":"chlorophyll"}}],
                "height":7,
                "weight":90
                }
class TestPokemonMain(unittest.TestCase):
    @unittest.mock.patch('main.PokemonNameTranslator', MockPokemonTranslator)
    @unittest.mock.patch('main.PokemonService', MockPokemonService)

    def test_main(self):
        main()
        with open('report_template.html') as f:
            result = f.read()
            self.assertIn('bulbasaure', result)
            self.assertIn('overgrow', result)
            self.assertIn('chlorophyll', result)
            self.assertIn('7', result)
            self.assertIn('90', result)


