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