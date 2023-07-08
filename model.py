from dataclasses import dataclass
from db import DB


@dataclass
class User(DB):
    id: int = None
    full_name: str = None
    email: str = None
    password: str = None
    role: str = None
    created_at: str = None

    def check_full_name(self):
        query = """select id from Users where email = ?"""
        param = (self.email,)
        self.cur.execute(query, param)
        if self.cur.fetchone():
            return True

    def save_user(self):
        query = """insert into Users(full_name, email, password)
        values (?, ?, ?)"""
        parametrs = (self.full_name, self.email, self.password)
        self.cur.execute(query, parametrs)
        self.con.commit()

    def login_check(self):
        query = """select * from Users where email = ? and password = ?"""
        parametrs = (self.email, self.password,)
        self.cur.execute(query, parametrs)
        user_id = self.cur.fetchone()
        if user_id:
            obj = User(*user_id)
            return obj

    def delete_account(self, account):
        query = f" delete from Users where email =  ? "
        param = (account,)  # noqa
        self.cur.execute(query, param)
        self.con.commit()

    def change_name(self, new_name):  # noqa
        query = f" update Users set full_name = ? where email = ? "
        params = (new_name, self.email)
        self.cur.execute(query, params)
        self.con.commit()

    def change_username(self, new_username):  # noqa
        query = f" update Users set full_name = ? where email = ? "
        params = (new_username, self.email)
        self.cur.execute(query, params)
        self.con.commit()

    def change_password(self, new):
        query = f" update Users set paassword = ? where email = ? "
        params = (new, self.email)
        self.cur.execute(query, params)
        self.con.commit()

    def delete_account1(self):
        query = f" delete from Users where email =  ? "
        param = (self.email,)  # noqa
        self.cur.execute(query, param)
        self.con.commit()

    def change_info(self, col_name, val):
        query = f"""
            update Users set {col_name} = ? where id = ?
            """
        params = (val, self.id)
        self.cur.execute(query, params)
        self.con.commit()



@dataclass
class Car(DB):
    id: int = None
    company_id: str = None
    name: str = None
    year: int = None
    color: str = None
    price: int = None
    praberg: int = None  # noqa
    created_at: str = None

    def add(self):
        query = """select id from Car where name=?"""
        self.cur.execute(query, (self.name,))
        if self.cur:
            return False
        query = """insert into Car (name) values (?)"""
        self.cur.execute(query(self.name, ))
        return True

    def delete(self):
        query = """delete from Car where id=?"""
        self.cur.execute(query, (self.id,))
        self.con.commit()

    def update(self):
        query = """update Car set name=? where id=?"""
        self.cur.execute(query(self.name, self.id))
        self.con.commit()

    def show(self):
        query = """select * from Car;"""
        self.cur.execute(query)
        return self.cur.fetchall()


@dataclass
class Company(DB):
    name: str = None

    def company_name(self):
        query = """select name from Company where name = ?"""
        param = (self.name,)
        self.cur.execute(query, param)
        if self.cur.fetchone():
            return True