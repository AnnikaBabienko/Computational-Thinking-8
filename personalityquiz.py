Outdoor_person = 0
Indoor_person = 0


answer = input("Would you rather A watch a move or B watch a sports game?  ")
if answer == "A" or answer == "a":
	Indoor_person += 1
elif answer == "B" or answer == "b":
	Outdoor_person += 1
else:
	print("Please select A or B")


answer = input("Would you rather A stay in on a snow day or B Go out and play in the snow or C do both!? ")
if answer == "A" or "a":
	Indoor_person += 1
elif answer == "B" or answer == "b":
	Outdoor_person += 1
elif answer == "C" or answer == "c":
	Outdoor_person += 0.5  
	Indoor_person += 0.5
else:  
	print("Please select A or B")


answer = input("Would you rather A play a video game or B play a sport?   ")
if answer == "A" or answer == "a":
	Indoor_person += 1
elif answer == "B" or answer == "b":
	Outdoor_person += 1
else:
	print("Please select A or B")
	
answer = input("Would you rather A facetime friends or B hang out with them? ")
if answer == "A" or answer == "a":
	Indoor_person += 1
elif answer == "B" or answer == "b":
	Outdoor_person += 1
else:
	print("Please select A or B")
	
answer = input("Do your prefer A online shopping or B shopping at the mall? ")
if answer == "A" or answer== "a":
	Indoor_person += 1
elif answer == "B" or answer == "b":
	Outdoor_person += 1
else:
	print("Please select A or B")

if Outdoor_person > Indoor_person: 
	print ("You are an outdoor person!")
if Outdoor_person > Indoor_person and Outdoor_person > 4:
	print ("You are very much an outdoor person!")
elif Outdoor_person < Indoor_person and Indoor_person > 4:
	print ("You are very much an indoor person!")
elif Indoor_person > Outdoor_person:
	print ("You are an indoor person!")

