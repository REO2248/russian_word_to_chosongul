import main
import unittest



class Test(unittest.TestCase):

    def test_(self):
        """test method
        """
        self.assertEqual("ㅁㅗㅑ", main.jamoize("моя"))
        self.assertEqual("ㅂㅜㅈㅔㄸㅡ", main.jamoize("будет"))
        self.assertEqual("ㄸㅢ", main.jamoize("ты"))
        self.assertEqual("ㄷㅏ", main.jamoize("да"))
        self.assertEqual("ㄹㅠㅂㅣㅁㅏㅑ", main.jamoize("любимая"))



if __name__ == "__main__":
    unittest.main()
