from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='python-books_dataset_normalization_and_analysis',
    version='1.0',
    packages=find_packages(),
    url='https://github.com/TuringCollegeSubmissions/jmarci-DE1.v2.3.5',
    license='MIT',
    author='Julius Marčiulynas',
    author_email='j.marciulynas@gmail.com',
    description='Normalization and analysis of the GoodReads Best Books dataset',
    long_description=long_description,
    long_description_content_type='text/markdown',
    python_requires=">=3.10",
    install_requires=[
        'matplotlib==3.9.0',
        'numpy==1.26.4',
        'pandas==2.2.2',
        'PyMySQL==1.1.0',
        'pyparsing==3.1.2',
        'python-dateutil==2.9.0.post0',
        'SQLAlchemy==2.0.30',
        'SQLAlchemy-Utils==0.41.2'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Scientific/Engineering :: Information Analysis'
    ],
)
