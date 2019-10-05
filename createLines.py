from boxes import Boxes, bs
from lines import Lines
from lines import lines
def createLines():
    for b in bs:
        l = Lines(b)
        lines.append(l)

