[![python](https://img.shields.io/badge/Python-gray?logo=Python)](https://www.python.org)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
## Data Analysis Project: Best Books Ever dataset

This project focuses on analyzing a dataset of books, aiming to extract insights and facilitate further analysis. It involves various data processing steps, including data normalization, transformation, and insertion into a relational database.

### Key Features:
1. **Data Extraction and Cleaning:** The dataset is sourced from Goodreads and undergoes cleaning and normalization procedures to ensure consistency and reliability.
2. **Database Schema Definition:** SQLAlchemy is utilized to define the database schema, including tables for books, authors, genres, characters, awards, settings, ratings, and publication information.
3. **Data Insertion and Error Handling:** Data is inserted into the database tables, with error handling mechanisms implemented to log any SQLAlchemy errors encountered during insertion.

### Installation

1. Clone this repository.
2. Install the required dependencies using pip:

   ```bash
   pip install -r requirements.txt
3. Download Raw Dataset from > https://www.kaggle.com/datasets/thedevastator/comprehensive-overview-of-52478-goodreads-best-b
4. The code utilizes the 'decouple' library for defining environment variables. You can specify your 'CONNECTION_STRING' and 'CSV_PATH' constants in your configuration file (such as a .env or .ini file) or modify them in the initialization code.
5. You can start data exctraction, cleaning and insertion process by launching a code:

   ```bash
   python __init__.py
6. For further data analysis, please check 'books_dataset_analysis.ipynb' Jupyter Notebook file in examples folder.

 **Alternitavely:** For a guided analysis of the 'Best Books Ever' dataset, refer to the books_dataset_normalization_and_analysis.ipynb Jupyter Notebook file (in examples folder), which contains the full code.

### Suggestions for future improvements

- **Error Handling:** Some parts of the code currently doesn't handle potential errors explicitly. Consider implementing try-except blocks or custom error classes to handle issues like database connection failures, invalid CSV data format, or unexpected SQL exceptions.
- **Further dataset cleaning:** There might still be mistakes in the transformed dataset. Additional checks could be performed to ensure data integrity and correctness.
- **Analysis and Visualization:** Further analysis and visualization techniques can be applied to derive insights from the dataset.

**Feel free to fork this repository and make your own modifications!**