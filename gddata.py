## INFILE-LICENSE: GNU GPLv3
# -*- geoscript-compiler -*- ---------------------
#
#   Copywrite (C) EukeGD, All rights reserved
#
#   See LICENSE or README for more infomation
#
# ------------------------------------------------
#
#   file: components/__init__.py
#
#   File for reading the JSON data in gddata
#
# ------------------------------------------------

import json

def readJSONData() -> dict:
    with open('data/gddata.json') as file:
        return json.load(file)