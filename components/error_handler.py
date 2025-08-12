## INFILE-LICENSE: GNU GPLv3
# -*- geoscript-compiler -*- ---------------------
#
#   Copywrite (C) EukeGD, All rights reserved
#
#   See LICENSE or README for more infomation
#
# ------------------------------------------------
#
#   file: components/error_handler.py
#
#   Header file for how GeoScript handles errors
#
# ------------------------------------------------

import sys

def __safeexit__():
    sys.exit(1)
class ErrorType: ...


class TypeMergeError(ErrorType): ...


class HandleErrorCase:
    def __init__(self, error: ErrorType, desc: str, file: str|None, linenum: int|None, line: str|None, highlight_index: list|None) -> None:
        self.file = file
        self.ln = linenum
        self.line = line
        self.error: ErrorType = error
        self.desc = desc
        self.highlight = highlight_index
    
    def throw(self) -> None:
        print(f"{self.error.__name__}: {self.desc}")
        __safeexit__()
    
    def throw_with_traceback(self) -> None:
        print(f'File {self.file}, line {self.ln}')
        print(f'  {self.line}')
        
        print('  ', end='')
        for _ in range(self.highlight[0]):
            print(' ', end='')
        for _ in range(self.highlight[1]):
            print('^', end='')
        print('\n')
        
        print(f'{self.error.__name__}: {self.desc}')
        __safeexit__()