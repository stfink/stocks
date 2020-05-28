from setuptools import setup

setup (
    name='stocks',
    description='Stock Market Reader',
    test_suite='tests',
    packages=[
        'stocks',
        'stocks/log',
        'stocks/api'
    ]
)