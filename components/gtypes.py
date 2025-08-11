## INFILE-LICENSE: GNU GPLv3
# -*- geoscript-compiler -*- ---------------------
#
#   Copywrite (C) EukeGD, All rights reserved
#
#   See LICENSE or README for more infomation
#
# ------------------------------------------------
#
#   file: components/gtypes.py
#
#   Header file for GeoScript memory types
#
# ------------------------------------------------

INT64 = "int64"
LONG64 = "long64"
SHORT64 = "short64"
FLOAT64 = "float64"
CHARASCII = "char"
CHARUNICODE = "charuni"
BOOL64 = "bool64"

STATIC = "static"
VOLITILE = "volit"
UNSIGNED = "unsigned"
SIGNED = "signed"
POINTER = "ptr"

def embedded_gtype(keyword: str) -> str:
    return {
        "int": INT64,
        "long": LONG64,
        "short": SHORT64,
        "float": FLOAT64,
        "char": CHARASCII,
        "cuni": CHARUNICODE,
        "bool": BOOL64,
        "static": STATIC,
        "volitile": VOLITILE,
        "unisgned": UNSIGNED,
        "signed": SIGNED,
        "*": POINTER
    } [keyword]

class VariableTypeCreator:
    def __init__(self) -> None:
        self.typecat = []
        self.TYPES_CANNOT_MERGE = 1
        self.FAILED = 0
        self.SUCSESS = 2

    def set_allocation_type(self, constant_alloc: bool) -> int:
        if constant_alloc == True:
            self.typecat.append("constant")
        else:
            self.typecat.append("variable")
        return self.SUCSESS

    def set_type_specifier(self, type_constant: str) -> int:
        mtyc = 0
        for i in self.typecat:
            if i in [INT64, BOOL64, FLOAT64, CHARASCII, CHARUNICODE]:
                mtyc += 1
        if mtyc > 1:
            return self.TYPES_CANNOT_MERGE
        mtyc = 0
        for i in self.typecat:
            if i in [STATIC, VOLITILE]:
                mtyc += 1
        if mtyc > 1:
            return self.TYPES_CANNOT_MERGE
        mtyc = 0
        for i in self.typecat:
            if i in [UNSIGNED, SIGNED]:
                mtyc += 1
        if mtyc > 1:
            return self.TYPES_CANNOT_MERGE

        self.typecat.append(type_constant)

    def lock_and_return_type(self) -> list:
        return self.typecat
