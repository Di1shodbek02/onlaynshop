from dataclasses import dataclass

import bcrypt

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
        parametrs = (self.full_name, self.email, bcrypt.hashpw(self.password.encode('utf-8'), bcrypt.gensalt()))
        self.cur.execute(query, parametrs)
        self.con.commit()

    def login_check(self):
        query = """select * from Users where email = ?"""
        parametrs = (self.email,)
        self.cur.execute(query, parametrs)
        user_id = self.cur.fetchone()
        return user_id

            # obj = User(*user_id)
            # return obj

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

    def add(self, name, year, color, price, praberg):
        query = """select * from Car where name=?"""
        self.cur.execute(query, (self.name,))
        if self.cur:
            return False
        query = """insert into Car (name, year, color, price, praberg) values (?, ?, ?, ?, ?)"""
        self.cur.execute(query(name, year, color, price, praberg,))
        return True

    def delete(self):
        query = """delete from Car where id=?"""
        self.cur.execute(query, (self.id,))
        self.con.commit()

    def update(self):
        query = """update Car set name=? where id=?"""
        self.cur.execute(query(self.name, self.id, ))
        self.con.commit()

    def show(self):
        query = """select * from Car"""
        self.cur.execute(query)
        return self.cur.fetchall()

    def cars(self, company_id):
        query = """select * from Car where company_id = ?"""
        param = (company_id,)
        self.cur.execute(query, param)
        data = self.cur.fetchall()
        self.con.commit()
        return data


@dataclass
class Company(DB):
    id: int = None
    company_name: str = None
    created_at: str = None

    def add(self):
        query = """select id from Company where company_name=?"""
        self.cur.execute(query, (self.company_name,))
        if self.cur.fetchall():
            return False
        query = """insert into Company (company_name) values (?)"""
        self.cur.execute(query, (self.company_name,))
        self.con.commit()
        return True

    def delete(self):
        query = """delete from Company where id=?"""
        self.cur.execute(query, (self.id,))
        self.con.commit()

    def update(self):
        query = """update Company set company_name=? where id=?"""
        self.cur.execute(query, (self.company_name, self.id,))
        self.con.commit()

    def show(self):
        query = """ select * from Company"""
        self.cur.execute(query)
        return self.cur.fetchall()
