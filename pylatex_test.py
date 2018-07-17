import os
from pylatex import Document, PageStyle, Head, Foot, Section, Subsection, Tabular, Math, TikZ, Axis, \
    Plot, Figure, Matrix, Alignat, StandAloneGraphic, MiniPage, LineBreak, Center, Command
from pylatex.utils import italic, bold, NoEscape

image_filename = os.path.join(os.path.dirname(__file__), 'Invoices\sus_header.png')
geometry_options = {"tmargin": "1cm", "lmargin": "1cm"}
doc = Document(geometry_options=geometry_options)

with doc.create(Figure(position='h!')) as sus_pic:
    sus_pic.add_image(image_filename, width='550px')

doc.append(Command('noindent'))
doc.append(Command('textbf', 'asdasdasd'))
doc.append(Command('linebreak'))
doc.append(Command('textbf', 'asdasdasd'))

doc.generate_pdf('test', clean_tex=False, compiler='pdflatex')
