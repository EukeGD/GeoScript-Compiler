## INFILE-LICENSE: GNU GPLv3
# -*- geoscript-compiler -*- ---------------------
#
#   Copywrite (C) EukeGD, All rights reserved
#
#   See LICENSE or README for more infomation
#
# ------------------------------------------------
#
#   file: interface/geoscript.py
#
#   Script for the geoscript command line interface
#
# ------------------------------------------------

import sys
import os

USAGE = '''GeoScript Usage: geoscript [file] [options]'''
HELP = '''GeoScript Usage: geoscript [file] [options]
Options:
    -h | Returns this message [ alias: --help ]
    -u | Returns a usage message [ alias: --usage ]
    -v | Returns a message specifying the version [ alias: --version ]

    -o [output] | Specify the output file
    -ir | Flag allows it to only return the GSIR as an output
    -af | Flag allows it to return all used files in compilation
    -lvl | Flag allows it to only return a lvlstring as an output'''
VERSION = 'Windows x64 | GeoScript 1.0.0'

class GeoScriptMain:
    def __init__(self, argv: list[str]) -> int:
        output_file = 'level.gso'
        input_file = []
        
        output_type = 'GSO'
        all_file_out = False
        
        argv.pop(0)
        for cloc, arg in enumerate(argv):
            if arg == '-o':
                output_file = argv[cloc+1]
            elif arg == '-ir':
                output_type = 'GSIR'
            elif arg == '-af':
                all_file_out = True
            elif arg == '-lvl':
                output_type = 'LVL'
            
            elif arg in ['-h', '--help']:
                print(HELP)
                sys.exit(0)
            elif arg in ['-u', '--usage']:
                print(USAGE)
                sys.exit(0)
            elif arg in ['-v', '--version']:
                print(VERSION)
                sys.exit(0)
            
            else:
                if os.path.isfile(arg) == True:
                    input_file.append(arg)
                elif arg == output_file:
                    continue
                else:
                    print('geoscript.exe - fatal error ( 0x01 )')
                    print(f'CompilationTerminated: Argument "{arg}" does not exist')
                    sys.exit(1)
        
        if len(input_file) == 0:
            print('geoscript.exe - fatal error ( 0x01 )')
            print('CompilationTerminated: No input files')
            sys.exit(1)
        try:
            os.execve('C:/Program Files/GeoScript/geocompiler.exe', ['C:/Program Files/GeoScript/geocompiler.exe', '|$|'.join(input_file), output_file, output_type, f'{all_file_out}'], os.environ)
        except Exception:
            print('geoscript.exe - fatal error ( 0x01 )')
            print('CompilationTerminated: Cannot execute compiler ( geocompiler.exe ) file is unexecutable or does not exist')
            sys.exit(1)


if __name__ == '__main__':
    GeoScriptMain(sys.argv)