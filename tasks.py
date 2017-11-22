# Imports
import datetime

from peewee import *


db = SqliteDatabase('work_logs.db')
time_format = ('%m/%d/%y')


class Tasks(Model):
    employee = CharField(max_length=255)
    task_name = CharField(max_length=255)
    time_elapsed = CharField(max_length=255)
    notes = TextField()
    timestamp = DateTimeField(default=datetime.datetime.now)
    date = datetime.datetime.today().strftime(time_format)

    class Meta:
        database = db


def initialize():
    '''Create the database and the table if they do not exist'''
    db.connect()
    db.create_tables([Tasks], safe=True)
