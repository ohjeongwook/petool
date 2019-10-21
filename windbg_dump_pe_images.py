

if __name__ == '__main__':
    import os
    import sys
    sys.path.append(os.path.join(os.path.dirname(os.__file__), 'site-packages'))

    import petool
    import pykd

    pattern = 'test'
    filename= "output.dmp"
    tmp_filename = filename+".tmp"

    lm_lines = pykd.dbgCommand("lm")
    for line in lm_lines.splitlines():
        toks = line.split()
        
        if len(toks) >= 3:
            if toks[2] == pattern:
                (start, end) = toks[0:2]
                start = int(start, 16)
                end = int(end, 16)

                pykd.dbgCommand(".writemem %s %x L?%x" % (tmp_filename, start, end-start))
                pykd.dbgCommand("q")

    pe_file = petool.PEFile(tmp_filename)
    pe_file.FixPointerToRaw()
    pe_file.Write(filename)
