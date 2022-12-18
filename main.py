import json
import src.init_exercises as exercises
import src.app as app


def init():
    print("Initialising exercises...")
    try:
        exercises.init()
        print("Initialised.")
    except FileNotFoundError as e:
        print(e.filename, "not found.")


if __name__ == '__main__':
    init()
    with open("src/data/volumes.json") as f:
        volumes = json.load(f)

    volumes = app.run(volumes)

    # Save modified
    with open("src/data/volumes.json", "w") as f:
        json.dump(volumes, f)
