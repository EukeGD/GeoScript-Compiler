## INFILE-LICENSE: GNU GPLv3
# -*- geoscript-compiler -*- ---------------------
#
#   Copywrite (C) EukeGD, All rights reserved
#
#   See LICENSE or README for more infomation
#
# ------------------------------------------------
#
#   file: components/memmanager.py
#
#   Pointer allocation and identifier manager for the compiler
#
# ------------------------------------------------

NULL: dict[str, int] = {"type": ["void"], "val": 0}

class PointerAllocateManager:
    def __init__(self, max_memory: int, starting_pointer: str) -> None:
        self.maxmem = max_memory
        self.start_ptr = starting_pointer
        self.ptr_manager = { "0x0": NULL }
    
    @property
    def next_free_pointer(self) -> str:
        for i in range(0, self.maxmem, 1):
            if self.ptr_manager.get(hex(i)) == None:
                return hex(i)
    
    def allocate_pointer(self, pointer: str, binval: int, gtype: str) -> int:
        if self.ptr_manager.get(pointer) == None:
            return -1
        if len(self.ptr_manager) >= self.maxmem:
            return -2
        self.ptr_manager[pointer] = {"type": gtype, "val": binval}
        return 0
    
    def delete_pointer(self, pointer: str) -> int:
        if not self.ptr_manager.get(pointer) == None:
            return -1
        del self.ptr_manager[pointer]
        return 0
    
    def get_pointer(self, pointer: str) -> dict|int:
        if self.ptr_manager.get(pointer) == None:
            return -1
        return self.ptr_manager.get(pointer)

class IdentifierAllocateManager:
    def __init__(self) -> None:
        self.ident_manager = {}
    
    def allocate_ident(self, identifier: str, pointer: str) -> int:
        if self.ident_manager.get(identifier) == None:
            return -1
        self.ident_manager[identifier] = pointer
        return 0
    
    def get_ident_ptr(self, identifier: str) -> str|int:
        if not self.ident_manager.get(identifier) == None:
            return self.ident_manager.get(identifier)
        return -1