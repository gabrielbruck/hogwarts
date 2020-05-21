import datetime
import pprint
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['hogwarts']
collection = db['student']

magic_skills = ['Animagi', 'Metamorphmagi',
                'Parseltongue', 'Seers',
                'Legilimency and Occlumency',
                'Apparition and Disapparition',
                'Teleportation', 'Veela Charm',
                'Magical Resistence']

all_courses = ['Transfiguration',
               'Defence Against the Dark Arts',
               'Charms', 'Potion', 'Astronomy',
               'History of Magic', 'Herbology',
               'Arithmancy', 'Study of Ancient Runes',
               'Divination', 'Care of Magical Creatures',
               'Muggle Studies', 'Alchemy', 'Flying',
               'Apparition']

student = {"first_name": "Ben",
           "last_name": "Ron",
           "creation_time": datetime.datetime.now(),
           "update_time": datetime.datetime.now(),
           "existing_skills": {magic_skills[6]: 5, magic_skills[8]: 4},
           "desired_skills": {magic_skills[2]: 2},
           "courses": [all_courses[1], all_courses[3],   all_courses[5], all_courses[6]]
           }

user_id = collection.insert_one(student)

pprint.pprint(user_id)
