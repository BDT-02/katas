# Create a new class, SMS_store. The class will instantiate SMS_store objects, similar to an inbox
# or outbox on a cellphone:
# 	my_inbox = SMS_store()
# This store can hold multiple SMS messages (i.e. its internal state will just be a list of messages).
# Each message will be represented as a tuple:
# 	(has_been_viewed, from_number, time_arrived, text_of_SMS)
# The inbox object should provide these methods:
# 	my_inbox.add_new_arrival(from_number, time_arrived, text_of_SMS)
# 		# Makes new SMS tuple, inserts it after other messages
# 		 # in the store. When creating this message, its # has_been_viewed status is set False.
# 	my_inbox.message_count()
#  		# Returns the number of sms messages in my_inbox
# 	my_inbox.get_unread_indexes()
# 		# Returns list of indexes of all not-yet-viewed SMS messages
# 	my_inbox.get_message(i)
# 		# Return (from_number, time_arrived, text_of_sms) for message[i]
# 		# Also change its state to "has been viewed".
# 	 	# If there is no message at position i, return None
# 	my_inbox.delete(i) # Delete the message at index i
#   my_inbox.clear() # Delete all messages from inbox
#
# Write the class, create a message store object, write tests for these methods, and implement the methods.
#************************************************************************************************************
from datetime import datetime
class Message:
    def __init__(self, from_number, time_arrived, text_of_sms):
        self.has_been_viewed = False
        self.from_number = from_number
        self.time_arrived = time_arrived
        self.text_of_sms = text_of_sms

    def get_number(self):
        return self.from_number

    def get_time(self):
        return self.time_arrived

    def get_text(self):
        return self.text_of_sms

    def set_viewed(self):
        self.has_been_viewed = True

    def check_read(self):
        return self.has_been_viewed


class SMS_Store:
    def __init__(self):
        self.list = []

    def add_new_arrival(self, from_number, time_arrived, text_of_sms):
        # Makes new SMS tuple, inserts it after other messages
        # in the store. When creating this message, its # has_been_viewed status is set False.
        self.list.append(Message(from_number, time_arrived, text_of_sms))

    def message_count(self):
        # Returns the number of sms messages in my_inbox
        return len(self.list)

    def get_unread_index(self):
        # Returns list of indexes of all not-yet-viewed SMS messages
        unread = []
        for (i, message) in enumerate(self.list):
            if not message.check_read():
                unread.append(i)
        return unread

    def read_message(self, index):
        # Return (from_number, time_arrived, text_of_sms) for message[i]
        #  Also change its state to "has been viewed".
        #  If there is no message at position i, return None
        number = self.list[index].get_number()
        time1 = self.list[index].get_time()
        message_text = self.list[index].get_text()
        self.list[index].set_viewed()
        print(str(number) + ' ' + time1 + ' ' + message_text)

    def delete(self, index):
        # Delete the message at index i
        self.list.pop(index)

    def clear(self):
        # Delete all messages from inbox
        self.list.clear()

date = datetime.today().strftime("%d-%m-%y %I:%m %p")
print(date)
inbox = SMS_Store()
inbox.add_new_arrival(67598562, date, 'This a first message')
inbox.add_new_arrival(67500236, '10/01/2018 10:30', 'This a second message')
inbox.add_new_arrival(67525984, '28/08/2018 22:30', 'This a third message')
print(inbox.get_unread_index())  # -> [0, 1, 2]
print(inbox.read_message(2))     # -> This a third message
print(inbox.get_unread_index())  # -> [0, 1]
inbox.delete(0)
print(inbox.get_unread_index())
inbox.clear()
print(inbox.get_unread_index())
