def count_digit(num):
    count = 0

    while num > 0:
     count += 1
     num = num // 10

    return count

print(count_digit(547386))
