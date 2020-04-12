import random

# Practice 1 Random Numbers
my_randoms = list()
for i in range(10):
    my_randoms.append(random.randrange(1, 6))

numbers_1_to_10 = range(1, 11)

for number in numbers_1_to_10:
    the_numbers_match = False

    for i in my_randoms:
        if i == number:
            the_numbers_match = True
    if the_numbers_match == True:
        print(f'{number} is in the list')
    else:
        print(f'{number} is not in the list')

