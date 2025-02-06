import random as rd
import re


def remove_indents(multi_line_string):
    # Split string by parts
    lines = multi_line_string.splitlines()
    # Remove pre blanks
    new_lines = [line.lstrip() for line in lines]
    # Merge strings back together
    return '\n'.join(new_lines)


def shuffle_lines(multi_lines_string):
    # Split string by parts
    lines = multi_lines_string.splitlines()
    # Shuffle lines random
    rd.shuffle(lines)
    # Merge strings back together
    return '\n'.join(lines)


def conc_lines_suffix(multi_line_string):
    # Split string by parts
    lines = multi_line_string.splitlines()

    suffix_dict = {}

    for line in lines:
        # Search for suffix with #\d
        suffix = ''
        parts = line.rsplit(' ', 1)  # Split at last blank
        if len(parts) > 1:
            suffix_cand = parts[-1]
            if suffix_cand.startswith('#') and suffix_cand[1:].isdigit():
                suffix = suffix_cand

        # Add line with suffix to dictionary
        if suffix:
            if suffix not in suffix_dict:
                suffix_dict[suffix] = []
            suffix_dict[suffix].append(
                parts[0] + ' ' + suffix)  # Dont remove suffix
        else:
            # Add line without changes if no valid Suffix found
            # Add empty group for line without suffix
            if '' not in suffix_dict:  
                suffix_dict[''] = []
            suffix_dict[''].append(line)

    # Connect lines with same suffix
    connected_lines = []
    for lines_with_suffix in suffix_dict.values():
        connected_lines.append(' '.join(lines_with_suffix))

    return '\n'.join(connected_lines)


def insert_new_line(text):
    # Regex pattern for #Zahl followed by a blank and more optional chars
    pattern = r'(#[0-9]+ )'

    # Insert new line to pattern
    new_line_added = re.sub(pattern, r'\1\n', text)

    return new_line_added


def edit_pattern(input_string, sequence='', pattern=r'#\d+\s*'):
    # Regex for finding #Zahl plus blank

    # Replace pattern by empty string
    result_string = re.sub(pattern, sequence, input_string)

    return result_string


def split_string(input_string):
    # Break string at char '|'
    parts = input_string.split('|')

    # Check string for partitioning in two halfes
    if len(parts) == 2:
        # Trim excessive spaces
        return parts[0].strip(), parts[1].strip()  
    else:
        return None


def number_to_letters(n):
    if n < 1:
        return ''

    letters = []

    while n > 0:
        # Correspond numbs with chars
        # (1 -> 'a', 2 -> 'b', ..., 26 -> 'z')
        # Change from 1-based to 0-based
        n -= 1  
        # Calculate char from integer
        letters.append(chr(n % 26 + ord('a')))
        # Setup next char
        n //= 26

    # Reverse char order
    return ''.join(reversed(letters))


def check_and_execute(input_string):
    # RegEx for #+Zahl
    pattern = r'#\d+'

    # Search for all matches with input string
    matches = re.findall(pattern, input_string)

    # Check for multiple appearances
    if len(matches) > 1:
        pass


# Function to read the file and store its content as a string
def read_file(file_path):
    try:
        # Open the file in read mode with UTF-8 encoding
        with open(file_path, 'r', encoding='utf-8') as file:
            # Read the entire content of the file
            content = file.read()
            return content
    except FileNotFoundError:
        print(f'The file {file_path} was not found.')
        return None
    except Exception as e:
        print(f'An error occurred: {e}')
        return None