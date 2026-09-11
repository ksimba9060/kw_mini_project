import random

class daily_fortune():
    def __init__(self):
        self.fortune_results = {
            "1": {
                "JACKPOT": [
                    "뜻밖의 큰 행운이 찾아와요."
                ],
                "좋음": [
                    "생각지도 못한 작은 돈이 들어올 수 있어요.",
                    "오늘은 좋은 가격에 원하는 것을 만날 수 있어요.",
                    "작은 절약이 큰 행운으로 돌아와요."
                ],
                "나쁨": [
                    "오늘은 지갑을 꽉 닫아두는 게 좋겠어요."
                ]
            },

            "2": {
                "JACKPOT": [
                    "운명적인 인연이 찾아올지도 몰라요."
                ],
                "좋음": [
                    "오늘은 누군가에게 특별한 사람이 될 수 있어요.",
                    "기다리던 연락이 올지도 몰라요.",
                    "좋아하는 사람과 즐거운 시간을 보낼 수 있어요."
                ],
                "나쁨": [
                    "오늘은 괜히 오해가 생길 수 있으니 조심하세요."
                ]
            },

            "3": {
                "JACKPOT": [
                    "오늘 공부한 내용은 머릿속에 쏙쏙 들어와요."
                ],
                "좋음": [
                    "집중력이 올라가서 평소보다 공부가 잘돼요.",
                    "어려웠던 문제가 의외로 쉽게 풀릴 거예요.",
                    "오늘 시작한 공부가 좋은 결과로 이어질 수 있어요."
                ],
                "나쁨": [
                    "오늘은 공부하기는 글렀어요..."
                ]
            }
        }

    def fortune(self):
        print()
        print("=========================")
        print("     오늘의 포춘쿠키")
        print("=========================")
        print()

        print("오늘의 운세를 선택하세요.")
        print("1. 재물운")
        print("2. 연애운")
        print("3. 학업운")
        print()

        choice = input("운세 선택 : ")

        if choice not in self.fortune_results:
            print("잘못된 선택입니다.")
            return

        input("Enter를 눌러 포춘쿠키를 열어보세요!")

        grade = random.choices(
            ["JACKPOT", "좋음", "나쁨"],
            weights=[10, 70, 20]
        )[0]

        result = random.choice(
            self.fortune_results[choice][grade]
        )

        print()
        print("포춘 쿠키를 열었습니다.")
        print()
        print("등급 :", grade)
        print("결과 :", result)
        print()