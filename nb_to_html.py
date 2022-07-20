import os
import re
import nbformat
import nbconvert

PART = 4


# notebooks = []
# for root, subdirs, files in os.walk(f'.\\Part {PART}'):
#     for file in files:
#         if file.endswith('ipynb'):
#             notebooks.append((root + '\\'  + file))
# parts = [x.split('\\',maxsplit=3) for x in notebooks]
# merged_nb = nbformat.v4.new_notebook()
# merged_nb.cells = []
# last_section = None
# for dot, part, section, file in parts:
#     nbfpath = '\\'.join([part, section, file])
#     print(part, section, file)
#     if last_section != section:
#         merged_nb.cells.extend([nbformat.v4.new_markdown_cell('# ' + section)])
#         last_section = section
#     input_cells = nbformat.read(nbfpath, 4).cells
#     # adjust first input to match 2level header
#     input_cells[0]['source'] = re.sub(pattern='#+', repl='## ', string=input_cells[0]['source'])
#     merged_nb.cells += input_cells
# nbformat.write(merged_nb, f'merged_Part{PART}.ipynb')

[
    'merged_Part1.ipynb',
    'merged_Part2.ipynb',
    'merged_Part3.ipynb',
    'merged_Part4.ipynb'
]
exporter = nbconvert.MarkdownExporter()
