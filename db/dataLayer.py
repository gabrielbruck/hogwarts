import pymongo
from bson import ObjectId
from model.user import User


class DataLayer:
    def __init__(self):
        self.__client = pymongo.MongoClient('localhost', 27017)
        self.__db = self.__client["hogwarts"]

    def get_student(self, first_name):
        user_dict = self.__db.student.find_one({"first_name": first_name})
        user = self.create_user_from_dict(user_dict)
        return user

    def get_existing_skill(self, skill):
        user_dict = self.__db.student.find_one({"existing_skills": {skill}})
        user = self.create_user_from_dict(user_dict)
        return user

    # create user from dict
    def create_user_from_dict(self, user_dict):
        user = User(user_dict['_id'], user_dict['first_name'], user_dict['last_name']
                    , user_dict['creation_time'], user_dict['update_time'],
                    user_dict['existing_skills'], user_dict['desired_skills'], user_dict['courses']
                    )
        return user

