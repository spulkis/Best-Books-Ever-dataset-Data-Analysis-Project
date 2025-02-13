from sqlalchemy import (
    create_engine, ForeignKey, ForeignKeyConstraint,
    Column, String, Integer, Float, Text, Date
)
from sqlalchemy.orm import declarative_base
from decouple import config 

Base = declarative_base()

class Books(Base):
    """
    SQLAlchemy model for the 'books' table.

    Attributes:
    index (int): Primary key, auto-incremented index.
    book_id (int): Unique identifier for the book.
    title (str): Title of the book.
    series (str): Series to which the book belongs.
    description (str): Description of the book.
    language (str): Language of the book.
    isbn (str): ISBN of the book.
    book_format (str): Format of the book (e.g., paperback, hardcover).
    edition (str): Edition of the book.
    pages (int): Number of pages in the book.
    cover_img (str): URL or path to the cover image of the book.
    price (float): Price of the book.
    """
    __tablename__ = "books"

    index = Column(Integer, primary_key=True, unique=True, index=True, autoincrement=True)
    book_id = Column(Integer, index=True)
    title = Column(String(512))
    series = Column(String(512))
    description = Column(Text(collation='utf8mb4_unicode_ci'))
    language = Column(String(255))
    isbn = Column(String(50))
    book_format = Column(String(50))
    edition = Column(String(255))
    pages = Column(Integer)
    cover_img = Column(String(255))
    price = Column(Float)

    def __init__(self, index, book_id, title, series, description, language, isbn, book_format, edition, pages, cover_img, price):
        self.index = index
        self.book_id = book_id
        self.title = title
        self.series = series 
        self.description = description
        self.language = language
        self.isbn = isbn
        self.book_format = book_format 
        self.edition = edition
        self.pages = pages
        self.cover_img = cover_img
        self.price = price

    def __repr__(self):
        return (
        f"<Books(index={self.index}, book_id={self.book_id}, title={self.title}, series={self.series}, "
        f"description={self.description}, language={self.language}, isbn={self.isbn}, book_format={self.book_format}, "
        f"edition={self.edition}, pages={self.pages}, cover_img={self.cover_img}, price={self.price})>"
        )

class Authors(Base):
    """
    SQLAlchemy model for the 'authors' table.

    Attributes:
    author_id (int): Primary key, unique identifier for the author.
    author (str): Name of the author.
    """
    __tablename__ = "authors"
    
    author_id = Column(Integer, primary_key=True, unique=True, index=True)
    author = Column(String(255))

    def __init__(self, author_id, author):
        self.author_id = author_id
        self.author = author

    def __repr__(self):
        return f"<Authors(author_id={self.author_id}, author={self.author})>"

class AuthorsBooks(Base):
    """
    SQLAlchemy model for the 'authors_books_bridge' table.

    Attributes:
    index (int): Primary key, auto-incremented index.
    book_id (int): Foreign key to 'books' table.
    author_id (int): Foreign key to 'authors' table.
    """
    __tablename__ = "authors_books_bridge"
    __table_args__ = (
        ForeignKeyConstraint(["book_id"], ["books.book_id"]),
        ForeignKeyConstraint(['author_id'], ['authors.author_id'])
    )

    index = Column(Integer, primary_key=True, index=True)
    book_id = Column(Integer)
    author_id = Column(Integer)

    def __init__(self, index, book_id, author_id):
        self.index = index
        self.book_id = book_id
        self.author_id = author_id

    def __repr__(self):
        return f"<AuthorsBooks(index={self.index}, book_id={self.book_id}, author_id={self.author_id})>"

class Genres(Base):
    """
    SQLAlchemy model for the 'genres' table.

    Attributes:
    genre_id (int): Primary key, unique identifier for the genre.
    genre (str): Name of the genre.
    """
    __tablename__ = "genres"
    
    genre_id = Column(Integer, primary_key=True, unique=True, index=True)
    genre = Column(String(255))

    def __init__(self, genre_id, genre):
        self.genre_id = genre_id
        self.genre = genre

    def __repr__(self):
        return f"<Genres(genre_id={self.genre_id}, genre={self.genre})>"

class GenresBooks(Base):
    """
    SQLAlchemy model for the 'genres_books_bridge' table.

    Attributes:
    index (int): Primary key, auto-incremented index.
    book_id (int): Foreign key to 'books' table.
    genre_id (int): Foreign key to 'genres' table.
    """
    __tablename__ = "genres_books_bridge"
    __table_args__ = (
        ForeignKeyConstraint(["book_id"], ["books.book_id"]),
        ForeignKeyConstraint(['genre_id'], ['genres.genre_id'])
    )

    index = Column(Integer, primary_key=True)
    book_id = Column(Integer)
    genre_id = Column(Integer)

    def __init__(self, index, book_id, genre_id):
        self.index = index
        self.book_id = book_id
        self.genre_id = genre_id

    def __repr__(self):
        return f"<GenresBooks(index={self.index}, book_id={self.book_id}, genre_id={self.genre_id})>"

class Characters(Base):
    """
    SQLAlchemy model for the 'characters' table.

    Attributes:
    character_id (int): Primary key, unique identifier for the character.
    character (str): Name of the character.
    """
    __tablename__ = "characters"
    
    character_id = Column(Integer, primary_key=True, unique=True, index=True)
    character = Column(String(255))

    def __init__(self, character_id, character):
        self.character_id = character_id
        self.character = character

    def __repr__(self):
        return f"<Characters(character_id={self.character_id}, character={self.character})>"

class CharactersBooks(Base):
    """
    SQLAlchemy model for the 'characters_books_bridge' table.

    Attributes:
    index (int): Primary key, auto-incremented index.
    book_id (int): Foreign key to 'books' table.
    character_id (int): Foreign key to 'characters' table.
    """
    __tablename__ = "characters_books_bridge"
    __table_args__ = (
        ForeignKeyConstraint(["book_id"], ["books.book_id"]),
        ForeignKeyConstraint(['character_id'], ['characters.character_id'])
    )

    index = Column(Integer, primary_key=True)
    book_id = Column(Integer)
    character_id = Column(Integer)

    def __init__(self, index, book_id, character_id):
        self.index = index
        self.book_id = book_id
        self.character_id = character_id

    def __repr__(self):
        return f"<CharactersBooks(index={self.index}, book_id={self.book_id}, character_id={self.character_id})>"

class Awards(Base):
    """
    SQLAlchemy model for the 'awards' table.

    Attributes:
    award_id (int): Primary key, unique identifier for the award.
    award (str): Name of the award.
    """
    __tablename__ = "awards"
    
    award_id = Column(Integer, primary_key=True, unique=True, index=True)
    award = Column(String(255))

    def __init__(self, award_id, award):
        self.award_id = award_id
        self.award = award

    def __repr__(self):
        return f"<Awards({self.award_id}, {self.award})>"
    
class AwardsBooks(Base):
    """
    SQLAlchemy model for the 'awards_books_bridge' table.

    Attributes:
    index (int): Primary key, auto-incremented index.
    book_id (int): Foreign key to 'books' table.
    award_id (int): Foreign key to 'awards' table.
    """
    __tablename__ = "awards_books_bridge"
    __table_args__ = (
        ForeignKeyConstraint(["book_id"], ["books.book_id"]),
        ForeignKeyConstraint(['award_id'], ['awards.award_id'])
    )

    index = Column(Integer, primary_key=True)
    book_id = Column(Integer)
    award_id = Column(Integer)

    def __init__(self, index, book_id, award_id):
        self.index = index
        self.book_id = book_id
        self.award_id = award_id

    def __repr__(self):
        return f"<AwardsBooks(index={self.index}, book_id={self.book_id}, award_id={self.award_id})>"

class Settings(Base):
    """
    SQLAlchemy model for the 'settings' table.

    Attributes:
    setting_id (int): Primary key, unique identifier for the setting.
    setting (str): Text of the setting.
    """
    __tablename__ = "settings"
    
    setting_id = Column(Integer, primary_key=True, unique=True, index=True)
    setting = Column(Text)

    def __init__(self, setting_id, setting):
        self.setting_id = setting_id
        self.setting = setting

    def __repr__(self):
        return f"<Settings({self.setting_id}, {self.setting})>"

class SettingsBooks(Base):
    """
    SQLAlchemy model for the 'settings_books_bridge' table.

    Attributes:
    index (int): Primary key, auto-incremented index.
    book_id (int): Foreign key to 'books' table.
    setting_id (int): Foreign key to 'settings' table.
    """
    __tablename__ = "settings_books_bridge"
    __table_args__ = (
        ForeignKeyConstraint(["book_id"], ["books.book_id"]),
        ForeignKeyConstraint(['setting_id'], ['settings.setting_id'])
    )

    index = Column(Integer, primary_key=True)
    book_id = Column(Integer)
    setting_id = Column(Integer)

    def __init__(self, index, book_id, setting_id):
        self.index = index
        self.book_id = book_id
        self.setting_id = setting_id

    def __repr__(self):
        return f"<SettingsBooks(index={self.index},{self.book_id}, setting={self.setting_id})>"

class RatingsAndBBEScores(Base):
    """
    SQLAlchemy model for the 'ratings_and_bbe_scores' table.

    Attributes:
    index (int): Primary key, auto-incremented index.
    book_id (int): Foreign key to 'books' table.
    rating (float): Rating of the book.
    num_ratings (int): Number of ratings.
    five_stars (int): Number of five-star ratings.
    four_stars (int): Number of four-star ratings.
    three_stars (int): Number of three-star ratings.
    two_stars (int): Number of two-star ratings.
    one_star (int): Number of one-star ratings.
    liked_percent (float): Liked percentage.
    bbe_score (float): Bookbub engagement score.
    bbe_votes (int): Number of Bookbub votes.
    """
    __tablename__ = 'ratings_and_bbe_scores'
    
    index = Column(Integer, primary_key=True, unique=True, index=True)
    book_id = Column(Integer, ForeignKey('books.book_id'))
    rating = Column(Float)
    num_ratings = Column(Integer)
    five_stars = Column(Integer)
    four_stars = Column(Integer)
    three_stars = Column(Integer)
    two_stars = Column(Integer)
    one_star = Column(Integer)
    liked_percent = Column(Float)
    bbe_score = Column(Float)
    bbe_votes = Column(Integer)

    def __init__(self, index, book_id, rating, num_ratings, five_stars, four_stars, three_stars, two_stars, one_star, liked_percent, bbe_score, bbe_votes):
        self.index = index
        self.book_id = book_id
        self.rating = rating
        self.num_ratings = num_ratings
        self.five_stars = five_stars
        self.four_stars = four_stars
        self.three_stars = three_stars
        self.two_stars = two_stars
        self.one_star = one_star
        self.liked_percent = liked_percent
        self.bbe_score = bbe_score
        self.bbe_votes = bbe_votes

    def __repr__(self):
        return f"<RatingsAndBBEScores(index={self.index}, book_id={self.book_id}, rating={self.rating}, num_ratings={self.num_ratings}, five_stars={self.five_stars}, four_stars={self.four_stars}, three_stars={self.three_stars}, two_stars={self.two_stars}, one_star={self.one_star}, liked_percent={self.liked_percent}, bbe_score={self.bbe_score}, bbe_votes={self.bbe_votes})>"

class PublicationInfo(Base):
    """
    SQLAlchemy model for the 'publication_info' table.

    Attributes:
    index (int): Primary key, auto-incremented index.
    book_id (int): Foreign key to 'books' table.
    publisher (str): Publisher of the book.
    publish_date (Date): Date of publication.
    first_publish_date (Date): Date of the first publication.
    """
    __tablename__ = 'publication_info'
    
    index = Column(Integer, primary_key=True, unique=True, index=True)
    book_id = Column(Integer, ForeignKey('books.book_id'))
    publisher = Column(String(255))
    publish_date = Column(Date)
    first_publish_date = Column(Date)

    def __init__(self, index, book_id, publisher, publish_date, first_publish_date):
        self.index = index
        self.book_id = book_id
        self.publisher = publisher
        self.publish_date = publish_date
        self.first_publish_date = first_publish_date
        
    def __repr__(self):
        return f"<PublicationInfo(index={self.index}, book_id={self.book_id}, publisher={self.publisher}, publish_date={self.publish_date}, first_publish_date={self.first_publish_date})>"
