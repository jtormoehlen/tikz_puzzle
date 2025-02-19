import util as utl

# Explanation for picking rules:
# '#|' first or second piece
# '#*' zero or more pieces
# '#+' one or more pieces
# '#<Number> line break 
id_or = '#|'
id_zeroplus = '#*'
id_oneplus = '#+'

node = r"""\node[draw,$opt rounded corners, fill=$color!20, minimum width=$lenFac*\rectWidth, minimum height=\rectHeight, anchor=$anch] (rect$recNum) at (rect$prevRec.$susp) {
\begin{minipage}[c]{$snipLencm}
\begin{lstlisting}[language=Python, breaklines=true]
$snippet
\end{lstlisting}
\end{minipage}
\begin{minipage}[c]{$numLencm}
$enum
\end{minipage}
};"""

# Source code as string
tikz_ins = [
    'palindrome',
    'binomial',
    'tree',
    'majority',
    'mergesort'
]

permutations = []

for tikz_in in tikz_ins:

    file_content = utl.read_file('tikz_src/' + tikz_in + '.txt')
    # print(file_content)

    file_content = utl.remove_indents(file_content)
    file_content, permutation = utl.shuffle_lines(file_content)
    
    # for i in range(len(permutation)):
    #     permutation[i] += 1

    permutations.append(permutation)
    # s = verbinde_zeilen_mit_suffix(s)
    # s = trenne_zeilen_nach_suffix(s)
    # s = einfuege_zeilenumbruch(s)

    outputs = []
    inputs = {'$recNum': 1, '$prevRec': 0,
            '$xpos': 0, '$ypos': 0,
            '$enum': 0, '$snippet': '',
            '$numLen': 0.5, '$snipLen': 14.5,
            '$anch': 'north west', '$susp': 'south west',
            '$lenFac': 1, '$opt': '',
            '$color': 'lightgray'}
    grouped = False

    for line in file_content.splitlines():
        if id_zeroplus in line:
            inputs['$opt'] = 'dashed,'
            line = line.replace(id_zeroplus, '')
            # inputs['$color'] = 'red'
        elif id_oneplus in line:
            inputs['$opt'] = 'dashed,'
            line = line.replace(id_oneplus, '')
        else:
            inputs['$opt'] = ''
            # inputs['$color'] = 'blue'

        parts = line.split(id_or)
        if len(parts) == 2:
            grouped = True
        else:
            grouped = False

        if grouped:
            left_node = node
            left_node_inputs = {
                '$recNum': inputs['$recNum'],
                '$prevRec': inputs['$prevRec'],
                '$xpos': 0,
                '$ypos': 0,
                '$enum': str(inputs['$enum']) + utl.number_to_letters(1),
                '$snippet': parts[0],
                '$numLen': inputs['$numLen'],
                '$snipLen': 6.5,
                '$anch': inputs['$anch'],
                '$susp': inputs['$susp'],
                '$lenFac': 0.5,
                '$opt': inputs['$opt'],
                '$color': inputs['$color']
            }

            for key, value in left_node_inputs.items():
                left_node = left_node.replace(key, str(value))

            left_node = utl.edit_pattern(left_node)
            outputs.append(left_node)

            right_node = node
            right_node_inputs = {
                '$recNum': inputs['$recNum'] * 100 + 1,
                '$prevRec': inputs['$recNum'],
                '$xpos': 0,
                '$ypos': 0,
                '$enum': str(inputs['$enum']) + utl.number_to_letters(2),
                '$snippet': parts[1],
                '$numLen': inputs['$numLen'],
                '$snipLen': 6.5,
                '$anch': 'west',
                '$susp': 'east',
                '$lenFac': 0.5,
                '$opt': inputs['$opt'],
                '$color': inputs['$color']
            }

            for key, value in right_node_inputs.items():
                right_node = right_node.replace(key, str(value))
            
            right_node = utl.edit_pattern(right_node)
            outputs.append(right_node)

        else:
            inputs['$snippet'] = line
            root_node = node

            for key, value in inputs.items():
                root_node = root_node.replace(key, str(value))

            root_node = utl.edit_pattern(root_node)
            outputs.append(root_node)

        inputs['$enum'] = inputs['$enum']+1
        inputs['$recNum'] = inputs['$recNum']+1
        inputs['$prevRec'] = inputs['$prevRec']+1

    outputs[0] = utl.edit_pattern(
        outputs[0], '(rect1) at (0,0)', r'\((rect1)\) at \((.*?)\)')
    output = r"""\begin{tikzpicture}

    """ + ''.join(outputs) + r"""

    \end{tikzpicture}"""

    with open('tikz_tex/' + tikz_in + '.tex', 'w') as tex_file:
        print(output, file=tex_file)

with open('tikz_tex/solution.txt', 'w') as sol_file:
    for permutation in permutations:
        print(permutation, file=sol_file)