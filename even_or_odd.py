import random


class even_or_odd:
    rankings = []

    def __init__(self):
        self.money = 10000
        self.nickname = ""
        self.level = ""
        self.win_money = 5000
        self.lose_money = 3000
        self.max_rounds = 10

    def eoo_menu(self):
        print()
        print("=" * 20, "\n     홀짝 게임\n" + "=" * 20)
        print(f"\n당신은 지금 {self.money}원을 가지고 있습니다.")
        print("\n1: 난이도 하. 맞히면 +5000, 틀리면 -3000")
        print("2: 난이도 중. 맞히면 +5000, 틀리면 -5000")
        print("3: 난이도 상. 맞히면 +5000, 틀리면 -7000")

    def choose_nickname(self):
        while not self.nickname:
            self.nickname = input("\n닉네임을 입력해주세요: ").strip()
            if not self.nickname:
                print("닉네임을 입력해주세요.")

    def eoo_choose_level(self):
        while self.level not in ("1", "2", "3"):
            self.level = input("\n난이도 번호를 입력해주세요: ")

            if self.level not in ("1", "2", "3"):
                print("1, 2, 3 중 하나를 입력해주세요.")

        if self.level == "2":
            self.lose_money = 5000
        elif self.level == "3":
            self.lose_money = 7000

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

    def save_ranking(self):
        self.rankings.append({
            "nickname": self.nickname,
            "level": self.level,
            "money": self.money,
        })
        self.rankings.sort(key=lambda ranking: ranking["money"], reverse=True)

    def show_ranking(self):
        print("\n========== 홀짝 게임 랭킹 ==========")
        if not self.rankings:
            print("아직 등록된 랭킹이 없습니다.")

        for rank, ranking in enumerate(self.rankings, start=1):
            print(
                f"{rank}. {ranking['nickname']} | "
                f"난이도 {ranking['level']} | "
                f"최종 잔액 {ranking['money']}원"
            )
        print("===================================")

    def eoo_lobby(self):
        while True:
            print("\n========== 홀짝 게임 ==========")
            print("1. 게임 시작")
            print("2. 랭킹 보기")
            print("0. 메뉴로 돌아가기")
            lobby_choice = input("원하는 메뉴를 선택해주세요: ").strip()

            if lobby_choice == "1":
                return True
            if lobby_choice == "2":
                self.show_ranking()
                continue
            if lobby_choice == "0":
                return False

            print("메뉴 입력을 올바르게 해주세요.")

    def eoo_start(self):
        if not self.eoo_lobby():
            return

        self.choose_nickname()
        self.eoo_menu()
        self.eoo_choose_level()

        while self.money > 0:
            for round_number in range(1, self.max_rounds + 1):
                print(f"\n---------- {round_number}/{self.max_rounds}회차 ----------")
                self.eoo_play()

                if self.money <= 0:
                    break

            if self.money <= 0:
                break

            print("\n축하합니다! 10회의 기회를 모두 사용하고 잔액을 남겼습니다.")
            next_choice = input("\n1: 계속하기 / 0: 메뉴로 돌아가기: ")
            if next_choice == "0":
                print("\n홀짝 게임을 종료합니다.")
                break

            print("\n게임을 다시 시작합니다.")

        if self.money <= 0:
            print("\n잔액이 0원이 되어 게임이 종료되었습니다.")

        self.save_ranking()
        self.show_ranking()


if __name__ == "__main__":
    game = even_or_odd()
    game.eoo_start()
