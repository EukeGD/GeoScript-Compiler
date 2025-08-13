## INFILE-LICENSE: GNU GPLv3
# -*- geoscript-compiler -*- ---------------------
#
#   Copywrite (C) EukeGD, All rights reserved
#
#   See LICENSE or README for more infomation
#
# ------------------------------------------------
#
#   file: preprocessor.py
#
#   Script for handling preprocessor and data keywords
#
# ------------------------------------------------

import gddata as gdata
from components import error_handler
import json
import sys

class InvalidDataTagKeyword(error_handler.ErrorType): ...
class InvalidPreprocessorKeyword(error_handler.ErrorType): ...

class ParseForSingleFile:
    def __init__(self, file: str, string: str) -> None:
        self.file = file
        self.gddata = gdata.readJSONData()
        self.filelist = string.splitlines()
            
        self.datatags = {
            'ips': 30,
            'maxgroups': 9999,
            'maxver': '2.207',
            'minver': '2.200',
            'targetver': '2.207'
        }
        self.preprocessor_data: dict[dict, list, dict[list, list]] = {
            'macro': {},
            'controll-flow': {
                'start': [],
                'end': []
            }
        }
            
        for ln, line in enumerate(self.filelist):
            self.check_data_tags(line, ln)
            self.preprocessor_keywords(line, ln)
            
    def check_data_tags(self, line: str, ln: int) -> None:
        if line.startswith('@') == True:
            if line.startswith('@ips:') == True:
                line = line.removeprefix('@ips:')
                line = line.removeprefix(' ')
                self.datatags['ips'] = int(line)
            elif line.startswith('@maxgroups:') == True:
                line = line.removeprefix('@maxgroups:')
                line = line.removeprefix(' ')
                self.datatags['maxgroups'] = int(line)
            elif line.startswith('@maxver:') == True:
                line = line.removeprefix('@maxver:')
                line = line.removeprefix(' ')
                self.datatags['maxver'] = line
            elif line.startswith('@minver:') == True:
                line = line.removeprefix('@minver:')
                line = line.removeprefix(' ')
                self.datatags['minver'] = line
            elif line.startswith('@targetver:') == True:
                line = line.removeprefix('@targetver:')
                line = line.removeprefix(' ')
                self.datatags['targetver'] = line
                
                if self.gddata['gd-data']['version'] == line:
                    print(f'{self.file}, line {ln}')
                    print(f'  {line}\n')
                    print(f'VersionWarning: Script target version {line} does not match the version listed in gddata.json {self.gddata['gd-data']['version']} | This could cause issues or crashes upon opening the level')
            else:
                error_handler.HandleErrorCase(InvalidDataTagKeyword, f'Data tag "{line}" doesnt exist', self.file, ln, line, [0, len(line)]).throw_with_traceback()
    
    def preprocessor_keywords(self, line: str, ln: int) -> None:
        if line.startswith('#') == True:
            if line.startswith('#define ') == True:
                line = line.removeprefix('#define ')
                if ' ' in line:
                    line = line.split(' ')
                    self.preprocessor_data['macro'][line[0]] = line[1]
                else:
                    self.preprocessor_data['macro'][line] = None
            elif line.startswith('#ifdef ') == True:
                line = line.removeprefix('#ifdef ')
                self.preprocessor_data['controll-flow']['start'].append({'start': ln, 'macro': line, 'expected': '§GSDEFINED'})
            elif line.startswith('#ifndef ') == True:
                line = line.removeprefix('#ifndef ')
                self.preprocessor_data['controll-flow']['start'].append({'start': ln, 'macro': line, 'expected': '§GSUNDEFINED'})
            elif line.startswith('#if ') == True:
                line = line.removeprefix('#if ')
                line = line.split(' ')
                self.preprocessor_data['controll-flow']['start'].append({'start': ln, 'macro': line[0], 'expected': line[1]})
            elif line.startswith('#endif') == True:
                self.preprocessor_data['controll-flow']['end'].append(ln)



def main(file: str) -> None:
    with open(file) as rstream:
        sublines = -1
        gddata = gdata.readJSONData()
        usedfiles = [file]
        stringstream = rstream.read()
            
        while True:
            for line in stringstream.splitlines():
                if line.startswith('#include ') == True:
                    line = line.removeprefix('#include ')
                    
                    if line.startswith('<') == True:
                        line = line.removeprefix('<')
                        line = line.removesuffix('>')
                        
                        if not f'{gddata['geoscript']['stdlib-dir']}/{line}' in usedfiles:
                            with open(f'{gddata['geoscript']['stdlib-dir']}/{line}') as libstream:
                                usedfiles.append(f'{gddata['geoscript']['stdlib-dir']}/{line}')
                                stringstream.replace(f'#include <{line}>', libstream.read())
                    if line.startswith('"') == True:
                        line = line.removeprefix('"')
                        line = line.removesuffix('"')
                        
                        if not f'{gddata['geoscript']['stdlib-dir']}/{line}' in usedfiles:
                            with open(f'./{line}') as libstream:
                                usedfiles.append(f'./{line}')
                                stringstream.replace(f'#include "{line}"', libstream.read())
            break
        
        parsedfile = ParseForSingleFile(file, stringstream)
        for macro in parsedfile.preprocessor_data['macro']:
            if not parsedfile.preprocessor_data['macro'][macro] == None:
                stringstream = stringstream.replace(macro, parsedfile.preprocessor_data['macro'][macro])
        
        for num, ctrlflow in enumerate(parsedfile.preprocessor_data['controll-flow']['start']):
            if ctrlflow['expected'] == '§GSDEFINED':
                if not parsedfile.preprocessor_data['macro'].get(ctrlflow['macro']) == None:
                    rmlines = stringstream.splitlines()
                    for i in range(ctrlflow['start'], parsedfile.preprocessor_data['controll-flow']['end'][num]):
                        rmlines.pop(i-(i-ctrlflow['start'])-sublines)
                        sublines += 1
                    stringstream = '\n'.join(rmlines)
            elif ctrlflow['expected'] == '§GSUNDEFINED':
                if parsedfile.preprocessor_data['macro'].get(ctrlflow['macro']) == None:
                    rmlines = stringstream.splitlines()
                    for i in range(ctrlflow['start'], parsedfile.preprocessor_data['controll-flow']['end'][num], 1):
                        rmlines.pop(i-(i-ctrlflow['start'])-sublines)
                        sublines += 1
                    stringstream = '\n'.join(rmlines)
            else:
                if not parsedfile.preprocessor_data['macro'].get(ctrlflow['macro']) == ctrlflow['expected']:
                    rmlines = stringstream.splitlines()
                    for i in range(ctrlflow['start'], parsedfile.preprocessor_data['controll-flow']['end'][num]):
                        rmlines.pop(i-(i-ctrlflow['start'])-sublines)
                        sublines += 1
                    stringstream = '\n'.join(rmlines)
        
        with open('datatags.json', 'w') as wstrm:
            json.dump(parsedfile.datatags, wstrm)
        
        with open('preprocessed.gsi', 'w') as wstrm:
            wstrm.write(stringstream)
        
        exit(0)

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('No file to parse')
        exit(1)
    main(sys.argv[1])