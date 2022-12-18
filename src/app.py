import src.generate_hypertrophy_block as h
import src.generate_strength_block as s
import src.generate_peaking_block as p
from src.data.constants import *


def display_program(program):
    for week in program.keys():
        print(f"Week: {week}")
        print("#"*7)
        for day in program[week].keys():
            print(f"Day: {day}")
            print(program[week][day])


def get_input():
    return input("""
1. Search exercise list and modify MEV/MRV
2. Generate Hypertrophy Block
3. Generate Strength Block
4. Generate Peaking Block
5. Generate Full Training Cycle (6 months)
Enter: """)


def search_exercise(exercises, s):
    output = list()
    for exercise in exercises:
        if s.lower() in exercise.lower():
            output.append(exercise)
    return output


def get_exercise(exercises):
    search_input = input("Exercise search: ")
    results = search_exercise(exercises, search_input)
    for i, item in enumerate(results):
        print(f"{i + 1}. {item.rstrip()}")
    if len(results) == 0:
        print("None found.")
        return
    exercise_no = int(input("Option: ")) - 1
    return results[exercise_no]


def modify_exercise(exercises, volumes):
    exercise = get_exercise(exercises)
    mev, mrv, rep_max = volumes.get(exercise)
    print(f"MEV: {mev}\nMRV: {mrv}\nMax: {rep_max}")
    mod = input("Modify (y/N)? : ")
    if mod == "y":
        mev = int(input("MEV: "))
        mrv = int(input("MRV: "))
        rep_max = int(input("Max: "))
        volumes[exercise] = [mev, mrv, rep_max]


def run(volumes):
    exercises = list(volumes.keys())
    print("""   
_____
| ____|__ _ ___ _   _
|  _| / _` / __| | | |
| |__| (_| \__ \ |_| |
|_____\__,_|___/\__, |
                |___/
 ____           _           _ _           _   _
|  _ \ ___ _ __(_) ___   __| (_)___  __ _| |_(_) ___  _ __
| |_) / _ \ '__| |/ _ \ / _` | / __|/ _` | __| |/ _ \| '_ 
|  __/  __/ |  | | (_) | (_| | \__ \ (_| | |_| | (_) | | | |
|_|   \___|_|  |_|\___/ \__,_|_|___/\__,_|\__|_|\___/|_| |_|

By AdH01c""")
    option = ""
    while option != "quit":
        option = get_input()
        if option == '1':
            modify_exercise(exercises, volumes)
        elif option == '2':
            print("Choose main squat movement.")
            squat = get_exercise(exercises)
            squat_max = int(input("Enter 1rm: "))
            volumes[squat] = [DEFAULT_SQUAT_MEV, DEFAULT_SQUAT_MRV, squat_max]

            print("Choose main bench movement.")
            bench = get_exercise(exercises)
            bench_max = int(input("Enter 1rm: "))
            volumes[bench] = [DEFAULT_BENCH_MEV, DEFAULT_BENCH_MRV, bench_max]

            print("Choose main deadlift movement.")
            deadlift = get_exercise(exercises)
            deadlift_max = int(input("Enter 1rm: "))
            volumes[deadlift] = [DEFAULT_DEADLIFT_MEV, DEFAULT_DEADLIFT_MRV, deadlift_max]

            display_program(h.generate(volumes, squat, bench, deadlift))
        elif option == '3':
            s.generate(volumes)
        elif option == '4':
            p.generate(volumes)
        else:
            print("Invalid input.")
            option = get_input()
