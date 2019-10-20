from pykd import *
import petool

if __name__ == '__main__':
    import sys

    pattern = 'test'
    filename= sys.argv[1]
    tmp_filename = filename+".tmp"

    lm_lines = dbgCommand("lm")
    for line in lm_lines.splitlines():
        toks = line.split()
        
        if len(toks) >= 3:
            if toks[2] == pattern:
                (start, end) = toks[0:2]
                start = int(start, 16)
                end = int(end, 16)
                
                dbgCommand(".writemem %s %x L?%x" % (tmp_filename, start, end-start))
                dbgCommand("q")

	pe_file = petool.PEFile(tmp_filename)
	pe_file.FixPointerToRaw()
	pe_file.Write(filename)
