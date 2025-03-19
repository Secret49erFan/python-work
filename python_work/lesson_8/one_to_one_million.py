# DEFINING FUCNTIONS #
# 1/20/25 #

def sum_all_numbers_from_one_to_one_million():
    numbers = range(0, 1_000_000) # CREATE A LIST WITH ALL THE NUMBERS FROM ONE TO A MILLION #
    total_sum = 0 # INITIATE THE TOTAL #
    for number in numbers: # LOOP THROUGH ALL THE NUMBERS IN THE NUMBERS LIST (ONE THRU A MILLION) #
        total_sum += number # ADD THE TOTAL_SUM TO THE CURRENT NUMBER (total_sum = total_sum + number) #
    return total_sum

print(sum_all_numbers_from_one_to_one_million()) # SPIT IT OUT TO THE TERMINAL #