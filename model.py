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
class User(DB):
    name: str = None

    def campany_name(self):
        query = """select name from users where name = ?"""
        parametr = (self.name,)
        self.cur.execute(query, parametr)
        if self.cur.fetchone():
            return True
