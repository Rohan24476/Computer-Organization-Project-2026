import sys
import os

if len(sys.argv) != 4:
    print("Usage: python3 Assembler.py <input_assembly_path> <output_machine_code_path> <output_readable_path>")
    sys.exit(1)

print(list(x for x in sys.argv)) #Prints the paths for easy viewing

goldenPath = (sys.argv[1]).replace("simpleBin", "bin_s")
path1 = "..\\automatedTesting\\tests\\assembly\\user_bin_s"
path2 = "..\\automatedTesting\\tests\\assembly\\user_bin_h"
if not os.path.isdir(path1):
    os.makedirs(path1)
if not os.path.isdir(path2):
    os.makedirs(path2)


with open(sys.argv[2], 'w') as f:
    with open(goldenPath, 'r') as g:
        f.writelines(g.readlines())