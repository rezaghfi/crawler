array = [
  {"name": "reza", "age": 30},
  {"name": "reza", "age": 30},
]

with open("save_array.txt", "w") as f:
  for item in array:
    f.write("%s\n" % item)

o = open("save_array2.txt", "w")
o.write("%s\n" % item)