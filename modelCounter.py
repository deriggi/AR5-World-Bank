import os

cvar = "pr"
rootDir = "F:/climate/monthly/{0}/monthtrend_20/".format(cvar)
children = os.listdir(rootDir)

fileset = []
for c in children:
	if c not in fileset:
		fileset.append(c)

modelset = []
for i in xrange(0, len(fileset)):
	model = fileset[i].split('_')[2]
	if model not in modelset:
		modelset.append(model)  
# modelset = sorted(modelset)
out = open("C:/Users/Johnny/Documents/climatev2/ar5repo/{0}_models.txt".format(cvar), 'a')

for m in modelset:
	out.write(m.lower())
	out.write('\n')

out.close
