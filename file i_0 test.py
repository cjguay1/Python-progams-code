input = open('lines.txt', 'r')
output = open('lines-copy.txt', 'w')
for line in input:
    print(line.rstrip(), file=output)
    print(line.rstrip())
output.close()
print('done.')
