## INFILE-LICENSE: GNU GPLv3
# -*- geoscript-compiler -*- ---------------------
#
#   Copywrite (C) EukeGD, All rights reserved
#
#   See LICENSE or README for more infomation
#
# ------------------------------------------------
#
#   file: components/lexer_modules.py
#
#   Header file for the lexer
#
# ------------------------------------------------

from components import gtypes

class AllocateStatement:
    def __init__(self, pointer: str, identifier: str, gtype_statement: gtypes.VariableTypeCreator):
        self.ptr = pointer
        self.ident = identifier
        self.gtype: gtypes.VariableTypeCreator = gtype_statement