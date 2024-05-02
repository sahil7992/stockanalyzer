from setuptools import setup, find_packages

setup(
    name='stockanalyzer',
    version='0.1.0',
    author='sahil Dineshbhai Pambhar',
    author_email='sahilpambhar7@gmail.com',
    description='A Python package for analyzing and visualizing stock market data.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/sahil7992/stockanalyzer',  
    packages=find_packages(),
    install_requires=[
        'pandas>=1.0',
        'numpy',
        'matplotlib',
        'yfinance'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Financial and Insurance Industry',
        'Topic :: Office/Business :: Financial :: Investment',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    python_requires='>=3.7',
)
