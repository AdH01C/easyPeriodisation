def round_plate(weight, unit=2.5):
    return weight // unit * unit


def generate_day(program, volumes, week_no, day, exercise, top_set, back_off, no_sets):
    program[week_no][day][exercise] = list()
    top_set_scheme = f"{round_plate(top_set * volumes[exercise][2])} x 8"
    back_off_scheme = f"{round_plate(back_off * volumes[exercise][2])} x 8"
    program[week_no][day][exercise].append(top_set_scheme)
    for i in range(no_sets - 1):
        program[week_no][day][exercise].append(back_off_scheme)

    return program[week_no][day]


def generate_week(program, volumes, week_no, squat, squat_sets, bench, bench_sets, deadlift, deadlift_sets, top_set,
                  back_off):
    # Bench
    program[week_no][1] = generate_day(program, volumes, week_no, 1, bench, top_set, back_off, bench_sets)

    # Squat
    program[week_no][2] = generate_day(program, volumes, week_no, 2, squat, top_set, back_off, squat_sets)

    # Deadlift
    program[week_no][3] = generate_day(program, volumes, week_no, 3, deadlift, top_set, back_off, deadlift_sets)

    return program[week_no]


def generate(volumes, squat, bench, deadlift):
    program = dict()
    for weeks in range(1, 4):
        program[weeks] = dict()
        for days in range(1, 4):
            program[weeks][days] = dict()

    squat_mev, squat_mrv, squat_max = volumes[squat]
    bench_mev, bench_mrv, bench_max = volumes[bench]
    deadlift_mev, deadlift_mrv, deadlift_max = volumes[deadlift]

    program[1] = generate_week(program, volumes, 1, squat, squat_mev, bench, bench_mev, deadlift, deadlift_mev, 0.7,
                               0.6)
    program[2] = generate_week(program, volumes, 2, squat, squat_mev + 1, bench, bench_mev + 1, deadlift,
                               deadlift_mev + 1, 0.65, 0.65)
    program[3] = generate_week(program, volumes, 3, squat, squat_mev + 2, bench, bench_mev + 2, deadlift, deadlift_mev + 2,
                               0.8, 0.65)
    return program
