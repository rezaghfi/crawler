array = [
  {"name": "reza", "age": 30},
  {"name": "reza", "age": 30},
]

with open("save_array.txt", "w") as f:
  for item in array:
    f.write("%s\n" % item)
