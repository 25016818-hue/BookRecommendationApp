import pandas as pd

df = pd.read_csv('book_recommendation_dataset.csv')

print(df.head())
print(df['author'].unique)
print(" ")
aaaa = df['category'].unique


#aaaa.value_count()






# df.info()

# This class will handle taking the username and information
class User:
    def __init__(self):
        self.username = username = input("Please enter your Name: " )
        self.email = email = input("Please enter your E-mail: " )
        self.contact = contact = input("Please enter your contact: " )

        return
""" 
rrrrr = User()
print(rrrrr.email)
"""


#  This class will handle collecting of preferences for the user 
class Preferences:

    def __init__(self):
        self.author = ""
        self.category = ""
        self.rating = ""    

    def collect_preferences(self):
        self.author = input("Please Enter your prefered author: ")
        self.category = input("Please Enter your prefered category: ")
        self.rating = input("Please Enter your prefered rating between 1 and 5: " )

    def display_preferences(self):
        print("\nUser Preferences")
        print("----------------- You have selected -----------------")
        print(f"author: {self.author}")
        print(f":category {self.category}")
        print(f":rating {self.rating}")


bb = Preferences()
bb.collect_preferences()




# This class will make recommendation based on the users preferences
class Recommender():

    def __init__(self, ):
        pass

    pass




def main():
    

    pass





if __name__ == "__main__":
    main()
