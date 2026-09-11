class login:
    def __init__(self):
        self.user_id = "admin"
        self.user_pw = "1234"

    def login_menu(self):
        for i in range(3):
            print("==========Login Menu==========")
            x = (input("ID 입력: "))
            y = (input("PASSWORD 입력: "))
            if x == self.user_id and y == self.user_pw:
                print("로그인 성공")
                return True
            else:
                print(f"입력 정보가 맞지 않습니다. {i+1}회 실패")
        print("로그인 시도 횟수를 초과하였습니다. 프로그램을 종료합니다.")
        return False

login = login()
login.login_menu()
