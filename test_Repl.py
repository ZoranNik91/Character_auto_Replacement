import unittest
import Replace_letters as rl

class TestPath1(unittest.TestCase):

    def test1_path(self):
        result = rl.Path1("D:\Torrents_Movies\Torrenti\Andor")
    def test2_path(self):
        result = rl.Path1("Andor")


if __name__ == '__main__':
    unittest.main()

# "D:\Torrents_Movies\Popcorn Time\zMovies\V for Vendetta (2006)"