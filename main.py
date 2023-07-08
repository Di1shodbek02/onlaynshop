from tabulate import tabulate
from model import User
from model import Company
from model import Car


class Basic:
    def __init__(self, session):
        self.session_user = session

    def settings(self):
        menu = """
        1) change info
        2) delete account
        3) <- back
        """
        key = int(input(menu))
        match key:
            case 1:
                menu_col = """
                    1) name
                    2) username
                    3) password
                    4) <- back
                        >>>"""
                key = int(input(menu_col))
                if key != 4:
                    new_val = input("New value: ")
                match key:
                    case 1:
                        self.session_user.change_info("full_name", new_val)
                    case 2:
                        self.session_user.change_info("email", new_val)
                    case 3:
                        self.session_user.change_info("password", new_val)
                    case 4:
                        self.settings()
                self.settings()

            case 2:
                if self.session_user.role == "ADMIN":
                    AdminUI(self.session_user).admin_menu()
                else:
                    CustomerUI(self.session_user).customer_menu()


class CustomerUI(Basic):
    def __init__(self, session):
        super().__init__(session)

    def customer_menu(self):
        pass


class CompanyUI(Basic):
    def __init__(self, session):
        super().__init__(session)

    def company_menu(self):
        pass

    def add_company(self):
        pass

    def delete_company(self):
        pass

    def show_company(self):
        pass


class AdminUI(Basic):
    def __init__(self, session):
        super().__init__(session)

    def admin_menu(self):
        text = """
            1) Company
            2) settings
            3) <- back
        """
        key = int(input(text))
        match key:
            case 1:

                text = """
                    1) add company
                    
                    2) <- back
                """
                key = int(input(text))
                match key:
                    case 1:
                        pass
                    case 2:
                        self.admin_menu()

            case 2:
                self.settings()
            case 3:
                UI()


def register():
    d = {
        "full_name": input("Full_name: "),
        "email": input("Email: "),
        "password": input("Password: ")
    }
    user = User(**d)
    if user.check_full_name():
        print("Your email already exists!")
        return
    user.save_user()
    print("Registration successful !")


def login():
    d = {
        "email": input("Email:"),
        "password": input("Password:"),
    }
    obj = User(**d)
    session_user = obj.login_check()
    if not session_user:
        print("Wrong email or password !")
        return
    print(f"Welcome {session_user.full_name}")
    if session_user.role == "ADMIN":
        AdminUI(session_user).admin_menu()
    else:
        CustomerUI(session_user).customer_menu()


def UI():
    while True:
        text = """
            1) Register
            2) Login
            3) Exit
            >>>>   """
        key = int(input(text))
        match key:
            case 1:
                register()
            case 2:
                login()
            case 3:
                break


UI()
