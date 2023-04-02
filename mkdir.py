import os
parent_dir = "data"
for i in range(125,150):
    path = os.path.join(parent_dir, str(i))
    os.mkdir(path)
print("Directory '% s' created" % i)