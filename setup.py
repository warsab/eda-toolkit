from setuptools import setup, find_packages

setup(
    name='eda-toolkit',
    version='0.1',
    packages=find_packages(),
    install_requires=['pandas', 'numpy', 'plotly', 'IPython'],
    extras_require={
        'fuzzy': ['rapidfuzz'],
    },
    author='Warrick Sabatta',
    description='Exploratory data analysis helpers for pandas notebooks',
    license='MIT',
    python_requires='>=3.8',
)
