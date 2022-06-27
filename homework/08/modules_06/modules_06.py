my_str = 'aaaaaaadssadsaaacxz'
last_char = ''
current_seq_len = 0
max_seq_len = 0
longest_str = ''

for c in my_str:
    if c == last_char:
        current_seq_len += 1
        if current_seq_len > max_seq_len:
            longest_str += last_char
            max_seq_len = current_seq_len
    else:
        current_seq_len = 1
        last_char = c



print(max_seq_len, longest_str)