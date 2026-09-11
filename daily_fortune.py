import random

class daily_fortune():
    def __init__(self):
        self.fortune_results = [
            "행운이 너무 커서 쿠키가 감당을 못 했어요!",
            "좋은 일이 살짝 찾아와요",
            "작은 행복이 찾아와요",
            "오늘은 무난무난한 하루예요",
            "앗, 행운이 잠깐 외출 중이에요",
            "오늘의 행운은 품절이에요",
            "행운이 몰래 따라다녀요",
            "오늘은 왠지 잘 풀릴 것 같아요",
            "앗… 쿠키가 빈말을 못 하는 타입이네요",
            "쿠키를 열었는데 감자만 나왔어요",
        ]
        
    def fortune(self):
        print()
        print("=========================")
        print("     오늘의 포춘쿠키")
        print("=========================")
        print()
        input("Enter를 눌러 포춘쿠키를 열어보세요!")

        result = random.choice(self.fortune_results)

        print()
        print("포춘 쿠키를 열었습니다!")
        print()
        print(result)
        print()
