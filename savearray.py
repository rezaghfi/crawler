array = [
  {"name": "reza", "age": 30},
  {"name": "reza", "age": 30},
]

with open("a.txt", "w") as f:
  for item in array:
    f.write("%s\n" % item)
