# House Cleaning Cost Calculator 2.0
# This program calculates the cost of house cleaning based on the number of rooms, the type(s) of cleaning service(s), and cleaning quality selected.
# Name: Adnan Civic
# Date: 1/31/2024

import re
from fuzzywuzzy import process
from word2number import w2n

# Constants for room size cutoffs and number words.
SMALL_HOUSE_MAX = 3
MEDIUM_HOUSE_MAX = 6
NUMBER_WORDS = ['one', 'two', 'three', 'four', 'five',
                'six', 'seven', 'eight', 'nine', 'ten',
                'eleven', 'twelve', 'thirteen', 'fourteen',
                'fifteen', 'sixteen', 'seventeen', 'eighteen',
                'nineteen', 'twenty']

# Cleaning costs per room.
CLEANING_SERVICE_COSTS = {
    "floors": 50,
    "windows": 40,
    "bathrooms": 60,
    "dusting": 30
}

# Constants for cleaning quality.
LIGHT_CLEANING_MULTIPLIER = 0.6
COMPLETE_CLEANING_MULTIPLIER = 1.1
CLEANING_QUALITIES = {
    "light": LIGHT_CLEANING_MULTIPLIER,
    "complete": COMPLETE_CLEANING_MULTIPLIER
}

#Prompt user for number of rooms and validate input.
def get_number_of_rooms():
    attempt_count = 0
    while attempt_count < 3:
        num_rooms_input = input("Enter the number of rooms in your house: ").lower()
        
        if num_rooms_input.isdigit():
            return int(num_rooms_input)
        else:
            # Fuzzy matching to interpret number words.
            matched_number, similarity = process.extractOne(num_rooms_input, NUMBER_WORDS)
            
            if similarity >= 75: # This similarity score can be adjusted from 0-100. The higher the score the more similar it is.
                try:
                    return w2n.word_to_num(matched_number)
                except ValueError:
                    print("Invalid number of rooms. Please try again.")
            else:
                print("Invalid number of rooms. Please try again.")
        attempt_count += 1
    print("Maximum attempts reached. Exiting.")
    exit()

#Prompt user for cleaning services and validate input.
def select_cleaning_services(): 
    print("Cleaning services offered: floors, windows, bathrooms, dusting")
    selected_services = set() # Using set to avoid duplicate services.
    while True:
        cleaning_services_input = input("Enter the type(s) of cleaning you want (separate by space or comma): ").lower()
         # Splitting input by both commas and spaces
        service_list = [service.strip() for service in re.split(',| ', cleaning_services_input) if service]
        valid_input = True
        for service in service_list:
            cleaning_type, similarity = process.extractOne(service, CLEANING_SERVICE_COSTS.keys())
            
            if similarity >= 75: # This similarity score can be adjusted from 0-100. The higher the score the more similar it is.
                selected_services.add(cleaning_type)
            else:
                print(f"Invalid cleaning type '{service}'. Please try again.")
                valid_input = False
                break

        if valid_input:
            return selected_services

# Prompt user for cleaning quality and validate input.
def get_cleaning_quality():
    while True:
        cleaning_quality_input = input("Would you like a light or complete cleaning: ").lower().split()
        matched_qualities = []

        for word in cleaning_quality_input:
            quality, similarity = process.extractOne(word, CLEANING_QUALITIES.keys())
            if similarity >= 75: # This similarity score can be adjusted from 0-100. The higher the score the more similar it is.
                matched_qualities.append(quality)

        if len(matched_qualities) == 1:
            return matched_qualities[0], CLEANING_QUALITIES[matched_qualities[0]]
        else:
            print("Invalid option. Please choose 'light' or 'complete'.")

#Calculate the total cleaning cost based on room count and services.
def calculate_total_cost(num_rooms, selected_services): 
    total_cost = sum(CLEANING_SERVICE_COSTS[service] * num_rooms for service in selected_services)
    return total_cost

def main():
    print("House Cleaning Cost Calculator")
    print("Adnan, CMSC 105 6384, 1/31/2024\n")

    num_rooms = get_number_of_rooms()
    selected_services = select_cleaning_services()

    house_size = "Small" if num_rooms <= SMALL_HOUSE_MAX else "Medium" if num_rooms <= MEDIUM_HOUSE_MAX else "Large"
    total_cost = calculate_total_cost(num_rooms, selected_services)

#Factor in cleaning quality to total cost.
    cleaning_quality, cleaning_quality_multiplier = get_cleaning_quality()
    total_cost *= cleaning_quality_multiplier

    print(f"\nHouse size: {house_size}, with {num_rooms} rooms")
    print(f"Cleaning services selected: {', '.join(selected_services)}")
    print(f"Cleaning quality selected: {cleaning_quality}")
    print(f"Total cost: ${round(total_cost, 2)}")

if __name__ == "__main__":
    main()