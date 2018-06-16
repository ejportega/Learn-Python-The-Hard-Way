from sys import argv
script, filename = argv # filename is the file you want to open

txt = open(filename) # the file will open then store in variable "txt"

print(f"\nHere's your file {filename}:")
print(txt.read()) # file content will read
txt.close() # close file

# print("Type the filename again:")
# file_again = input("> ")
#
# txt_again = open(file_again)
# print(txt_again.read())

print()
