#!/usr/bin/env python3
"""
Daily Quote Generator

This script selects a random quote for the day and prints it. Optional: The same quote should be generated for a given day.

Your task:
1. Complete the get_quote_of_the_day() function
2. Set up a cron job to run this script daily at 8:00 AM and append the output to a file

Hint: Look up `random.choice()` to select a random item from a list. You can use the `date` module to get the current date and set a seed for the random number generator.
"""

import random
import datetime 
from datetime import date

 # Create a list of quotes here

quotes = [ "Rather than love, than money, than fame, give me truth", 
          "Success is not final, failure is not fatal: It is the courage to continue that counts.", 
          "I have not failed. I've just found 10,000 ways that won't work.", 
          "The elevator to success is out of order. You’ll have to use the stairs, one step at a time." , 
          "If you’re going through hell, keep going.", 
          "Go the extra mile. It’s never crowded there.", 
          "Debugging: Being the detective in a crime drama where you are also the murderer.", 
          "To err is human, but to really foul things up, you need a computer.", 
          "There are 10 types of people in the world: those who understand binary and those who don’t.", 
          "I had a life once... now I have assignments.",
          "The code works. I have no idea why. The code doesn’t work. I have no idea why.", 
          "My code is compiling, but am I?",
]

def get_quote_of_the_day(quotes):
    today = datetime.date.today()
    random.seed(today.toordinal)
    todays_quote = random.choice(quotes)


    # Your code here
    
    return todays_quote

if __name__ == "__main__":
    print(get_quote_of_the_day(quotes))

# Cron job (add this to your crontab):
# 0 8 * * * /usr/bin/python3 /path/to/quote_generator.py >> /path/to/daily_quote.txt