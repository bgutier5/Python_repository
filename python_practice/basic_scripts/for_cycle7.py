param = {"mass": 5, "states": 5, "HOs": 5}
print(param)

for j in range(2,7):
 for i in range(2,7):
  param["mass"] =  i
  param["states"] = j

  print(param)
