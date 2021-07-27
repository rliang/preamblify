import os
import sys

with open(sys.argv[1], encoding="utf-8") as file:
    data = file.read(-1)

idx = data.find('\\begin{document}')

with open(sys.argv[1], mode='w', encoding="utf-8") as file:
    print("%&preamble", file=file)
    print(data[idx:], file=file)

with open("preamble.tex", mode='w', encoding="utf-8") as file:
    print(data[:idx], file=file)

os.system('pdflatex -ini -jobname="preamble" "&pdflatex preamble.tex\\dump"')
