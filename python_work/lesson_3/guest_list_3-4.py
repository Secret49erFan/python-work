#12/15/24
#practice for chapeter 3 'lists'

gst_lst = ['grandparents', 'obama', 'george'] #populate list with names
for gsts in gst_lst:
    print(f'{gsts.title()}, you have been cordially invited to my dinner.') #anounce the invitations

# // ---- COULD PROBABLY PUT ALL THIS IN A FUNTION
#msg1 = f'{gst_lst[0].title()}, you have been cordially invited to my dinner.' #set fist message
#msg2 = f'{gst_lst[1].title()}, you have been cordially invited to my dinner.' #set second message
#msg3 = f'{gst_lst[2].title()}, you have been cordially invited to my dinner.' #set third message
#print(msg1)
#print(msg2)
#print(msg3)
#print(' ')
#/ // ---- THIS ^^^

no_show = gst_lst[1] #set the guest whom can not make dinner
new_gst = 'biden' #set the new guest
gst_lst.remove(no_show) # remove the no show from the list
gst_lst.insert(1, new_gst)
print(f'\n{no_show.title()} cannot make the diner and sends their regards.\n') # no show msg
for gsts in gst_lst:
    print(f'{gsts.title()}, you have been cordially invited to my dinner.') #anounce the new invitations

# // ---- COULD PROBABLY PUT ALL THIS IN A FUNTION
#msg1 = f'{gst_lst[0].title()}, you have been cordially invited to my dinner.' #set fist message
#msg2 = f'{gst_lst[1].title()}, you have been cordially invited to my dinner.' #set second message
#msg3 = f'{gst_lst[2].title()}, you have been cordially invited to my dinner.' #set third message
#anounce the invitations VVVVVV
#print(msg1)
#print(msg2)
#print(msg3)
#/ // ---- THIS ^^^

print('\nI have found a larger table!\n') #anounce the bigger table

gst_lst.insert(0, 'hideo') #adding new guests
gst_lst.insert(3, 'davinci') #adding new guests
gst_lst.append('edison') #adding new guests

for gsts in gst_lst:
    print(f'{gsts.title()}, you have been cordially invited to my dinner.') #anounce the new invitations

#msg1 = f'{gst_lst[0].title()}, you have been cordially invited to my dinner.' #set fist message
#msg2 = f'{gst_lst[1].title()}, you have been cordially invited to my dinner.' #set second message
#msg3 = f'{gst_lst[2].title()}, you have been cordially invited to my dinner.' #set third message
#msg4 = f'{gst_lst[3].title()}, you have been cordially invited to my dinner.' #set forth message
#msg5 = f'{gst_lst[4].title()}, you have been cordially invited to my dinner.' #set fifth message
#msg6 = f'{gst_lst[5].title()}, you have been cordially invited to my dinner.' #set sixth message
#anounce the invitations VVVVVV
#print(msg1)
#print(msg2)
#print(msg3)
#print(msg4)
#print(msg5)
#print(msg6)

print('\nAmazon fucked up my order and the larger table will not arrive on time! I can only invite two people for dinner.\n')

while len(gst_lst) > 2: # THIS IS A WHILE LOOP; GETTING AHEAD OF MYSELF LOL
    uninvited_gst = gst_lst.pop() # pop the gst out and label them uninvited_gst
    print(f'{uninvited_gst.title()}, you have been uninvited to my dinner. My deepest appologies!')

print ('\n')

#remove gst 1/4 //----------->
#for gsts in gst_lst[:4]: # slice of the first 4 items in the list
#    uninvited_gst = gst_lst.pop() # looop through each item and pop it off
#    print(f'{uninvited_gst.title()}, you have been ramdonly been uninvited to my dinner. My deepest appologies!') # print to console
#uninvited_gst = gst_lst.pop()
#print(f'{uninvited_gst.title()}, you have been ramdonly been uninvited to my dinner. My deepest appologies!') 
#remove gst 2/4 //----------->
#uninvited_gst = gst_lst.pop()
#print(f'{uninvited_gst.title()}, you have been ramdonly been uninvited to my dinner. My deepest appologies!') 
#remove gst 3/4 //----------->
#uninvited_gst = gst_lst.pop()
#print(f'{uninvited_gst.title()}, you have been ramdonly been uninvited to my dinner. My deepest appologies!') 
#remove gst 4/4 //----------->
#uninvited_gst = gst_lst.pop()
#print(f'{uninvited_gst.title()}, you have been ramdonly been uninvited to my dinner. My deepest appologies!') 

for gsts in gst_lst:
    print(f'{gsts.title()}, you are still invited to the dinner.')

#print(f'\n{gst_lst[0].title()}, you are still invited to the dinner.') # first guest remaining
#print(f'{gst_lst[1].title()}, you are still invited to the dinner.') # second guest remaining
# ending this program

print('\nPsyke! You\'re all uninvited!\n')

#del gst_lst[0] # remove first element
#del gst_lst[0] # remove second element

del gst_lst[:]
print(gst_lst)