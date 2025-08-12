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
from components import comparitives
from components import gsmath

class SingleKeywordStatement: ...

class AllocateStatement:
    def __init__(self, pointer: str, identifier: str, gtype_statement: gtypes.VariableTypeCreator) -> None:
        self.ptr = pointer
        self.ident = identifier
        self.gtype: gtypes.VariableTypeCreator = gtype_statement

class ComparitiveIFStatement:
    def __init__(self, comparitive_statements: comparitives.ComparitiveStatement) -> None:
        self.comp_statement = comparitive_statements

class ChainedELIFStatement:
    def __init__(self, comparitive_statements: comparitives.ComparitiveStatement) -> None:
        self.comp_statement = comparitive_statements

class ChainedELSEStatement:
    def __init__(self, comparitive_statements: comparitives.ComparitiveStatement):
        self.comp_statement = comparitive_statements

class CFlowForLoop:
    def __init__(self, gtype_statement: gtypes.VariableTypeCreator, pointer: str, comparitive_statement: comparitives.ComparitiveStatement, math_statement: gsmath.MathStatements) -> None:
        self.gtype = gtype_statement
        self.ptr = pointer
        self.comp_statement = comparitive_statement
        self.math_statement = math_statement

class CFlowWhileLoop:
    def __init__(self, comparitive_statements: gtypes.VariableTypeCreator) -> None:
        self.comp_statement = comparitive_statements

class AllocateFunction:
    def __init__(self, identifier: str, args: list|None, kwargs: dict|None) -> None:
        self.ident = identifier
        self.args: dict|list|None
        self.usekwa = False
        if args == None:
            self.args = args
        elif kwargs == None:
            self.args = kwargs
            self.usekwa = True

class AllocateClass:
    def __init__(self, identifier: str, inherit_class_ident: list[str]|None) -> None:
        self.ident = identifier
        self.inherit_classes = inherit_class_ident

class ReturnStatement(SingleKeywordStatement): ...
class ContineLoop(SingleKeywordStatement): ...
class BreakLoop(SingleKeywordStatement): ...
class NonLocal(SingleKeywordStatement): ...
class GlobalStatement(SingleKeywordStatement): ...

class DefineAsync:
    def __init__(self, identifier: str) -> None:
        self.ident = identifier

class AwaitStatement:
    def __init__(self, subroutine: str) -> None:
        self.subr = subroutine
        
        
class LexerModuleSend:
    def __init__(self, module: AllocateClass|AllocateFunction|AllocateStatement|CFlowForLoop|CFlowWhileLoop|ChainedELIFStatement|ChainedELSEStatement|ComparitiveIFStatement|SingleKeywordStatement, scope: str, error: dict[str, str|int]) -> None:
        self.module = module
        self.scope = scope
        self.errorhandle = error