import main
import unittest



class Test(unittest.TestCase):

    def test_(self):
        """test method
        """
        self.assertEqual("모야", main.chosongulize("моя"))
        self.assertEqual("얌", main.chosongulize("ямм"))
        self.assertEqual("부제뜨", main.chosongulize("будет"))
        self.assertEqual("띄", main.chosongulize("ты"))
        self.assertEqual("다", main.chosongulize("да"))
        self.assertEqual("류비마야", main.chosongulize("любимая"))



if __name__ == "__main__":
    unittest.main()
