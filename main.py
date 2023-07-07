from tabulate import tabulate
from model import User, Company
from model import Car


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
        print("Wrong username or password !")
        return
    print(f"Welcome {session_user.full_name}")
    if session_user.role == "ADMIN":
        admin_menu()
    else:
        customer_menu()


def admin_menu():
    text = """
        1) Company
        2) Cars
        3) settings
        4) <- back
        >>>>  """
    key = int(input(text))
    match key:
        case 1:
            pass
        case 2:
            crud_menu = """
                1) add car
                2) delete car
                3) update car
                4) show car
                5) <-back
                Select number >>>"""
            key = int(input(crud_menu))
            match key:
                case 1:
                    name = input("Enter name of car: ")
                    response = Car(name=name).add()
                    if not response:
                        print("There is this car in our collection!!!")
                    else:
                        print("Success add!")
                    admin_menu()
                case 2:
                    datas = Car().show()
                    print(tabulate(datas, tablefmt="simple_grid"))
                    Id_key = int(input("Id: "))
                    Car(id=Id_key).delete()
                    print("Successfully delete!")
                    admin_menu()
                case 3:
                    datas = Car().show()
                    print(tabulate(datas, tablefmt="simple_grid"))
                    d = {
                        "Id_key": int(input("Id: ")),
                        "new_name": input("New name: ")
                    }
                    Car(**d).update()
                    print("Success update!!")
                    admin_menu()
                case 4:
                    datas = Car().show()
                    print(tabulate(datas, tablefmt="simple_grid"))
                    admin_menu()
                case 5:
                    UI()
        case 3:
            pass
        case 4:
            UI()

# def query_company():
#     table = {
#         "company_name": input("name"),
#     }
#     model = Company(**table)
#
#     if model.company_name():
#         print(" The account already exists !")
#     return


def customer_menu():
    pass


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
