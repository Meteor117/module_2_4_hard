def get_pair(n, i, j):
    pair_sum = i + j
    if n % pair_sum == 0:
        pair_str = f"{i}{j}"
        return pair_str
    else:
        return ""# пустая строка

def generate_password (n):
    result = ""
    for i in range (1, 21):
        for j in range (i+1, 21):
            result += get_pair (n, i, j)
    return result

for test_number in range (3, 21):
    password = generate_password (test_number)
    print(f"{test_number}-{password}")

