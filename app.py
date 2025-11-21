print("Welcome to my Python program!")
hours = input("How many hours did you study today? ")

#convert and calculate weekly hours
try:
    hours = float(hours)
except ValueError:
    print("Please enter a valid number")
    exit()
#result
weekly_hours = hours * 7
print(f"You are on track to study {weekly_hours:.1f} hours this week.")