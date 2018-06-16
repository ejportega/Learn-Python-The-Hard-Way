from sys import argv
script, user_name = argv
prompt = '> '

print("\nHi %s, I'm the %s script." % (user_name, script))
print("I'd like to ask you a few questions.")

print("Do you like me zed?")
likes = input(prompt)

print("Where do you live zed?")
lives = input(prompt)

print("What kind of computer you have?")
computer = input(prompt)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
Ands you have a {computer} computer. Nice.
""")

print()
