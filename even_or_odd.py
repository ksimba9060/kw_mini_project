import random


class even_or_odd:
    def __init__(self):
        self.money = 1000
        self.level = ""
        self.win_money = 500
        self.lose_money = 100

    def eoo_menu(self):
        print()
        print("=" * 20, "\n     홀짝 게임\n" + "=" * 20)
        print(f"\n당신은 지금 {self.money}원을 가지고 있습니다.")
        print("\n1: 난이도 하. 맞히면 +500, 틀리면 -100")
        print("2: 난이도 중. 맞히면 +500, 틀리면 -300")
        print("3: 난이도 상. 맞히면 +500, 틀리면 -500")

    def eoo_choose_level(self):
        while self.level not in ("1", "2", "3"):
            self.level = input("\n난이도 번호를 입력해주세요: ")

            if self.level not in ("1", "2", "3"):
                print("1, 2, 3 중 하나를 입력해주세요.")

        if self.level == "2":
            self.lose_money = 300
        elif self.level == "3":
            self.lose_money = 500

    def eoo_play(self):
        choice = input("\n홀은 1번, 짝은 2번을 입력하세요: ")

        if choice not in ("1", "2"):
            print("1 또는 2만 입력해주세요.")
            return

        number = random.randint(1, 100)
        result = "2" if number % 2 == 0 else "1"

        print("컴퓨터 숫자:", number)

        if choice == result:
            self.money += self.win_money
            print(f"정답! {self.win_money}원을 얻었습니다.")
        else:
            self.money -= self.lose_money
            print(f"틀렸습니다. {self.lose_money}원을 잃었습니다.")

        print("현재 잔액:", self.money, "원")

    def eoo_start(self):
        self.eoo_menu()
        self.eoo_choose_level()

        while self.money > 0:
            self.eoo_play()

            if self.money <= 0:
                break

            next_choice = input("\n1: 계속하기 / 0: 메뉴로 돌아가기: ")
            if next_choice == "0":
                print("\n홀짝 게임을 종료합니다.")
                return

        print("\n잔액이 0원이 되어 게임이 종료되었습니다.")


if __name__ == "__main__":
    game = even_or_odd()
    game.eoo_start()
