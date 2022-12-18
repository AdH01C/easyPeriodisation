import json
from src.data.constants import *
import os


def init():
    if os.path.exists("src/data/volumes.json"):
        return

    with open("src/data/exercises.txt") as f:
        exercise_list = [exercise.rstrip() for exercise in f]
    exercise_dict = dict()

    for exercise in exercise_list:
        exercise_dict[exercise] = [DEFAULT_ACCESSORY_MEV, DEFAULT_ACCESSORY_MRV, -1]

    # Write data to a JSON file
    with open("src/data/volumes.json", "w") as f:
        json.dump(exercise_dict, f)
