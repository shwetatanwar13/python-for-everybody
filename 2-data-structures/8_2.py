fhand = open('mbox-short.txt')
count = 0
for line in fhand:
  line = line.rstrip()
  words in line.split()
  #print 'Debug:', words
  if len(words) == 0 : continue
  if words[0] != 'From' : continue
  print words[2]