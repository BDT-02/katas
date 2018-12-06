from src.yury.taskLesson3 import get_url, replace_text, fill_list, show_list, count_repetitions_alphabet

text = "url http://fundacion.com and other url http://jalasoft.com "
assert ['http://fundacion.com', 'http://jalasoft.com'] == get_url(text)

assert "yury OrtunO" == replace_text("yury ortuno", "o", "O")

list = fill_list()
show_list(list)

assert {'y': 3, 'e': 1, 'r': 2, 'u': 1, 'v': 1} == count_repetitions_alphabet("yury yver")
