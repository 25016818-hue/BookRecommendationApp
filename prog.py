import pandas as pd

df = pd.read_csv('book_recommendation_dataset.csv')

df.head()
print(df['author'].unique)
print(" ")
print(df['category'].unique)

# df.info()

# This class will handle taking the username and information
class User():
    def __init__(self, username, email, contact):
        self.username = username
        self.email = email
        self.contact = contact    



class Preferences():

    
    #  This class will handle collecting of preferences for the user

    pass





class Recommender():

    # This class will make recommendation based on the users preferences
    
    pass




def main():
    

    pass





if __name__ == "__main__":
    main()
