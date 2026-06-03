"""SQLAlchemy ORM models - Python classes that map to database tables."""

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class Author(Base):
    __tablename__ = "authors"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))

    # one-to-many: one author has many books
    books: Mapped[list["Book"]] = relationship(back_populates="author")

    def __repr__(self):
        return f"Author(id={self.id}, name={self.name!r})"


class Book(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(200))
    author_id: Mapped[int] = mapped_column(ForeignKey("authors.id"))

    author: Mapped["Author"] = relationship(back_populates="books")

    def __repr__(self):
        return f"Book(id={self.id}, title={self.title!r})"
