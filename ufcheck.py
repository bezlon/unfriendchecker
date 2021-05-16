import requests
import json
import datetime
import time
import os

print("- PROMPT -")
user_id = input("What is your Roblox user ID? ")
request = requests.get(f"https://friends.roblox.com/v1/users/{user_id}/friends").json()

friends = []

def refresh_friends():
	global friends
	new_friends_list = []

	for friend in request["data"]:
		new_friends_list.append(friend["name"])

	friends = new_friends_list

def get_friends():
	friends_ = []

	for friend in request["data"]:
		friends_.append(friend["name"])

	return friends_

os.system("color") # Activates colors and ANSI
print("\x1b[2J\x1b[H", end="") # Clear screen
refresh_friends()

while True:
	print("""\x1b[1;0m
██╗░░░██╗███████╗░█████╗░██╗░░██╗███████╗░█████╗░██╗░░██╗
██║░░░██║██╔════╝██╔══██╗██║░░██║██╔════╝██╔══██╗██║░██╔╝
██║░░░██║█████╗░░██║░░╚═╝███████║█████╗░░██║░░╚═╝█████═╝░
██║░░░██║██╔══╝░░██║░░██╗██╔══██║██╔══╝░░██║░░██╗██╔═██╗░
╚██████╔╝██║░░░░░╚█████╔╝██║░░██║███████╗╚█████╔╝██║░╚██╗
░╚═════╝░╚═╝░░░░░░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░╚═╝░░╚═╝""") # Logo/title
	print("\x1b[1;0m" + "^"*57) # 57 ^ long line
	request = requests.get(f"https://friends.roblox.com/v1/users/{user_id}/friends").json()

	new_friends = get_friends()

	for friend in friends: # Check if user unfriends
		if friend in new_friends:
			print(f"\x1b[1;32m\"{friend}\" is still your friend as of \x1b[1;0m{datetime.datetime.now()}!")
		else:
			with open("betrayers.txt", "a") as file:
				file.write(f"{friend} in {datetime.datetime.now()}.")

			print(f"\x1b[1;31m\"{friend}\" unfriended you some time in \x1b[1;0m{datetime.datetime.now()}!")

		time.sleep(0.01) # Small delay for style

	print(f"\x1b[1;0mAnother check will occur in 24 hours as of {datetime.datetime.now()}.") # Resets terminal color to white

	time.sleep(86400) # One day
	print("\x1b[2J\x1b[H") # Clear screen