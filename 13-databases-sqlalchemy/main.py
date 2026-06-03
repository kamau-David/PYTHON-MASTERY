"""Creating tables, inserting, querying, updating, and deleting with
SQLAlchemy's ORM (Session-based) API."""

from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from models import Base, Author, Book

engine = create_engine("sqlite:///demo.db", echo=False)
Base.metadata.create_all(engine)   # creates tables if they don't exist

with Session(engine) as session:
    # --- Create ---
    ngugi = Author(name="Ngũgĩ wa Thiong'o")
    ngugi.books = [Book(title="Weep Not, Child"), Book(title="Petals of Blood")]
    session.add(ngugi)
    session.commit()
    print("inserted author id:", ngugi.id)

    # --- Read ---
    stmt = select(Author).where(Author.name.like("%Ngũgĩ%"))
    found = session.scalars(stmt).first()
    print("found:", found, "books:", found.books)

    all_books = session.scalars(select(Book)).all()
    print("all books:", all_books)

    # --- Update ---
    book = session.scalars(select(Book).where(Book.title == "Petals of Blood")).first()
    book.title = "Petals of Blood (Revised Edition)"
    session.commit()
    print("updated:", book)

    # --- Delete ---
    session.delete(book)
    session.commit()
    print("remaining books:", session.scalars(select(Book)).all())
