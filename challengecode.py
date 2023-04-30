import sys 

ciphered = ""

sys.stdin = ''.join([i for i in sys.stdin if i.isalpha()])

sys.stdin = sys.stdin.upper()

count = 0
count2 = 0

for char in sys.stdin:
  if ord(char) + sys.argv <= 133:
    ciphered = ciphered + chr(ord(char) + sys.argv)
  else:
    ciphered = ciphered + chr(ord(char) - (26-sys.argv))

  count = count + 1

  if count == 5:
    ciphered = ciphered + " "
    count = 0
    count2 = count2 + 1

  if count2 == 10:
    ciphered = ciphered + "\n"
    count2 = 0

print(ciphered)

