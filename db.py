import sqlite3
from dataclasses import dataclass


@dataclass
class DB:
    con = sqlite3.connect("shops.sqlite")
    cur = con.cursor()

    query_user = """
        create table if not exists Users(
        id integer primary key autoincrement,
        full_name varchar(255),
        email varchar(255),
        password varchar(255),
        role varchar(20) default 'CUSTOMER',
        created_at date default current_date
    );
    """

    query_company = """
        create table if not exists Company(
        id integer primary key autoincrement,
        company_name vaarchar(255),
        created_at date default current_date
        );
    """

    query_car = """
        create table if not exists Car(
        id integer primary key autoincrement,
        company_id integer not null,
        name varchar(255),
        year varchar(100),
        color varchar(255),
        price integer,
        praberg integer not null,
        created_at date default current_date
        );
    """

    cur.execute(query_user)
    cur.execute(query_company)
    cur.execute(query_car)
    con.commit()
