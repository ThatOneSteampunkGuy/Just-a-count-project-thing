notNum = True
while notNum:
  print("What would you like me to count up to?")
  try:
    num = float(input())
    notNum = False
  except:
    print("That is not a number!")
    break
for f in range(int(num / 10 * 10)):
  f += 1
  print(f)




