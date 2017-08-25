import turtle
import math

class User:
    class_counter = 0
    def __init__(self, user_name, user_id):
        #recommended attributes
        self.user_name = user_name
        self.user_id = user_id
        self.connections = []
        self.id= User.class_counter
        User.class_counter += 1

    def addConnection(self, connection_id):
        self.connection_id = connection_id

    def getUserName(self):
        return self.username

    def getConnections(self):
        return self.connection_id

    def getUserID(self):
        return self.user_id
class Network:
    def __init__(self):
        self.users = []

    def numUsers(self):
        #returns the number of users in the network
        return len(self.users)

    def addUser(self, username):
        # creates a new user, assigns them an ID
        # and adds them to the network
        user_id
        newUser = User(user_name, user_id)
        user_id = len(self.users)+1
        (self.users).append(newUser)

    def getUserID(self, username):
        #returns the user id when given the users username
        return self.user_id
    def addConnection(self, user1, user2):
        #This function
        # 1) gets the user ids of user1 and user2
        # 2) checks to see if these users are already connected
        # 3) If theyre not, adds user1 to user2's connections and viceversa

    def printUsers(self):
        #BONUS
        #this function goes through the users in the network and prints them
        return self.users


    def printConnections(self, username):
        #BONUS
        #This function takes in a username, finds the corresponding user, and
        #then prints that users connections
