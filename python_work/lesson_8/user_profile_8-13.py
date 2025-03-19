# practice 2/1/25
# chapter 8 
# user profile

def build_profile(first, last, **user_info): # define function
    '''Build a dictionary containing everything we know about a user.'''
    '''Two parameters take strings. Third parameter creates dictionary of said name.'''
    user_info['first_name'] = first # value from parameters assinged to key
    user_info['last_name'] = last # value from parameters assigned to key
    return user_info # returns the dictionary

my_profile = build_profile('alex', 'flores',
                             location='reno',
                             field='programming',
                             level='beginner')
print(my_profile)