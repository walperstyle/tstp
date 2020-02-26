age = 62
retirement =  65 - age

if retirement < 10 and retirement >= 0:
    print("You get to retire soon.")
elif retirement <= 0:
    print("You should already be retired")
else:
    print("You have a long time until you can retire!")
    
#the old code for challenge 6, page 45 from the book was wrong
#the old code would produce "you get to retire soon" regardless
#of what the age variable was. This code I have written is better.
