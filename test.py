import main
import unittest

import unittest


class Test(unittest.TestCase):

    def test_(self):
        """test method
        """
        self.assertEqual("ㅁㅗㅑ", main.jamoize("моя"))
        self.assertEqual("ㅂㅜㅈㅔㄸㅡ", main.jamoize("будет"))



if __name__ == "__main__":
    unittest.main()
