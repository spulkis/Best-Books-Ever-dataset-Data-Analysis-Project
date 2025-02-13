import pandas as pd
from decouple import config
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database 

# Importing data transformation functions from separate modules
from data_cleaning_and_normalization import (
    data_cleaning, transform_authors, transform_awards, 
    transform_characters, transform_genres, 
    transform_publication_info, transform_ratings_and_bbe_scores, 
    transform_settings, drop_columns
)
from database_schema_tables_definition import Base
from data_utils import data_to_sql

if __name__ == "__main__":
    # Load environment variables
    CONNECTION_STRING = config('CONNECTION_STRING')
    CSV_PATH = config('CSV_PATH')

    # Create a database engine
    engine = create_engine(CONNECTION_STRING)

    # If the database doesn't exist, create it
    if not database_exists(engine.url):
        create_database(engine.url)
    print("Database exists: ", database_exists(engine.url))

    # Load CSV data into a pandas DataFrame
    books = pd.read_csv(CSV_PATH)
    print("Dataset sample: \n", books.head(3))

    # Data cleaning and normalization
    books = data_cleaning(books)

    # Create database tables based on the defined schema
    Base.metadata.create_all(engine)

    # Transform data and insert into respective tables
    authors, authors_books_bridge = transform_authors(books)
    awards, awards_books_bridge = transform_awards(books)
    characters, characters_books_bridge = transform_characters(books)
    genres, genres_books_bridge = transform_genres(books)
    publication_info = transform_publication_info(books)
    ratings_and_bbe_scores = transform_ratings_and_bbe_scores(books)
    settings, settings_books_bridge = transform_settings(books)

    # Drop unnecessary columns from the books DataFrame
    books = drop_columns(books)

    # Insert transformed data into respective database tables
    data_table_pairs = [
        (books, 'books'),
        (authors, 'authors'),
        (authors_books_bridge, 'authors_books_bridge'),
        (awards, 'awards'),
        (awards_books_bridge, 'awards_books_bridge'),
        (characters, 'characters'),
        (characters_books_bridge, 'characters_books_bridge'),
        (genres, 'genres'),
        (genres_books_bridge, 'genres_books_bridge'),
        (publication_info, 'publication_info'),
        (ratings_and_bbe_scores, 'ratings_and_bbe_scores'),
        (settings, 'settings'),
        (settings_books_bridge, 'settings_books_bridge')
    ]

    # Loop through each pair and call data_to_sql function
    for data, table in data_table_pairs:
        data_to_sql(data, table, engine)

    # Close the connection associated with the provided SQLAlchemy engine and disposes of all associated resources, ensuring proper cleanup
    engine.dispose()
