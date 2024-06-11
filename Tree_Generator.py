import os

def print_dir_tree(startpath, exclude_dirs=None):
    if exclude_dirs is None:
        exclude_dirs = ['.git']  # Default directory to exclude if none is provided

    print(f"Starting directory tree print for: {startpath}")

    for root, dirs, files in os.walk(startpath, topdown=True):
        # Skip directories that are in the exclude list
        dirs[:] = [d for d in dirs if d not in exclude_dirs]
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print(f"{indent}{os.path.basename(root)}/")
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print(f"{subindent}{f}")

# Example usage:
exclude_list = ['.git','node_modules', '.import', '__pycache__','ArduinoJson','Pour_Moi','Codepo_22_23','CodePourChristian']
print_dir_tree('.', exclude_list)
#print_dir_tree('C:/MES_Programmes/VirtualMachineSharedFolder/Polytech/0_MA1/year_23_24/INFOH505_Cloud Computing/Seminar', exclude_list)
