import datetime


def get_number_of_laps(duration, lap_time):
    seconds = get_seconds_from_lap_time(lap_time)
    print("Duration: ", duration)
    print("Seconds: ", seconds)
    return (duration * 60) / seconds


def get_fuel(number_of_laps, fuel_per_lap):
    return number_of_laps * fuel_per_lap


def get_seconds_from_lap_time(lap_time):
    splits = lap_time.split(":")
    return datetime.timedelta(
        minutes=int(splits[0]), seconds=int(splits[1]), milliseconds=int(splits[2])
    ).total_seconds()
