def int_func(text):
    length = len(text)
    first = text[0].upper()
    last = text[1:length].lower()
    text_new = first + last
    return str(text_new)

string_text = 'пика черва бубна трефа'

raw = string_text.split(' ')
length_list = len(raw)
i = 0
new_text = []
while i < (length_list):
    el = raw[i]
    el_change = str(int_func(el))
    new_text.append(el_change)
    i += 1
new_string = ' '.join(new_text)


print(new_string)
