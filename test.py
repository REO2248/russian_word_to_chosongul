import main
import unittest



class Test(unittest.TestCase):

    def test_(self):
        """test method
        """
        self.assertEqual(main.chosongulize("моя"), "모야")
        self.assertEqual(main.chosongulize("ямм"), "얌")
        self.assertEqual(main.chosongulize("будет"), "부제뜨")
        self.assertEqual(main.chosongulize("ты"), "띄")
        self.assertEqual(main.chosongulize("да"), "다")
        self.assertEqual(main.chosongulize("любимая"), "류비마야")
        self.assertEqual(main.chosongulize("страны"), "쓰뜨라늬")
        self.assertEqual(main.chosongulize("мы"), "믜")
        self.assertEqual(main.chosongulize("друг"), "드루그")
        self.assertEqual(main.chosongulize("другу"), "드루구")
        self.assertEqual(main.chosongulize("нам"), "남")
        self.assertEqual(main.chosongulize("не"), "네", )
        self.assertEqual(main.chosongulize("тебе"), "쩨베")
        self.assertEqual(main.chosongulize("рука"), "루까")
        self.assertEqual(main.chosongulize("будем"), "부젬", )
        self.assertEqual(main.chosongulize("мир"), "미르", )
        self.assertEqual(main.chosongulize("путин"), "뿌찐", )
        self.assertEqual(main.chosongulize("земля"), "제믈랴", )
        self.assertEqual(main.chosongulize("не"), "네", )
        self.assertEqual(main.chosongulize("не"), "네", )
        self.assertEqual(main.chosongulize("не"), "네", )
        self.assertEqual(main.chosongulize("не"), "네", )
        self.assertEqual(main.chosongulize("не"), "네", )
        self.assertEqual(main.chosongulize("не"), "네", )
        self.assertEqual(main.chosongulize("не"), "네", )
        self.assertEqual(main.chosongulize("не"), "네", )
        self.assertEqual(main.chosongulize("не"), "네", )
        self.assertEqual(main.chosongulize("не"), "네", )



if __name__ == "__main__":
    unittest.main()
