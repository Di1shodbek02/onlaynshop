import bcrypt
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
                    CustomerUI(self.session_user).customer_menu()  # ✅


class CustomerUI(Basic):
    def __init__(self, session):
        super().__init__(session)

    def customer_menu(self):
        pass


class CarUI(Basic):
    def __init__(self, session):
        super().__init__(session)

    def car_crud(self):

        text = """
                  1) add car
                  2) delete car
                  3) update car
                  4) show car
                  5) <-back
                  Select number >>>"""
        key = int(input(text))
        data = Company().show()
        print(tabulate(data, tablefmt="simple_grid"))
        match key:
            case 1:
                comp_id = int(input("Select comp id:"))
                d = {
                    'name': input("Name: "),
                    'year': int(input('Year: ')),
                    'color': input('Color: '),
                    'price': int(input('Price: ')),
                    'praberg': int(input('Praberg: '))

                }
                data = Car(**d)
                data.cars(comp_id)
                print(tabulate(data, tablefmt="simple_grid"))
                name = input("Enter name of car: ")
                response = Car(name=name).add()
                if not response:
                    print("There is this car in our collection!!!")
                else:
                    print("Success add!")
            case 2:
                comp_id = int(input("Select comp id:"))
                data = Car()
                data.cars(comp_id)
                data = Car().show()
                print(tabulate(data, tablefmt="simple_grid"))
                Id_key = int(input("Id: "))
                Car(id=Id_key).delete()
                print("Successfully delete!")

            case 3:
                comp_id = int(input("Select comp id:"))
                data = Car()
                data.cars(comp_id)
                data = Car().show()
                print(tabulate(data, tablefmt="simple_grid"))
                d = {
                    "Id_key": int(input("Id: ")),
                    "new_name": input("New name: ")
                }
                Car(**d).update()
                print("Success update!!")
            case 4:
                comp_id = int(input("Select comp id:"))
                data = Car()
                data.cars(comp_id)
                data = Car().show()
                print(tabulate(data, tablefmt="simple_grid"))

            case 5:
                CompanyUI(self.session_user).company_crud()
        self.car_crud()


class CompanyUI(Basic):
    def __init__(self, session):
        super().__init__(session)

    def company_crud(self):
        text = """
           1) add company
           2) delete company
           3) update company
           4) show company
           5) <-back
        """
        key = int(input(text))
        match key:
            case 1:
                name = input("Enter name of company: ")
                response = Company(company_name=name).add()
                if not response:
                    print("There is this company in our collection!!!")
                else:
                    print("Success add!")
            case 2:
                data = Company().show()
                print(tabulate(data, tablefmt="simple_grid"))
                Id_key = int(input("Id: "))
                Company(id=Id_key).delete()
                print("Successfully delete!")
            case 3:
                data = Company().show()
                print(tabulate(data, tablefmt="simple_grid"))
                d = {
                    "Id_key": int(input("Id: ")),
                    "new_name": input("New name: ")
                }
                Company(**d).update()
                print("Success update!!")
            case 4:
                data = Company().show()
                print(tabulate(data, tablefmt="simple_grid"))
            case 5:
                AdminUI(self.session_user).admin_menu()
        self.company_crud()


class AdminUI(Basic):
    def __init__(self, session):
        super().__init__(session)

    def admin_menu(self):
        text = """
            1) Company
            2) Cars
            3) settings
            4) <- back
        """
        key = int(input(text))
        match key:
            case 1:
                CompanyUI(self.session_user).company_crud()
            case 2:
                CarUI(self.session_user).car_crud()
            case 3:
                self.settings()
            case 4:
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
    session_user = list(obj.login_check())
    new_post = d["password"]
    bytes_pass = new_post.encode('utf-8')
    if_true = bcrypt.checkpw(bytes_pass, session_user[3])
    if not if_true:
        print("Wrong email or password !")
        return
    # print(f"Welcome {session_user.full_name}")
    if session_user[4] == "ADMIN":
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
