import random as rnd

def modify_lines(file_path):

    try:
        # Open code files
        with open(f'./widget_src/in/{file_path}.pzl', 'r') as input_file:
            lines = input_file.readlines()

        permutation = [i for i in range(1, len(lines) + 1)]
        rnd.shuffle(permutation)
        modified_lines = []
        
        for index, line in enumerate(lines):
            max_chars = 50
            delta = max_chars - len(line.lstrip(' '))
            blanks = ' ' * delta
            # Preserve initial blanks
            modified_line = '"' + line.rstrip('\n') + blanks + f' # {permutation[index]}\\n' + '" +\n'
            modified_lines.append(modified_line)
        
        # Save modiefied lines as same file
        with open(f'./widget_src/out/{file_path}.pzl', 'w') as output_file:
            output_file.writelines(modified_lines)

    except FileNotFoundError:
        print(f"Die Datei {file_path} wurde nicht gefunden.")
    except Exception as e:
        print(f"Ein Fehler ist aufgetreten: {e}")

# Read all code files
for filename in ['binomial', 'majority', 'mergesort', 'palindrome', 'tree']:
    modify_lines(filename)