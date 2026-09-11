from daily_fortune import daily_fortune
from even_or_odd import even_or_odd
from player_wallet import PlayerWallet
from roulette import RouletteGame
from shop import Shop

class Menu :
    def __init__(self) :
        self.wallet = PlayerWallet()
        self.shop = Shop(self.wallet)
        self.DailyFortune = daily_fortune()
        self.games = {
            "1": ("과연 오늘 나의 운세는?", self.play_daily_fortune),
            "2": ("홀짝 나를 맞춰봐!", self.play_even_or_odd),
            "3": ("돌려 돌려 룰렛판~", self.play_roulette),
        }

    def menu(self) :
        while True : 
            print(f"[보유 코인: {self.wallet.coins}]")
            print("1. 게임 선택하기\n2. 내 지갑 보기\n3. 상점 가기\n0. 게임 종료하기\n")
            menu_choice = input("원하는 메뉴를 선택해주세요. : ").strip()

            if (menu_choice == "1") :
                self.select_game()

            elif (menu_choice == "2") :
                self.wallet.show_status()

            elif (menu_choice == "3") :
                self.shop.open()

            elif (menu_choice == "0") :
                print("게임을 종료합니다.")
                return

            else :
                print("메뉴 입력을 올바르게 해주세요.\n")

    def select_game(self):
        while True:
            print()
            print("========== 게임 선택 ==========")
            for key, (game_name, _) in self.games.items():
                print(f"{key}. {game_name}")
            print("0. 메인 메뉴로 돌아가기")
            print("=============================")

            game_choice = input("플레이할 게임을 선택해주세요. : ").strip()

            if game_choice == "0":
                print("메인 메뉴로 돌아갑니다.")
                return

            if game_choice not in self.games:
                print("게임 번호를 올바르게 입력해주세요.\n")
                continue

            _, play_game = self.games[game_choice]
            play_game()
            return

    def play_daily_fortune(self):
        grade = self.DailyFortune.fortune()
        self.reward_fortune(grade)

    def reward_fortune(self, grade):
        if grade is None:
            return

        rewards = {
            "JACKPOT": 3000,
            "좋음": 700,
            "나쁨": 100,
        }
        reward = rewards[grade]

        if self.wallet.use_item("fortune_bonus"):
            reward += 1000
            print("포춘 보너스권을 사용해 보상이 1000코인 증가했습니다.")

        self.wallet.earn(reward)

    def play_even_or_odd(self):
        game = even_or_odd()
        game.money = self.wallet.coins
        game.eoo_start()
        self.wallet.coins = game.money
        self.wallet.use_safety_ticket_if_needed()

    def play_roulette(self):
        game = RouletteGame()
        game.coin = self.wallet.coins

        if self.wallet.use_item("roulette_coupon"):
            game.coupon = 5
            print("룰렛 쿠폰팩을 사용해 쿠폰 5개를 충전했습니다.")

        game.play()
        self.wallet.coins = int(game.coin)
        self.wallet.use_safety_ticket_if_needed()
