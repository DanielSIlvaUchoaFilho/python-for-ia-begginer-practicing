# import requests

# # Download a web page
# response = requests.get("https://api.github.com")
# print(response.status_code)  # Should print 200

# print('hi')

"""
sup
hurry up
"""

name = 'Elijah'

list_of_names = """
James
Elijah
"""

first_name = 'Enoque'
last_name = 'Silva'

names_together = first_name + ' ' + last_name

long_dash = '-' * 30

len(long_dash)

print('hi')

is_logged_in = False

can_vote = 16 >= 18

# and or not

name = 'Elijah'

good_morning_message = f'good morning {name}'

good_morning_message.lower()
good_morning_message.upper()
good_morning_message.title()

print('morning' in good_morning_message) # is the word morning in this
print(good_morning_message.startswith('g')) # true in this case
print(good_morning_message.endswith('morning')) # false in this case
print(good_morning_message.endswith(name)) # true in this case
print(good_morning_message.find('morning')) # 5
print(good_morning_message.count('morning')) # counts how many times something appears
print(good_morning_message.replace('morning', 'afternoon'))

age = 18    

if age >= 65:
    print('u can retire now')
elif age >= 18:
    print('adult')
else:
    print('not an adult')

for i in range(5):
    print('hi')

for i in range(1, 7):
    print(i)

for i in range(0, 12, 2):
    print(i)

# data structures

list = ['Elijah', 18, True] # list, acho q é um array
list[0]
list[-1]
list[0: 2]
list[1:]
list.append('Engenieer')
list.append('Arquitect')
list.remove('Arquitect')
list.insert(1, 10000)
#len(length), count(see how many times something appears), index(search for something's index)
#sort(sort in place), reverse(reverse the order of the elements), copy(creates a copy of the list)

#dictionaryy
person = {
    'name': 'Elijah',
    'profession': 'Engenieer',
    'age': 18,
    'hi': 'hi'
}

person['name']
person['age'] = 65
person['state'] = 'california'
del person['hi']
# isso aq da erro
print(person['job'])
# esse retorna None
print(person.get('job'))
# esse retorna a palavra q você botar como segundo argumento
print(person.get('job', 'whats that?'))

# .pop() removes and returns and .clear remove all
#.keys() .values() .items
# check if some key exists
# if '' in person
# update multiple values
# .updade('': , '': '')

# Tuples r immutable
#single items need a comma
name = ('Elijah',)
# implicit
salary = 70000, 10000, 3000000
print(name[0])
print(salary[0: 2])
n = 3, 5
n1, n2 = n
n3, n4, n5 = 1, 2, 3
# da p swape variables too

# Sets
# they make sure there's no duplicate values
set = set()
# if theres values pyton knows its a set, but if there's not it will assume
# u meant to use a dictionary
set1 = {1, 2, 3, 4, 5}
# .add .remove .discart if '' in :

def say_hi():
    print('sup kkk')
    # u dont need to write pass, but it just says that ur returning nothing
    # pass
    # thats the pass

def hurry_up(name):
    print(f'hurry up {name}')

hurry_up('Elijah')
# hurry_up(name = 'John')

def n(n1, n3 = 3):
    print(n1, n3)

# the atributes that have a default value got be after those who dont have

n(1)

# se você tiver uma variavel fora do escopo de uma função e dps pegar
# ela e overwrite qndo sair do escopo da função ela volta pro valor normal

# module we can considere it a single python file

import math
# from math import sqrt, pi

math.sqrt(1)

import datetime

today = datetime.date.today()

import os

current_dir = os.getcwd()

import json

data = {'name': 'Elijah', 'salary': 10000}

json_string = json.dumps(data)

# pip install requests
# pip install requests==2.3.5
# pip install requests pandas math
# pip freeze > requirements.txt
# pip install -r requirements.txt

# requests .get() .json [] .keys()

# datatime.now() timedelta(days = 7) strftime('%m-%d-%Y')

# pd.DataFrame({
#   :
# })

# pd.to_datetime() data vem da API como string

# matplotlib biblioteca p criar graficos
# pyplot parte q tem comandos p criar graficos
# aí da p fzr matplot.pyplot convenção botar como plt

# os.path.exists

# ../../../

# Reading a CSV file - needs exact path
# with open("sales-analyses/data/sales.csv", "r") as file:
#     content = file.read()
# opens the file in 'r' read mode, theres the 'w' write
# a 'append' and then reading and storing the content
# in content
# nesse caso content é do tipo str uma string com
# o texto inteiro do arquivo
# nesse caso ta lendo as file

# Importing a module - Python searches for it
# import mymodule                    # Looks for mymodule.py
# from folder.utils import helper    # Looks for folder/utils.py

# 2 jeitos de importar modules o pyton msmo procura

# import sys
# print(sys.path)  # List of folders Python checks

# import sys

# # Add a folder to Python's search path
# sys.path.append("/path/to/my/folder")

# # Now you can import from that folder
# import mymodule

# import sys
# import os

# # Go up one level from current script
# parent = os.path.dirname(os.path.dirname(__file__))
# sys.path.append(parent)

# u can create a module put functions in there
# and then import those functions from this module

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

dog = Dog('dog', 'labrador')

class Tax:
    def __init__(self, tax, price):
        self.tax = tax
        self.price = price

    def calculate(self, product):
        # self.tax = 5
        # product = 10
        return self.tax + product

pj_programador = Tax(10000, 30000)
print(pj_programador.calculate(65000))

print('hi', end="")

n1 = int(input('hi'))
        

# lists r actually linked lista

# oq é cada coisa nesse git ignore

import os

api_key = os.environ.get('API_KEY')

database = os.environ,get('DATABASE_NAME', 'default.db')

from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv()
# inside the () u can specify the path

# Now use your variables
api_key = os.environ.get('API_KEY')
debug = os.environ.get('DEBUG')
# api_key = os.environ['API_KEY']

print(f"API Key: {api_key}")
print(f"Debug mode: {debug}")