import sys 

ciphered = ""

input_text = input()
input_text = ''.join([i for i in input_text if i.isalpha()])

input_text = input_text.upper()

count = 0
count2 = 0

n = int(sys.argv[1])

for char in input_text:
  if ord(char) + n <= 133:
    ciphered = ciphered + chr(ord(char) + n)
  else:
    ciphered = ciphered + chr(ord(char) - (26-n))

  count = count + 1

  if count == 5:
    ciphered = ciphered + " "
    count = 0
    count2 = count2 + 1

  if count2 == 10:
    ciphered = ciphered + "\n"
    count2 = 0

print(ciphered)

