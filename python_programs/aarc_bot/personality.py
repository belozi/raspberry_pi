import dictionary

def greeting():

# This method sets the class variables for the current manager

print('Hello!')
print("I am RILO, the social media robot reporter")
print("for the Auburn Avenue Research Company")
name = input("Please enter your name:  ")
user_type = input("Are you a current user? y/n: ")

if user_type == "y":

    while pa
  password = input("Password: ")

  if password == self.password:
    research()

else:
  password = input("Please enter a new password:\n")

print("Good %(day_time)s, %(name)s!")
#print("You have %(schedule)s on the schedule for the day" % {"schedule": schedule})
mood = input("How are you doing?\n")

print(name, mood)



def research():
keywords = []
raw = input('What are you working on today?\n')
print(raw)
