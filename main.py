from menu import Menu
from login import login

class Main :
    def __init__(self) :
        self.Log_in = login()
        self.menu = Menu()

    def main(self) : 

        print("안녕하세요! 인생은 한방! 도박 게임입니다.\n")

        bool_login = self.Log_in.login_menu()
        if (bool_login is True) :
            self.menu.menu()


play = Main()
play.main()