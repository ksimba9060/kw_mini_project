class Shop:
    def __init__(self, wallet):
        self.wallet = wallet
        self.products = {
            "1": {
                "name": "포춘 보너스권",
                "price": 1200,
                "item": "fortune_bonus",
                "description": "다음 운세 보상을 1000코인 더 받습니다.",
            },
            "2": {
                "name": "룰렛 쿠폰팩",
                "price": 2000,
                "item": "roulette_coupon",
                "description": "룰렛 쿠폰 5개를 충전해 1회 무료 배팅합니다.",
            },
            "3": {
                "name": "긴급 지원권",
                "price": 3000,
                "item": "safety_ticket",
                "description": "코인이 0 이하가 되면 1000코인으로 회복합니다.",
            },
        }

    def open(self):
        while True:
            print()
            print("========== 상점 ==========")
            print(f"보유 코인: {self.wallet.coins}")
            for key, product in self.products.items():
                print(f"{key}. {product['name']} - {product['price']}코인")
                print(f"   {product['description']}")
            print("0. 나가기")
            print("========================")

            choice = input("구매할 상품 번호를 입력해주세요: ").strip()

            if choice == "0":
                print("상점을 나갑니다.")
                return

            if choice not in self.products:
                print("올바른 상품 번호를 입력해주세요.")
                continue

            product = self.products[choice]
            if self.wallet.spend(product["price"]):
                self.wallet.add_item(product["item"])
                print(f"{product['name']}을 구매했습니다.")
