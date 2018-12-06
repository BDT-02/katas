from src.yury.taskLesson4Convertions import convert_age_to_minutes, convert_minutes_to_day

assert 525600 == convert_age_to_minutes(1)
assert 1051200 == convert_age_to_minutes(2)

assert 1 == convert_minutes_to_day(1440)
assert 2 == convert_minutes_to_day(2880)
