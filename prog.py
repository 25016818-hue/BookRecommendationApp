import pandas as pd
import os

df = pd.read_csv('book_recommendation_dataset.csv')

# print(df.head())
# print(df['author'].unique)
# print(" ")
# aaaa = df['category'].unique
#aaaa.value_count()

# df.info()

# This class will handle taking the username and information
class User:
    def __init__(self):
        self.username = input("Please enter your Name: " )
        self.email = input("Please enter your E-mail: " )
        self.contact = input("Please enter your contact: " )
        return


#  This class will handle collecting of preferences for the user 
class Preferences:

    def __init__(self):                       
        # Create 1-based index maps for unique authors and categories
        self.authors_map = {i + 1: author for i, author in enumerate(sorted(df['author'].unique()))}
        self.categories_map = {i + 1: cat for i, cat in enumerate(sorted(df['category'].unique()))}
        
        # Updated to lists to store multiple choices
        self.author = []
        self.category = []
        self.rating = ""    

    def display_grid(self, items_map, columns=5, width=30):
        """Helper method to format and display a map as a clean grid layout."""
        items_list = list(items_map.items())
        for i in range(0, len(items_list), columns):
            row_items = items_list[i:i+columns]
            grid_row = "".join(f"[{idx}] {item}".ljust(width) for idx, item in row_items)
            print(grid_row)

    def parse_multiple_inputs(self, input_string, items_map):
        """Helper method to parse, validate, and extract multiple unique inputs."""
        # Split by comma and strip empty spaces
        raw_indices = [x.strip() for x in input_string.split(",")]
        
        selected_items = []
        for raw_idx in raw_indices:
            if not raw_idx:  # Skip empty splits from trailing commas
                continue
            try:
                idx = int(raw_idx)
                if idx in items_map:
                    # Prevent duplicates if user types the same number twice
                    if items_map[idx] not in selected_items:
                        selected_items.append(items_map[idx])
                else:
                    print(f"-> Warning: Index '{idx}' is out of range and will be ignored.")
                    return None
            except ValueError:
                print(f"-> Error: '{raw_idx}' is not a valid number.")
                return None
                
        if not selected_items:
            print("-> Error: You must choose at least one selection.")
            return None
            
        return selected_items

    def collect_preferences(self):
        # 1. Show all authors in a grid and get multiple selections
        print("\n----------------- AVAILABLE AUTHORS -----------------")
        self.display_grid(self.authors_map, columns=5, width=30)
            
        while True:
            user_input = input("\nEnter preferred author numbers separated by commas (e.g., 1, 4, 12): ")
            selections = self.parse_multiple_inputs(user_input, self.authors_map)
            if selections is not None:
                self.author = selections
                break

        # 2. Show all categories in a grid and get multiple selections
        print("\n----------------- AVAILABLE CATEGORIES -----------------")
        self.display_grid(self.categories_map, columns=4, width=35) # Slightly wider columns for longer names
            
        while True:
            user_input = input("\nEnter preferred category numbers separated by commas (e.g., 2, 5): ")
            selections = self.parse_multiple_inputs(user_input, self.categories_map)
            if selections is not None:
                self.category = selections
                break

        # 3. Get the rating selection between 1 and 5
        while True:
            try:
                rating_input = float(input("\nPlease Enter your preferred rating between 1 and 5: "))
                if 1 <= rating_input <= 5:
                    self.rating = str(rating_input)
                    break
                else:
                    print("Rating must be between 1 and 5.")
            except ValueError:
                print("Please enter a valid numeric value.")

    def display_preferences(self):
        print("\nUser Preferences")
        print("----------------- YOU HAVE SELECTED -----------------")
        # Joining list arrays into comma-separated strings for clean terminal presentation
        print(f"author(s): {', '.join(self.author)}")
        print(f"category(ies): {', '.join(self.category)}")
        print(f"rating: {self.rating}")


    

# This class will make recommendation based on the users preferences
class Recommender:
    def __init__(self, dataframe):
        self.df = dataframe
        self.recommendations = pd.DataFrame()

    def recommend_books(self, preferences):

        filtered_df = self.df.copy()

        #filter authors
        filtered_df = filtered_df[
            filtered_df['author'].isin(preferences.author)
            ]
        
        #filter categories
        filtered_df = filtered_df[
            filtered_df['category'].isin(preferences.category)
        ]

        # filter ratings
        filtered_df = filtered_df[
            filtered_df['rating'] >= float(preferences.rating)
        ]

        #sort hightest rating first
        filtered_df = filtered_df.sort_values(
            by='rating', ascending=False
            )
        
        self.recommendations = filtered_df

        def display_recommendations(self):

            print("\n----------------- RECOMMENDED BOOKS -----------------")
            if self.recommendations.empty:
                print("No recommendations found based on your preferences.")
                return
            
            for _, row in self.recommendations.iterrows():
                print(f"Title: {row['title']}, Author: {row['author']}, Category: {row['category']}, Rating: {row['rating']}")

        def save_to_text_file(self, user, preferences):
            filename = f"{user.username}_recommendations.txt"
            with open(filename, 'w', encoding = "utf-8") as file:
                file.write(f"User: {user.username}\n")
                file.write(f"Email: {user.email}\n")
                file.write(f"Contact: {user.contact}\n\n")
                
                file.write("----------------- USER PREFERENCES -----------------\n")
                file.write(f"Authors: {', '.join(preferences.author)}\n")
                file.write(f"Categories: {', '.join(preferences.category)}\n")
                file.write(f"Rating: {preferences.rating}\n\n")

                file.write("----------------- RECOMMENDED BOOKS -----------------\n")
                if self.recommendations.empty:
                    file.write("No recommendations found based on your preferences.\n")
                else:
                    for _, row in self.recommendations.iterrows():
                        file.write(f"Title: {row['title']}, Author: {row['author']}, Category: {row['category']}, Rating: {row['rating']}\n")

            print(f"\nRecommendations saved to {filename}")






if __name__ == "__main__":
    preferences = Preferences()
    preferences.collect_preferences()
    preferences.display_preferences()
    
    recommender = Recommender(df)
    recommender.recommend_books(preferences)

    recommender.display_recommendations()

    recommender.save_to_text_file(User(), preferences)  

    print("\nThank you for using the Book Recommendation System!")