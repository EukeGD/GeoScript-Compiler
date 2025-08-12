## INFILE-LICENSE: GNU GPLv3
# -*- geoscript-compiler -*- ---------------------
#
#   Copywrite (C) EukeGD, All rights reserved
#
#   See LICENSE or README for more infomation
#
# ------------------------------------------------
#
#   file: components/math.py
#
#   Header file for GeoScript math statements
#
# ------------------------------------------------

ADD = "add"
SUB = "subt"
MULT = "mult"
DIV = "div"
ADDEQ = "addeq"
SUBEQ = "subeq"
MULTEQ = "multeq"
DIVEQ = "diveq"

class MathStatements:
    def __init__(self, pointer: str, mathstate: str, pointer2: str|None) -> None:
        self.ptr = pointer
        self.mathstate = mathstate
        self.ptr2 = pointer2