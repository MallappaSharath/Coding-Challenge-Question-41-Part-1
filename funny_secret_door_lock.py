"""
Coding Challenge Question 41 : Funny Secret Door Lock
Program will operate in Automatic mode where pass-code is chosen by the program. The user needs to guess the pass-code.
"""


# To generate random pass-code
from random import randint


# Retive Pass-code from user
def get_the_user_input():
	user_passcode = input("Enter the pass-code: ")
	return user_passcode


# Validte user pass-code
def validate_passcode(user_passcode):
	error = False
	validated_passcode = 0
	try:
		validated_passcode = int(user_passcode)
		if validated_passcode < 0:
			print("Invalid passcode!! No negative numbers")
			error = True
			return validated_passcode, error
		else:
			return validated_passcode, error
	
	except ValueError:
		error = True
		print("Invalid passcode!! passcode should be numeric")
		return validated_passcode, error

		
# Verify the user pass-code against auto-passcode		
def check_the_passcode(user_passcode, auto_passcode):
	success = False
	if user_passcode == auto_passcode:
		print("WELCOME !!!\n")
		success = True
		return success, 0
	elif user_passcode > (auto_passcode + 3):
		print("Walk down some steps\n")
		success = False
		return success, abs(auto_passcode - user_passcode)
	elif user_passcode < (auto_passcode - 3):
		print("Walk up some steps\n")
		success = False
		return success, abs(auto_passcode - user_passcode)
	else:
		print("Hop around\n")
		success = False
		return success, abs(auto_passcode - user_passcode)


# Funny Secret Door Lock program starts here.
# =============================================
# Generate automatic pass-code between 10 to 40
auto_passcode = randint(10, 40)

print("You need to guess the pass-code. You have five chance!\n")

count = 0
steps_away = 0
nearest = 0

while count < 5:
	error = True
	validated_passcode = 0
	
	while error == True:
		user_passcode = get_the_user_input()
		validated_passcode, error = validate_passcode(user_passcode)
		
	success, steps_away = check_the_passcode(validated_passcode, auto_passcode)
	
	if success == True:
		break;
		
	if count == 0:
		nearest = steps_away
	else:
		if steps_away < nearest:
			nearest = steps_away
			
	count += 1
else:
	print("Sorry : You were {n} steps away".format(n=nearest))