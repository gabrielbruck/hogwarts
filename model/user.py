import json


class User:

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)

    def __init__(self, user_id, first_name, last_name, creation_time, last_updating_time, existing_magical_skills,
                 desired_magical_skills, interested_in_course):

        self.user_id = str(user_id)
        self.first_name = first_name
        self.last_name = last_name
        self.creation_time = str(creation_time)
        self.last_updating_time = str(last_updating_time)
        self.existing_magical_skills = existing_magical_skills
        self.desired_magical_skills = desired_magical_skills
        self.interested_in_course = interested_in_course
