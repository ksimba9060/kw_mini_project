class PlayerWallet:
    def __init__(self, coins=10000):
        self.coins = coins
        self.items = {
            "fortune_bonus": 0,
            "roulette_coupon": 0,
            "safety_ticket": 0,
        }

    def show_status(self):
        print()
        print("========== 내 지갑 ==========")
        print(f"보유 코인: {self.coins}")
        print(f"포춘 보너스권: {self.items['fortune_bonus']}개")
        print(f"룰렛 쿠폰팩: {self.items['roulette_coupon']}개")
        print(f"긴급 지원권: {self.items['safety_ticket']}개")
        print("============================")
        print()

    def earn(self, amount):
        self.coins += amount
        print(f"{amount}코인을 획득했습니다. 현재 코인: {self.coins}")

    def spend(self, amount):
        if self.coins < amount:
            print("코인이 부족합니다.")
            return False

        self.coins -= amount
        print(f"{amount}코인을 사용했습니다. 현재 코인: {self.coins}")
        return True

    def add_item(self, item_name, count=1):
        self.items[item_name] += count

    def use_item(self, item_name, count=1):
        if self.items[item_name] < count:
            return False

        self.items[item_name] -= count
        return True

    def use_safety_ticket_if_needed(self):
        if self.coins > 0:
            return

        if self.use_item("safety_ticket"):
            self.coins = 1000
            print("긴급 지원권을 사용해 코인 1000개로 회복했습니다.")
