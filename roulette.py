import random

class RouletteGame:
    def __init__(self):
        self.coin = 10000
        self.bet_amount = 500
        self.win_amount = 50000
        self.coupon = 0  # 쿠폰 개수 초기화
        self.bet_list = {
            1: 0,
            2: 0.25,
            3: 0.5,
            4: 0.8,
            5: 1.5,
            6: 2.0,
            7: 2.5,
            8: 3
        }

    def check_game_over(self):
        """보유 코인이 최소 배팅금보다 부족한지 확인합니다."""
        # 쿠폰이 5개면 코인이 0원이어도 게임 오버가 되지 않도록 예외 처리
        if self.coupon >= 5:
            return False
            
        if self.coin < self.bet_amount:
            print("\n### GAME OVER ###")
            print("보유중인 코인이 게임 플레이에 필요한 금액보다 부족합니다.")
            return True
        return False

    def check_win(self):
        """목표 금액에 도달했는지 확인합니다."""
        if self.coin >= self.win_amount:
            print(f"\n축하합니다! {self.win_amount}에 도달하여 승리하셨습니다!!")
            return True
        return False

    def play(self):
        """게임 루프를 실행합니다."""
        while True:
            print(f"\n[현재 코인: {self.coin} | 현재 쿠폰: {self.coupon}/5]")
            menu_roulette = input("1. 배팅하기 / 2. 게임종료: ").strip()

            if menu_roulette == "1":
                # 쿠폰이 5개 이상이면 쿠폰 5개를 소모하고 배팅금 면제
                if self.coupon >= 5:
                    self.coupon -= 5
                    print("쿠폰 5개를 사용하여 이번 게임은 배팅금이 차감되지 않습니다!")
                else:
                    self.coin -= self.bet_amount
                    print(f"배팅금으로 {self.bet_amount}만큼 차감됩니다.")

                # 시도 완료 시 쿠폰 1개 적립
                self.coupon += 1

                # 룰렛 실행
                bet_num = random.randint(1, 8)
                bet_multiply = self.bet_list[bet_num]
                self.coin = self.coin * bet_multiply

                print(f"룰렛 결과 배율: {bet_multiply}배")
                print(f"보유중인 코인: {self.coin}")

                if self.check_win():
                    break
                if self.check_game_over():
                    break

            elif menu_roulette == "2":
                print("게임을 종료합니다.")
                break
            else:
                print("1~2 중에서 입력해주세요!!")

# 게임 실행
if __name__ == "__main__":
    game = RouletteGame()
    game.play()