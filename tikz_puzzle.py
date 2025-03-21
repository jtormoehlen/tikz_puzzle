import util as utl

# Explanation for picking rules:
# '#|' first or second piece
# '#*' zero or more pieces
# '#+' one or more pieces
# '#<Number> line break 
ident_or = '#|'
ident_opt = '#*'
ident_plus = '#+'

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
filenames = [
    'sum',
    'palindrome',
    'binomial',
    'tree',
    'majority',
    'mergesort',
    'memo'
]

permutations = []


def update_variables(vars):
    vars['$enum'] = vars['$enum']+1
    vars['$recNum'] = vars['$recNum']+1
    vars['$prevRec'] = vars['$prevRec']+1


def replace_variables(node, node_vars):
    for key, value in node_vars.items():
        node = node.replace(key, str(value))
    return node


def handle_distractor(vars, parts, codeboxes):
    left = node
    left_vars = vars.copy()
    left_vars['$enum'] = str(vars['$enum']) + utl.number_to_letter(1)
    left_vars['$snippet'] = parts[0]
    left_vars['$snipLen'] = 6.5
    left_vars['$lenFac'] = 0.5
    left = replace_variables(left, left_vars)
    left = utl.edit_pattern(left)
    codeboxes.append(left)

    right = node
    right_vars = vars.copy()
    right_vars['$recNum'] = vars['$recNum'] * 100 + 1
    right_vars['$prevRec'] = vars['$recNum']
    right_vars['$enum'] = str(vars['$enum']) + utl.number_to_letter(2)
    right_vars['$snippet'] = parts[1]
    right_vars['$snipLen'] = 6.5
    right_vars['$anch'] = 'west'
    right_vars['$susp'] = 'east'
    right_vars['$lenFac'] = 0.5
    right = replace_variables(right, right_vars)       
    right = utl.edit_pattern(right)
    codeboxes.append(right)


def handle_codeline(codeline, vars, codeblocks):

    if ident_opt in codeline:
        vars['$opt'] = 'dashed,'
        codeline = codeline.replace(ident_opt, '')
        # vars['$color'] = 'red'
    elif ident_plus in codeline:
        vars['$opt'] = 'dashed,'
        codeline = codeline.replace(ident_plus, '')
    else:
        vars['$opt'] = ''
        # vars['$color'] = 'blue'

    parts = codeline.split(ident_or)
    is_distractor = True if len(parts) == 2 else False

    if is_distractor:
        handle_distractor(vars, parts, codeblocks)
    else:
        vars['$snippet'] = codeline
        root = node
        root = replace_variables(root, vars)
        root = utl.edit_pattern(root)
        codeblocks.append(root)

    update_variables(vars)


def codelines_to_blocks():
    codelines = utl.read_file('tikz_src/' + filename + '.txt')
    codelines = utl.remove_indents(codelines)
    codelines, permutation = utl.shuffle_lines(codelines)

    permutations.append(permutation)

    codeboxes = []
    vars = {
        '$recNum': 1,
        '$prevRec': 0,
        '$xpos': 0, 
        '$ypos': 0,
        '$enum': 0, 
        '$snippet': '',
        '$numLen': 0.5, 
        '$snipLen': 14.5,
        '$anch': 'north west', 
        '$susp': 'south west',
        '$lenFac': 1, 
        '$opt': '',
        '$color': 'lightgray'
    }
    
    for codeline in codelines.splitlines():
        handle_codeline(codeline, vars, codeboxes)

    codeboxes[0] = utl.edit_pattern(
        codeboxes[0], '(rect1) at (0,0)', r'\((rect1)\) at \((.*?)\)')
    tikzcode = r"""\begin{tikzpicture}

    """ + ''.join(codeboxes) + r"""

    \end{tikzpicture}"""

    with open('tikz_tex/' + filename + '.tex', 'w') as tex_file:
        print(tikzcode, file=tex_file)


if __name__ == "__main__":
    for filename in filenames:
        codelines_to_blocks()

    with open('tikz_tex/solution.txt', 'w') as sol_file:
        for permutation in permutations:
            print(permutation, file=sol_file)
