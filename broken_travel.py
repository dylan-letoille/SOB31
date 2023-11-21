# A time traveler has suddenly appeared in your classroom!

# Create a variable representing the traveler's
# year of origin (e.g., year = 2000)
# and greet our strange visitor with a different message
# if he is from the distant past (before 1900),
# the present era (1900-2020) or from the far future (beyond 2020).

year = int(input("Greetings! What is your year of origin? "))  # replaced int. with int(, replaced ' with " at the
# end and removed an equals sign

if year <= 1900:  # added colon
    print("Woah, that's the past!")  # replaced ' with " on both ends of the string
elif 1900 <= year <= 2020:  # simplified comparison from year > 1900 and year < 2020 and added <= so 2020 and 1900 is
    # counted as the present
    print("That's totally the present!")
else:  # replaced elif with else
    print("Far out, that's the future!!")
