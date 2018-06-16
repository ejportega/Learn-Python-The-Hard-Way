from sys import argv
from os.path import exists

script, from_file, to_file = argv

print("\nCopying from %s to %s\nThe input file is %s bytes long\nDoes the output file exist? %s\nReady, hit RETURN to continue, CTRL-C to abort.\n\nAlright, all done" % (from_file, to_file, len(from_file), exists(to_file)))
open(to_file, 'w').write(open(from_file).read())
print()
