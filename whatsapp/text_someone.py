import pywhatkit

# Send message to a contact
phone_number = input("Enter phone number: ")

# pywhatkit.sendwhatmsg(phone_number, "Test", 7, 21)
# message, time in hour send, time in min send, wait 
# time(seconds you have to wait untill delivered), 
# when we want to close the tab, then the time to wait untill delivered
pywhatkit.sendwhatmsg(phone_number, "Test", 7, 25, 15, True, 2)

# Send message to a group
#group id is in the info section then invite using link
group_id = input("Enter group id: ")

pywhatkit.sendwhatmsg_to_group(group_id, "Test Group", 7, 31)
