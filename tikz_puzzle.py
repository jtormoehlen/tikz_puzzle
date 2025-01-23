import util as utl

# Explanation for picking rules:
# '#|' first or second piece
# '#*' zero or more pieces
# '#+' one or more pieces
OR = '#|'
ZEROPLUS = '#*'
ONEPLUS = '#+'

# Source code as string
tikz_ins = [
    'binomial',
    'majority',
    'mergesort',
    'palindrome',
    'tree'
]

for tikz_in in tikz_ins:

    file_content = utl.read_file('tikz_src/' + tikz_in + '.txt')
    print(file_content)

    file_content = utl.remove_indents(file_content)
    file_content = utl.shuffle_lines(file_content)
    # s = verbinde_zeilen_mit_suffix(s)
    # s = trenne_zeilen_nach_suffix(s)
    # s = einfuege_zeilenumbruch(s)

    node = r"""\node[draw,$opt rounded corners, fill=$color!20, minimum width=$lenFac*\rectWidth, minimum height=\rectHeight, anchor=$anch] (rect$recNum) at (rect$prevRec.$susp) {
    \begin{minipage}[c]{$snipLencm}
    \begin{lstlisting}[language=Python, breaklines=true]
    $snippet
    \end{lstlisting}
    \end{minipage}
    \begin{minipage}[c]{$numLencm}
    $enum
    \end{minipage}
    };
    """

    outputs = []
    inputs = {'$recNum': 1, '$prevRec': 0,
            '$xpos': 0, '$ypos': 0,
            '$enum': 1, '$snippet': '',
            '$numLen': 0.5, '$snipLen': 14.5,
            '$anch': 'north west', '$susp': 'south west',
            '$lenFac': 1, '$opt': '',
            '$color': 'blue'}
    grouped = False

    for line in file_content.splitlines():
        if ZEROPLUS in line:
            inputs['$opt'] = 'dashed,'
            line = line.replace(ZEROPLUS, '')
            inputs['$color'] = 'red'
        elif ONEPLUS in line:
            inputs['$opt'] = 'dashed,'
            line = line.replace(ONEPLUS, '')
        else:
            inputs['$opt'] = ''
            inputs['$color'] = 'blue'

        parts = line.split(OR)
        if len(parts) == 2:
            grouped = True
        else:
            grouped = False

        if grouped:
            leftNode = node
            leftNodeInputs = {'$recNum': inputs['$recNum'], 
                            '$prevRec': inputs['$prevRec'],
                            '$xpos': 0, 
                            '$ypos': 0,
                            '$enum': str(inputs['$enum']) + 
                                utl.number_to_letters(1),
                            '$snippet': parts[0],
                            '$numLen': inputs['$numLen'], 
                            '$snipLen': 6.5,
                            '$anch': inputs['$anch'], 
                            '$susp': inputs['$susp'],
                            '$lenFac': 0.5, 
                            '$opt': inputs['$opt'],
                            '$color': inputs['$color']}

            for key, value in leftNodeInputs.items():
                leftNode = leftNode.replace(key, str(value))

            leftNode = utl.edit_pattern(leftNode)
            outputs.append(leftNode)

            rightNode = node
            rightNodeInputs = {'$recNum': inputs['$recNum']*100+1, 
                            '$prevRec': inputs['$recNum'],
                            '$xpos': 0, 
                            '$ypos': 0,
                            '$enum': str(inputs['$enum']) + 
                            utl.number_to_letters(2), 
                            '$snippet': parts[1],
                            '$numLen': inputs['$numLen'], 
                            '$snipLen': 6.5,
                            '$anch': 'west', 
                            '$susp': 'east',
                            '$lenFac': 0.5, 
                            '$opt': inputs['$opt'],
                            '$color': inputs['$color']}

            for key, value in rightNodeInputs.items():
                rightNode = rightNode.replace(key, str(value))

            rightNode = utl.edit_pattern(rightNode)
            outputs.append(rightNode)

        else:
            inputs['$snippet'] = line
            rootNode = node

            for key, value in inputs.items():
                rootNode = rootNode.replace(key, str(value))

            rootNode = utl.edit_pattern(rootNode)
            outputs.append(rootNode)

        inputs['$enum'] = inputs['$enum']+1
        inputs['$recNum'] = inputs['$recNum']+1
        inputs['$prevRec'] = inputs['$prevRec']+1

    outputs[0] = utl.edit_pattern(
        outputs[0], '(rect1) at (0,0)', r'\((rect1)\) at \((.*?)\)')
    output = r"""\begin{tikzpicture}

    """ + ''.join(outputs) + r"""

    \end{tikzpicture}"""

    with open('tikz_tex/' + tikz_in + '.tex', 'w') as f:
        print(output, file=f)
