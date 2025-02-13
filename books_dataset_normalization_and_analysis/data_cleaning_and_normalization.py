import re
import ast
import numpy as np
import pandas as pd
from dateutil import parser

def data_cleaning(dataset):
    """
    Clean and preprocess the dataset.

    Parameters:
    dataset (pd.DataFrame): The input dataset containing book information.

    Returns:
    pd.DataFrame: The cleaned and preprocessed dataset.
    """
    dataset.columns = ['book_id', 'title', 'series', 'author', 'rating', 'description',
        'language', 'isbn', 'genres', 'characters', 'book_format', 'edition',
            'pages', 'publisher', 'publish_date','first_publish_date', 'awards',
            'num_ratings', 'ratings_by_stars', 'liked_percent', 'setting', 'cover_img',
            'bbe_score', 'bbe_votes', 'price']

    def transform_book_id(text):
        return text.split('-')[0].split('.')[0].strip()

    dataset['book_id'] = dataset['book_id'].apply(transform_book_id)

    dataset['author'] = dataset['author'].str.replace(', more…', '')
    dataset['pages'] = dataset['pages'].str.replace(' page', '')

    dataset['book_id'] = pd.to_numeric(dataset['book_id'], errors='coerce')
    dataset['pages'] = pd.to_numeric(dataset['pages'], errors='coerce')
    dataset['price'] = pd.to_numeric(dataset['price'], errors='coerce')

    dataset = dataset.drop_duplicates(subset=['book_id'], keep='first')

    dataset = dataset.sort_values(by=['book_id'], ascending=True)
    dataset.reset_index(drop=True, inplace=True)
    dataset.index = dataset.index + 1

    def remove_commas_in_parentheses(text):
        return re.sub(r'\([^()]+\)', lambda x: x.group().replace(',', ';'), text)
        
    dataset['author'] = dataset['author'].apply(remove_commas_in_parentheses)
    
    print('Dataset sample after cleaning: \n', dataset.head(3))
    return dataset

def transform_authors(dataset):
    """
    Transform and extract author information from the dataset.

    Parameters:
    dataset (pd.DataFrame): The input dataset containing book information.

    Returns:
    tuple: A tuple containing two DataFrames:
        - authors: DataFrame containing unique authors.
        - authors_books_bridge: DataFrame mapping authors to books.
    """
    authors_exploded = dataset[['book_id', 'author']]
    authors_exploded.loc[:, 'author'] = authors_exploded['author'].apply(lambda x: x.split(', ') if isinstance(x, str) else x)
    authors_exploded = authors_exploded.explode('author')

    authors = authors_exploded[['author']].drop_duplicates().reset_index(drop=True)
    authors.index = authors.index + 1
    authors['author_id'] = authors.index

    authors_books_bridge = pd.merge(authors_exploded, authors, on='author', how='left')
    authors_books_bridge.rename(columns = {'index':'author_id'}, inplace = True)
    authors_books_bridge.rename_axis('index', inplace=True)
    authors_books_bridge.index = authors_books_bridge.index + 1
    authors_books_bridge.drop(columns=['author'], inplace=True)

    authors.drop(columns=['author_id'], inplace=True)
    authors.rename_axis('author_id', inplace=True)

    del authors_exploded
    print('\nAuthors df sample: \n', authors.head(3))
    return authors, authors_books_bridge

def transform_genres(dataset):
    """
    Transform and extract genre information from the dataset.

    Parameters:
    dataset (pd.DataFrame): The input dataset containing book information.

    Returns:
    tuple: A tuple containing two DataFrames:
        - genres: DataFrame containing unique genres.
        - genres_books_bridge: DataFrame mapping genres to books.
    """
    genres_exploded = dataset[['book_id', 'genres']]
    genres_exploded.loc[:, 'genres'] = genres_exploded['genres'].str.replace(r'\[|\]|\'', '', regex=True)
    genres_exploded.loc[:, 'genres'] = genres_exploded['genres'].apply(lambda x: x.split(', ') if isinstance(x, str) else x)
    genres_exploded = genres_exploded.explode('genres')

    genres = genres_exploded[['genres']].drop_duplicates().reset_index(drop=True)
    genres.index = genres.index + 1
    genres['genre_id'] = genres.index

    genres_books_bridge = pd.merge(genres_exploded, genres, on='genres', how='left')
    genres_books_bridge.rename(columns = {'index':'genre_id'}, inplace = True)
    genres_books_bridge.rename_axis('index', inplace=True)
    genres_books_bridge.index = genres_books_bridge.index + 1
    genres_books_bridge.drop(columns=['genres'], inplace=True)

    genres.drop(columns=['genre_id'], inplace=True)
    genres.rename_axis('genre_id', inplace=True)
    genres.rename(columns = {'genres':'genre'}, inplace = True)

    del genres_exploded
    print('\nGenres df sample: \n', genres.head(3))
    return genres, genres_books_bridge

def transform_characters(dataset):
    """
    Transform and extract character information from the dataset.

    Parameters:
    dataset (pd.DataFrame): The input dataset containing book information.

    Returns:
    tuple: A tuple containing two DataFrames:
        - characters: DataFrame containing unique characters.
        - characters_books_bridge: DataFrame mapping characters to books.
    """
    characters_exploded = dataset[['book_id', 'characters']]
    characters_exploded.loc[:, 'characters'] = characters_exploded['characters'].str.replace(r'\[|\]|\'', '', regex=True)
    characters_exploded.loc[:, 'characters'] = characters_exploded['characters'].apply(lambda x: x.split(', ') if isinstance(x, str) else x)
    characters_exploded = characters_exploded.explode('characters')

    characters = characters_exploded[['characters']].drop_duplicates().reset_index(drop=True)
    characters.index = characters.index + 1
    characters['character_id'] = characters.index

    characters_books_bridge = pd.merge(characters_exploded, characters, on='characters', how='left')
    characters_books_bridge.rename(columns = {'index':'character_id'}, inplace = True)
    characters_books_bridge.rename_axis('index', inplace=True)
    characters_books_bridge.index = characters_books_bridge.index + 1
    characters_books_bridge.drop(columns=['characters'], inplace=True)

    characters.drop(columns=['character_id'], inplace=True)
    characters.rename_axis('character_id', inplace=True)
    characters.rename(columns = {'characters':'character'}, inplace = True)

    del characters_exploded
    print('\nCharacters df sample: \n', characters.head(3))
    return characters, characters_books_bridge

def transform_awards(dataset):
    """
    Transform and extract award information from the dataset.

    Parameters:
    dataset (pd.DataFrame): The input dataset containing book information.

    Returns:
    tuple: A tuple containing two DataFrames:
        - awards: DataFrame containing unique awards.
        - awards_books_bridge: DataFrame mapping awards to books.
    """
    awards_exploded = dataset[['book_id', 'awards']]
    awards_exploded.loc[:, 'awards'] = awards_exploded['awards'].str.replace(r'\[|\]|\'', '', regex=True)
    awards_exploded.loc[:, 'awards'] = awards_exploded['awards'].apply(lambda x: x.split(', ') if isinstance(x, str) else x)
    awards_exploded = awards_exploded.explode('awards')

    awards = awards_exploded[['awards']].drop_duplicates().reset_index(drop=True)
    awards.index = awards.index + 1
    awards['award_id'] = awards.index

    awards_books_bridge = pd.merge(awards_exploded, awards, on='awards', how='left')
    awards_books_bridge.rename(columns = {'index':'award_id'}, inplace = True)
    awards_books_bridge.rename_axis('index', inplace=True)
    awards_books_bridge.index = awards_books_bridge.index + 1
    awards_books_bridge.drop(columns=['awards'], inplace=True)

    awards.drop(columns=['award_id'], inplace=True)
    awards.rename_axis('award_id', inplace=True)
    awards.rename(columns = {'awards':'award'}, inplace = True)

    del awards_exploded
    print('\nAwards df sample: \n', awards.head(3))
    return awards, awards_books_bridge

def transform_settings(dataset):
    """
    Transform and extract setting information from the dataset.

    Parameters:
    dataset (pd.DataFrame): The input dataset containing book information.

    Returns:
    tuple: A tuple containing two DataFrames:
        - settings: DataFrame containing unique settings.
        - settings_books_bridge: DataFrame mapping settings to books.
    """
    settings_exploded = dataset[['book_id', 'setting']]
    settings_exploded.loc[:, 'setting'] = settings_exploded['setting'].str.replace(r'\[|\]|\'', '', regex=True)

    def split_setting(setting):
        # Split by comma followed by a space only if not within parentheses
        parts = re.split(r',\s*(?=[A-Z][a-z]*(?:\s[A-Z][a-z]*)*(?:\s\([A-Za-z\s]*\)))', setting)
        return parts

    settings_exploded.loc[:, 'setting'] = settings_exploded['setting'].apply(lambda x: split_setting(x) if isinstance(x, str) else x)
    settings_exploded = settings_exploded.explode('setting')

    settings = settings_exploded[['setting']].drop_duplicates().reset_index(drop=True)
    settings.index = settings.index + 1
    settings['setting_id'] = settings.index

    settings_books_bridge = pd.merge(settings_exploded, settings, on='setting', how='left')
    settings_books_bridge.rename(columns = {'index':'setting_id'}, inplace = True)
    settings_books_bridge.rename_axis('index', inplace=True)
    settings_books_bridge.index = settings_books_bridge.index + 1
    settings_books_bridge.drop(columns=['setting'], inplace=True)

    settings.drop(columns=['setting_id'], inplace=True)
    settings.rename_axis('setting_id', inplace=True)

    del settings_exploded
    print('\nSettings df sample: \n', settings.head(3))
    return settings, settings_books_bridge

def transform_ratings_and_bbe_scores(dataset):
    """
    Transform and extract ratings and BBE scores from the dataset.

    Parameters:
    dataset (pd.DataFrame): The input dataset containing book information.

    Returns:
    pd.DataFrame: A DataFrame with transformed ratings and BBE scores information.
    """
    ratings_and_bbe_scores = dataset[['book_id', 'rating', 'num_ratings', 'ratings_by_stars', 'liked_percent', 'bbe_score', 'bbe_votes' ]]
    ratings_and_bbe_scores = pd.DataFrame(ratings_and_bbe_scores)

    def convert_to_list(ratings_str):
        return ast.literal_eval(ratings_str)

    ratings_and_bbe_scores['ratings_by_stars'] = ratings_and_bbe_scores['ratings_by_stars'].apply(convert_to_list)
    expanded_stars = pd.DataFrame(ratings_and_bbe_scores['ratings_by_stars'].tolist(), index=ratings_and_bbe_scores.index)
    expanded_stars.columns = ['5_stars', '4_stars', '3_stars', '2_stars', '1_star']

    ratings_and_bbe_scores = pd.concat([ratings_and_bbe_scores, expanded_stars], axis=1)
    ratings_and_bbe_scores.drop(columns=['ratings_by_stars'], inplace=True)
    ratings_and_bbe_scores = ratings_and_bbe_scores[['book_id', 'rating', 'num_ratings', '5_stars', '4_stars', '3_stars', '2_stars', '1_star', 'liked_percent', 'bbe_score', 'bbe_votes' ]]
    ratings_and_bbe_scores.rename(columns = {'5_stars':'five_stars', '4_stars':'four_stars', '3_stars':'three_stars', '2_stars':'two_stars', '1_star':'one_star'}, inplace = True)

    print('\nRatings and BBE scores df sample: \n', ratings_and_bbe_scores.head(3))
    return ratings_and_bbe_scores

def transform_publication_info(dataset):
    """
    Transform and extract publication information from the dataset.

    Parameters:
    dataset (pd.DataFrame): The input dataset containing book information.

    Returns:
    pd.DataFrame: A DataFrame with transformed publication information.
    """
    publication_info = dataset[['book_id', 'publisher', 'publish_date', 'first_publish_date']]

    def parse_date(date_str):
        for fmt in ('%B %d %Y', '%m/%d/%y', '%Y-%m-%d', '%B %d, %Y'):
            try:
                return pd.to_datetime(date_str, format=fmt)
            except (ValueError, TypeError):
                continue
        try:
            return parser.parse(date_str)
        except (ValueError, TypeError):
            return np.nan

    publication_info.loc[:, 'publish_date'] = publication_info['publish_date'].apply(parse_date)
    publication_info.loc[:, 'first_publish_date'] = publication_info['first_publish_date'].apply(parse_date)

    publication_info.loc[:, 'publish_date'] = pd.to_datetime(publication_info['publish_date'], errors='coerce').dt.strftime('%Y-%m-%d')
    publication_info.loc[:, 'first_publish_date'] = pd.to_datetime(publication_info['first_publish_date'], errors='coerce').dt.strftime('%Y-%m-%d')

    print('\nPublication info df sample: \n', publication_info.head(3))
    return publication_info

def drop_columns(dataset):
    """
    Drop unnecessary columns from the dataset.

    Parameters:
    dataset (pd.DataFrame): The input dataset containing book information.

    Returns:
    pd.DataFrame: The dataset with unnecessary columns removed.
    """
    dataset.drop(columns=['author', 'genres', 'characters', 'awards', 'rating', 'num_ratings', 'ratings_by_stars', 'liked_percent', 'bbe_score', 'bbe_votes', 'publisher', 'publish_date', 'first_publish_date', 'setting'], inplace=True)
    return dataset
