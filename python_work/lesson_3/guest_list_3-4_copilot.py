def print_invitations(guest_list):
    for guest in guest_list:
        print(f'{guest.title()}, you have been cordially invited to my dinner.')

def remove_guest(guest_list, guest):
    if guest in guest_list:
        guest_list.remove(guest)
        print(f'\n{guest.title()} cannot make the dinner and sends their regards.\n')
    else:
        print(f'\n{guest.title()} is not in the guest list.\n')

def add_guest(guest_list, guest, position=None):
    if position is None:
        guest_list.append(guest)
    else:
        guest_list.insert(position, guest)

guest_list = ['grandparents', 'obama', 'george']
print_invitations(guest_list)

no_show = 'obama'
new_guest = 'biden'
remove_guest(guest_list, no_show)
add_guest(guest_list, new_guest, 1)
print_invitations(guest_list)

print('\nI have found a larger table!\n')
add_guest(guest_list, 'hideo', 0)
add_guest(guest_list, 'davinci', 3)
add_guest(guest_list, 'edison')
print_invitations(guest_list)

print('\nAmazon messed up my order and the larger table will not arrive on time! I can only invite two people for dinner.\n')
while len(guest_list) > 2:
    uninvited_guest = guest_list.pop()
    print(f'{uninvited_guest.title()}, you have been uninvited to my dinner. My deepest apologies!')

print_invitations(guest_list)

print('\nPsyke! You\'re all uninvited!\n')
guest_list.clear()
print(guest_list)