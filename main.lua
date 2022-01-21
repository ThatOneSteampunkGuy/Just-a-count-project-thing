
local function count()
  print("What would you like to count up to?")
  upTo = io.read()
  for count = 1, upTo, 1 do
      print(count)
      print("___")
  end
end
count()

