import json


class User:

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)

    def __init__(self, user_id, first_name, last_name, creation_time, update_time, existing_skills,
                 desired_skills, courses):

        self.user_id = str(user_id)
        self.first_name = first_name
        self.last_name = last_name
        self.creation_time = str(creation_time)
        self.update_time = str(update_time)
        self.existing_skills = existing_skills
        self.desired_skills = desired_skills
        self.courses = courses

