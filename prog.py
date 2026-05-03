import pandas as pd

df = pd.read_csv('book_recommendation_dataset.csv')

df.head()
print(df['author'].unique)
print(" ")
aaaa = df['category'].unique


aaaa.value_count()






# df.info()

# This class will handle taking the username and information
class User:
    def __init__(self):
        self.username = username = input("Please enter your Name: " )
        self.email = email = input("Please enter your E-mail: " )
        self.contact = contact = input("Please enter your contact: " )

        return
    
# rrrrr = User()
# print(rrrrr.email)
 


#  This class will handle collecting of preferences for the user 
class Preferences:

    def __init__(self, author, category, rating):
        self.author = author
        self.category = category
        self.rating = input("Please enter your Book Rating between 1 and 5: " )
    






# This class will make recommendation based on the users preferences
class Recommender():

    def __init__(self, )

    
    
    pass




def main():
    

    pass





if __name__ == "__main__":
    main()
