formatter = "{} {} {} {}" # {} means put another string
k = 'B'
v = 'C'
z = 10
print("\n" + formatter.format(1, 2, 3, 4))
print(formatter.format('one', 'two', 'three', 'four'))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter.format(1, 2, 3, 4), formatter.format(5, 6, 7, 8), formatter.format(9, 10, 11, 12), formatter.format(13, 14, 15, 16)))
print(formatter.format(
    "This the start",
    "to build the foundation",
    "in learning python",
    "for a better future."
))
print("Yow %s or %s and %s" % (k, v, z * 10), end=' ')
print("Extension")
print()
