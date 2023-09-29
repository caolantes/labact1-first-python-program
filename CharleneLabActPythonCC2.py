import random

POUNDS_TO_KILOGRAMS = 0.454

userInput = float(input("Please enter a number to convert to kilograms: "))

userPoundsToKilograms = userInput * POUNDS_TO_KILOGRAMS

print(userInput, "pounds converted to kilogram is",\
       format(userPoundsToKilograms, ".2f"), "kilograms")

print("====================================")

miles = float(input("Please enter miles: "))
kilometers = miles * 1.6
print(kilometers, "kilometers")

print("===================================")

temp = float(input("Enter temperature in fahrenheit: "))
celsius = (temp - 32) * 5/9
print(f" {temp} in Fahrenheit is equal to {celsius} in Celsius")

print("====================================")

stud_input1 = float(input("Average age of student 1: "))
stud_input2 = float(input("Average age of student 2: "))
stud_input3 = float(input("Average age of student 3: "))
stud_input4 = float(input("Average age of student 4: "))
stud_input5 = float(input("Average age of student 5: "))
stud_input6 = float(input("Average age of student 6: "))
stud_input7 = float(input("Average age of student 7: "))
stud_input8 = float(input("Average age of student 8: "))
stud_input9 = float(input("Average age of student 9: "))
stud_input10 = float(input("Average age of student 10: "))

average_age = ((stud_input1 + stud_input2 + stud_input3 + stud_input4 + stud_input4 + stud_input5 + stud_input6 + stud_input7 + stud_input8 + stud_input9 + stud_input10)/10)
print("Average age of student is: ", average_age)

print("======================================")


names = ["Raelia", "Serene", "Farissia", "Khulus", "Heilan"]
equipments = ["katana", "bow and arrow", "gun", "excalibur", "sword"]
items = ["life-drinking dagger", "healing chalice", "cloak of invisibility", "potion", "crystal ball"]
abilities = ["agility", "summoning", "healing", "spellcasting", "endurance"]

randomname = random.choice(names)
randomequipment = random.choice(equipments)
randomitem = random.choice(items)
randomability = random.choice(abilities)

story = (f"In the mystical realm of Arvandor, five unlikely heroes embarked on a quest to save their world from impending darkness. {randomname}, an elven archer with eyes as sharp as her arrows, led the group with her wisdom and grace. She was known for her ability to {randomability}. {randomname}, a grizzled dwarven blacksmith, wielded {randomitem} and a {randomequipment}. His craftmanship forged the magical armor and weapons they would need on their journey. {randomname}, a mischievous gnome rogue with a talent for {randomability}, brought humor and cunning to the group. {randomname}, a young and inexperienced wizard, possessed untapped {randomability} in the arcane arts.He was the group's source of magical knowledge, through his inexperience often led to comical mishaps. {randomname}, a fierce dragon born warrior with scales as dark as night, was a formidable protector. His {randomability}, and his unwavering loyalty to his companions made him an invalluable ally. Together, they embarked on perilous journey to retrieve the lost Staff of Arvandor, the only artifact capable of banishing the encroaching darkness. Along the way, they encountered treacherous landscapes, faced formidable foes, and forged unbreakable bonds. Their quest tested their strengths and weaknesses, but their unwavering determination and unique talents ultimately allowed them to vanquish the darkness, restoring peace and realm's history.")

print(story)