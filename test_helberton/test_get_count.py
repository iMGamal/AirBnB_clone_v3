#!/usr/bin/python3
""" Test .get() and .count() methods
"""
from models import storage
from models.state import State
from models.place import Place

print("All objects: {}".format(storage.count()))
print("State objects: {}".format(storage.count(State)))
print("Place objects: {}".format(storage.count(Place)))

first_state_id = list(storage.all(State).values())[0].id
print("First state: {}".format(storage.get(State, first_state_id)))
