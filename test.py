import main
import unittest



class Test(unittest.TestCase):

    def test_(self):
        self.assertEqual(main.word_chosongulize("моя"), "모야")
        self.assertEqual(main.word_chosongulize("ямм"), "얌")
        self.assertEqual(main.word_chosongulize("будет"), "부제뜨")
        self.assertEqual(main.word_chosongulize("ты"), "띄")
        self.assertEqual(main.word_chosongulize("да"), "다")
        self.assertEqual(main.word_chosongulize("любимая"), "류비마야")
        self.assertEqual(main.word_chosongulize("страны"), "쓰뜨라늬")
        self.assertEqual(main.word_chosongulize("мы"), "믜")
        self.assertEqual(main.word_chosongulize("друг"), "드루그")
        self.assertEqual(main.word_chosongulize("другу"), "드루구")
        self.assertEqual(main.word_chosongulize("нам"), "남")
        self.assertEqual(main.word_chosongulize("не"), "네", )
        self.assertEqual(main.word_chosongulize("тебе"), "쩨베")
        self.assertEqual(main.word_chosongulize("рука"), "루까")
        self.assertEqual(main.word_chosongulize("будем"), "부젬", )
        self.assertEqual(main.word_chosongulize("мир"), "미르", )
        self.assertEqual(main.word_chosongulize("путин"), "뿌찐", )
        self.assertEqual(main.word_chosongulize("земля"), "제믈랴", )

    def test_글(self):
        self.assertEqual(main.chosongulize(
            "славься славься ты русь моя"),
            "쓸라비쌰 쓸라비쌰 띄 루씨 모야", )
        self.assertEqual(main.chosongulize(
            "славься ты русская наша земля"),
            "쓸라비쌰 띄 루쓰까야 나샤 제믈랴", )
        self.assertEqual(main.chosongulize(
            "да будет во веки веков сильна"),
            "다 부제뜨 워 웨끼 웨꼬브 씰나", )
        self.assertEqual(main.chosongulize(
            "любимая наша страна"),
            "류비마야 나샤 쓰뜨라나", )



if __name__ == "__main__":
    unittest.main()
