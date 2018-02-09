# Importing datetime to display the chat time and date
from datetime import datetime

# made a class for spy
class Spy:

  def __init__(self, name, salutation, age, rating):
    self.name = name
    self.salutation = salutation
    self.age = age
    self.rating = rating
    self.is_online = True
    self.chats = []
    self.current_status_message = None


# a class for chat_messages
class ChatMessage:

    def __init__(self, message, sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me


spy = Spy('Pankaj', 'Mr.', 22, 5.0)

friend_one = Spy('Pranav', 'Mr.', 27, 4.9)
friend_two = Spy('sumit', 'Mr.', 35, 3.0)
friend_three = Spy('ram', 'Mr.', 37, 5.5)

# List of friends
friends = [friend_one, friend_two, friend_three]
