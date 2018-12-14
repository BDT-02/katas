import time
class Message:
    def __init__(self, from_number, time_arrived, text_of_sms):
        self.has_been_viewed = False
        self.from_number = from_number
        self.time_arrived = time_arrived
        self.text_of_sms = text_of_sms

    def get_time(self):
        return self.time_arrived

    def get_number(self):
        return self.from_number

    def get_text(self):
        return self.text_of_sms

    def set_viewed(self):
        self.has_been_viewed = True

    def check_read(self):
        return self.has_been_viewed


class SMS_Store:
    def __init__(self):
        self.list_ = []

    def add_new_arrival(self, from_number, time_arrived, text_of_sms):
        self.list_.append(Message(from_number, time_arrived, text_of_sms))

    def message_count(self):
        return len(self.list_)

    def get_unread_index(self):
        unread = []
        for (i, message) in enumerate(self.list_):
            if not message.check_read():
                unread.append(i)
        return unread

    def read_message(self, index):
        message_time = self.list_[index].get_time()
        from_number = self.list_[index].get_number()
        message_text = self.list_[index].get_text()
        self.list_[index].set_viewed()
        return 'Hour: '+ message_time + ' message:' + message_text + ' from:' +from_number

    def delete(self, index):
        self.list_.pop(index)

    def clear(self):
        self.list_.clear()


inbox = SMS_Store()
time_received = time.strftime("%D %T")
inbox.add_new_arrival('+59178589130', time_received, 'some nights i stay up')
# inbox.add_new_arrival(12, 5, 'cashing in my bad luck')
inbox.add_new_arrival(14, 7, 'somenights i call it a draw')
inbox.add_new_arrival(56, 0, 'somenights i wish that my lips could built a castle.')
print inbox.message_count()
print(inbox.get_unread_index())  # -> [0, 1, 2, 3]
print(inbox.read_message(0))  # -> some nights i stay up
# print(inbox.get_unread_index()) # -> [1, 2, 3]
# inbox.delete(3)
# print inbox.message_count()
