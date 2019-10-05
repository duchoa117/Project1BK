from boxes import Boxes, bs
from createPlayer import playerL
def createBoxes():
    for player in playerL:
        boxes = Boxes(player)
        bs.append(boxes)