print("Welcome to my Python program!")
hours = input("How many hours did you study today? ")

#convert and calculate weekly hours
hours = float(hours)
weekly_hours = hours * 7

#result
print(f"You are on track to study {weekly_hours:.1f} hours this week.")