import os

print('Start testing all project')
command = 'coverage run -m unittest tests/unit_tests.py; coverage html; coverage report'
os.system(command)
