'''
Created on Sep 21, 2013

@author: Rob
'''
import os

def GetFilesFromDME(dmefile='baystation12.dme', ext='.dm'):
    filesInDME=[]
    rootdir = os.path.dirname(dmefile)
    with open(dmefile, 'r') as dmeh:
        for line in dmeh:
            if line.startswith('#include'):
                inString = False
                # escaped=False
                filename = ''
                for c in line:
                    """
                    if c == '\\' and not escaped:
                        escaped = True
                        continue
                    if escaped:
                        if
                        escaped = False
                        continue
                    """         
                    if c == '"':
                        inString = not inString
                        if not inString:
                            filepath = os.path.join(rootdir, filename.replace('\\',os.sep))
                            if filepath.endswith(ext):
                                filesInDME += [filepath]
                            filename = ''
                        continue
                    else:
                        if inString:
                            filename += c
    return filesInDME
