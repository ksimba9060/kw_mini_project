from daily_fortune import daily_fortune
from even_or_odd import even_or_odd
from roulette import Game_Roulette

class Menu :
    def __init__(self) :
        self.DailyFortune = daily_fortune()
        self.EvenOrOdd = even_or_odd()
        self.Roulette = Game_Roulette()

    def menu(self) :
        while True : 
            print("1. 과연 오늘 나의 운세는?\n2. 홀짝 나를 맞춰봐!\n3. 돌려 돌려 룰렛판~\n0.게임 종료하기\n")
            menu_choice = int(input("원하는 게임 종류를 선택해주세요. : ")) 

            if (menu_choice == 1) :
                self.DailyFortune.fortune()

            elif (menu_choice == 2) :
                self.EvenOrOdd.even_or_odd() # 함수 이름 다시 물어보기

            elif (menu_choice == 3) :
                self.Roulette.roulette() # 함수 이름 다시 물어보기

            elif (menu_choice == 0) :
                print("게임을 종료합니다.")
                return

            else :
                print("메뉴 입력을 올바르게 해주세요.\n")