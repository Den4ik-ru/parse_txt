import os

cwd = os.getcwd()+ "\\исходник"
files = os.listdir(cwd)
name=""
for file in files:
    name = file
with open(f'исходник/{name}', 'r') as infile, open(f'результат/{name}', 'w') as outfile:
    for line in infile:
        if not line.startswith('intergenic') and not line.startswith('intronic'):
            columns = line.split('\t')
            if columns[3] == columns[4]:
                outfile.write(line)
