# PRACTICE 2/1/25 #
# CHAPTER 8 - MESSAGES #

sent_messages = [] # INITIATE EMPTY LIST #
halo_messages = [ # LIST OF SHORT MESSAGES #
    'i need a weapon',
    'wake me when you need me',
    'were it so easy',
    'dont make a girl a promise if you know you cant keep it',
    'i am a monument to all your sins',
    'there are those who said this day would never come what are they to say now',
    'you are all of you vermin',
]


def send_messages(list_of_messages):
    ''' MOVES ITEMS FROM A LIST, PRINTS THE ITEM TO CONSOLE, AND MOVE TO NEW LIST. SINGLE ARG (LIST). '''
    while list_of_messages: # LOOP THRU LIST UNTIL EMPTY #
        sending_message = list_of_messages.pop() # REMOVE LAST ITEM ON PASSED LIST AND LABEL IT #
        print(f'Sending: {sending_message.capitalize()}.') # CONSOLE OUTPUT WITH CAPATALIZATION OF REMOVED ITEM #
        sent_messages.append(sending_message) # ADDS SENT ITEM TO NEW LIST #
#    for message in list_of_messages: # LOOP THRU MESSAGES #
#        working_message = message.pop() # REMOVE LAST ITEM ON PASSED LIST AND LABEL IT #
#        print(f'Sending: {working_message.capitalize()}.') # CONSOLE OUTPUT WITH CAPATALIZATION OF REMOVED ITEM #
#        sent_messages.append(message) # ADDS WORKING ITEM TO NEW LIST #

send_messages(halo_messages[:]) # CALL FUNCTION AND PASS LIST AS SLICE/COPY #
print(sent_messages) # PRINT TO MAKE SURE ITEMS WERE MOVED #
print(halo_messages) # ORIGINAL LIST RETAINS ITEMS #