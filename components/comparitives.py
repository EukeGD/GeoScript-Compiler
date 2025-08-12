## INFILE-LICENSE: GNU GPLv3
# -*- geoscript-compiler -*- ---------------------
#
#   Copywrite (C) EukeGD, All rights reserved
#
#   See LICENSE or README for more infomation
#
# ------------------------------------------------
#
#   file: components/comparitives.py
#
#   Header file for GeoScript comparitive statements
#
# ------------------------------------------------

EQUAL = "eq"
GREATER = "gt"
SMALLER = "st"
GREATEQ = "gq"
SMALLEQ = "sq"

AND = "and"
OR = "or"
XOR = "xor"

def embedded_comparitives(comparitive: str) -> str|None:
    return {
        "==": EQUAL,
        ">=": GREATEQ,
        ">": GREATER,
        "<": SMALLER,
        "<=": SMALLEQ,
        
        "&&": AND,
        "|": OR,
        "||": XOR
    }.get(comparitive)


class ComparitiveStatement:
    def __init__(self):
        self.complist = []
    
    def create_comparitive(self, pointer: str, comparitive: str, pointer2: str) -> None:
        self.complist.append([pointer, comparitive, pointer2])
    
    def chain_comparitive(self, chain_word: str) -> None:
        self.complist.append(chain_word)