from setuptools import setup, find_packages

FUZZY = ['rapidfuzz']
PARQUET = ['pyarrow']

setup(
    name='eda-toolkit',
    version='0.1',
    packages=find_packages(),
    install_requires=['pandas', 'numpy', 'plotly', 'IPython'],
    extras_require={
        'fuzzy': FUZZY,
        'parquet': PARQUET,
        'all': FUZZY + PARQUET,
    },
    author='Warrick Sabatta',
    description='Exploratory data analysis helpers for pandas notebooks',
    license='MIT',
    python_requires='>=3.8',
)
