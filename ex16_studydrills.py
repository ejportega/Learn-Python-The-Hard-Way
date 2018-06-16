from sys import argv
script, filename = argv

print("\nAppending the file...")
target = open(filename, 'a')

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

lines = "\n{}\n{}\n{}"

target.write(lines.format(line1, line2, line3))

print("I'm going to write these to the file.")
print("And finally, we close it.")

target.close();

print()
