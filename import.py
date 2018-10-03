import csv
import os

from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

os.environ['DATABASE_URL'] = 'postgres://vwkbfwdszgpuhl:5af21389486c95e925e6103b2fdc61becd23178e9ffd938a79575eaad369bbdc@ec2-54-217-235-137.eu-west-1.compute.amazonaws.com:5432/d49ua05gin9msl'

engine = create_engine('postgres://vwkbfwdszgpuhl:5af21389486c95e925e6103b2fdc61becd23178e9ffd938a79575eaad369bbdc@ec2-54-217-235-137.eu-west-1.compute.amazonaws.com:5432/d49ua05gin9msl')
db = scoped_session(sessionmaker(bind=engine))

def main():
    f = open("books.csv")
    reader = csv.reader(f)
    for isbn, title, author, year in reader:
        db.execute("INSERT INTO books (isbn, title, author, year) VALUES (:isbn, :title, :author, :year)",
                   {"isbn": isbn, "title": title, "author": author, "year": year})
        print(f"Added books from {isbn}")
    db.commit()


if __name__ == "__main__":
    main()
