"""
Study Time Tracker
Script that asks the user for daily study hours and
calculates weekly estimate
"""

print("Welcome to my Python program!")
#User input
hours = input("How many hours did you study today? ")

#convert weekly hours with error handling
try:
    hours = float(hours)
except ValueError:
    print("Please enter a valid number")
    exit()
#Calculation and result
weekly_hours = hours * 7
print(f"You are on track to study {weekly_hours:.1f} hours this week.")