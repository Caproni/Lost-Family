"""
author: Edmund Bennett
"""

from peewee import Model, TextField, BlobField


class Character(Model):

    character_id = TextField()
    first_name = TextField()
    middle_names = TextField()
    family_name = TextField()
    date_of_birth = TextField()
    date_of_death = TextField()
    image_one = BlobField()
    image_two = BlobField()
    image_three = BlobField()
    mother_id = TextField()
    father_id = TextField()
    description = TextField()
    birth_certificate_id = TextField()
    marriage_certificate_ids = TextField()
    divorce_certificate_ids = TextField()

    class Meta:
        pass


if __name__ == "__main__":
    pass

