import glob
import subprocess

molfilepaths = glob.glob("./*.mol")

with open("keggcid2inchikey.tsv", "w") as f:
  for path in molfilepaths:
    print(path)
    output = subprocess.run(['molconvert', 'inchikey', path], capture_output=True)
    stdout = output.stdout.decode()
    f.write(path.replace("./", "").replace(".mol", ""))
    f.write("\t")
    f.write(stdout.replace("InChIKey=", "").replace("\n", ""))
    f.write("\n")
    
