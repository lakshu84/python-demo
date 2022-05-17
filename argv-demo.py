from sys import argv

for filename in argv[1:]:
    with open(filename, 'r') as f:
        lines = f.readlines()

    lines.insert(0, filename.upper() + '\n')
    lines.insert(1, "Author: J. Smith\n")
    
    with open(filename, 'w') as f:
        f.writelines(lines)