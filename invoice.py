import os
import pylatex as pl

geometry_options = {"tmargin": "1cm", "lmargin": "1cm"}
doc = Document(geometry_options=geometry_options)

with doc.create(Subsection(' ')):
        with doc.create(Figure(position='h!')) as header_pic:
            sus_pic.add_image(image_filename, width='120px')
