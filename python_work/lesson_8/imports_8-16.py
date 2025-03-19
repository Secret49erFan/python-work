# practice 2/2/25
# chapter 8
# imports
import cars8_14 # use this style when importing all functions
# from cars8_14 import request_car
# from cars8_14 import request_car as rc # use this style when importing only certain functions
# import cars8_14 as car
# from cars8_14 import * # dont do this style if possible
my_car = cars8_14.request_car('toyota', '4runner',
                      color='charcol',
                      trim='special edition',
                      year=2023)
print('\nThank you for requesting a vehicle through our agency. Please review the car details for accuracy.')
for k, v in my_car.items():
    if not isinstance(v, int):
        print(f'\t{k.title()}: {v.title()}.')
    else:
        print(f'\t{k.title()}: {v}.')