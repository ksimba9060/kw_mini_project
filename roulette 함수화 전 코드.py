import random
# 룰렛 / 시간 남으면 기록 보기
# 일단 로그인 하면 아이디: user_id, 패스워드:user_pw
# win = 0               # 승리 기록 기록 (보류)
# 쿠폰생성 => 5회 참여서 1회 무료 ? => count 세서 겜진입전에 판별해서 차감안되게하면 될거같긴한데

# 클래스 이름 => Game_Roulette
# 모은 코인 배팅할 수 있게 하고 랜덤으로 꽝/0.5배/1.5배/3배 이런식으로 보상 주기
# 0 꽝 / # 0.25배 / # 0.5배 / # 1.5배 / # 2배 / # 3배

coin = 10000            # 초기자산
bet_amount = 500   # 게임 실행 때 마다 필요한 금액 (차감 금액)
win_amount = 50000      # 승리 조건의 금액

bet_list = {
    1:0,
    2:0.25,
    3:0.5,
    4:0.8,
    5:1.5,
    6:2.0,
    7:2.5,
    8:3
}

while True:
    menu_roulette = input("1. 배팅하기 / 2. 게임종료")
    if menu_roulette == "1":
        # print("룰렛 게임을 시작하겠습니다!!")
        # print(bet_num)
        # print(bet_multiply)
        bet_num = random.randint(1,8)   # 금액 차등 지급
        bet_multiply = bet_list[bet_num]

        coin -= bet_amount
        coin = coin * bet_multiply

        print(f"배팅금으로 {bet_amount}만큼 차감됩니다.")
        print(f"보유중인 코인이 {bet_multiply}배로 변경됩니다.")
        print(f"보유중인 코인 : {coin}")

        if coin >= win_amount:
            print(f"{win_amount}에 도달하여 승리하셨습니다!!")
            break

    if coin < bet_amount:
        print("### GAME OVER ###")
        print("보유중인 코인이 게임 플레이에 필요한 금액보다 부족합니다.")
        break

    if menu_roulette == "2":
        print("게임을 종료합니다")
        break
    else:
        print("1~2 중에서 입력해주세요!!")
    