from src.yury.taskLesson2 import determine_number_odd_or_even, determine_number_is_prime, area_of_circle, sum_to, \
    days_in_month

assert "odd" == determine_number_odd_or_even(5)
assert "odd" == determine_number_odd_or_even(7)
assert "even" == determine_number_odd_or_even(6)
assert "even" == determine_number_odd_or_even(10)

assert [2, 3, 5, 7] == determine_number_is_prime(2, 7)
assert [11, 13] == determine_number_is_prime(8, 15)

assert 380.13 == area_of_circle(11)
assert 530.93 == area_of_circle(13)

assert 55 == sum_to(10)
assert 35 == sum_to(40)

assert 31 == days_in_month('january')
assert 28 == days_in_month('february')
assert 31 == days_in_month('august')
