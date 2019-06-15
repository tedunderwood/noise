# USAGE:
# from within this /workflow directory:
# python WeaklyNormalizeLocalFolder2019.py folderoftexts outputfolder

# The paths in NormalizeVolume only work if you do it from
# within this directory.

import FileCabinet
import WeaklyNormalizeVolume
import sys, os, header

args = sys.argv

inputfolder = args[1]
outputfolder = args[2]

if not os.path.isdir(inputfolder):
    print("Input folder " + inputfolder + " is not a directory.")
    sys.exit(0)

if not os.path.isdir(outputfolder):
    print("Output folder " + outputfolder + " is not a directory.")
    sys.exit(0)

infiles = os.listdir(inputfolder)

already_converted = [x.replace('.tsv', '.txt') for x in os.listdir(outputfolder) if x.endswith('.tsv')]

not_yet_converted = set(infiles) - set(already_converted)

print("There are " + str(len(not_yet_converted)) + " files still to convert.")
inpaths = [os.path.join(inputfolder, x) for x in not_yet_converted if x.endswith('.txt')]

outpaths = [os.path.join(outputfolder, x).replace('.txt', '') for x in not_yet_converted if x.endswith('.txt')]

debug = False

with open('/Users/tunder/Dropbox/DataMunging/rulesets/romannumerals.txt', encoding = 'utf-8') as f:
    romannumerals = [x.strip() for x in f.readlines()]

for targetfile, outfile in zip(inpaths, outpaths):

    with open(targetfile, encoding='utf-8') as f:
        text = f.readlines()

    lines = []

    for line in text:
        line = line.strip()
        if line.startswith('<pb'):
            continue
        else:
            lines.append(line)

    unit = len(lines) // 4

    sequence = [0, unit, unit * 2, unit * 3, len(lines)]

    for i in range(4):
        theselines = lines[sequence[i]: sequence[i + 1]]

        tokens, pre_matched, pre_english, pagedata, headerlist = WeaklyNormalizeVolume.as_stream([theselines], verbose=debug)

        correct_tokens, pages, post_matched, post_english = WeaklyNormalizeVolume.correct_stream(tokens, verbose = debug)

        pagecounter = 0
        masterdict = dict()
        for page in pages:
            for item in page:
                if item in masterdict:
                    masterdict[item] += page[item]
                else:
                    masterdict[item] = page[item]

        thisoutfile = outfile + '_' + str(i) + '.fic.tsv'
        with open(thisoutfile, mode = 'w', encoding = 'utf-8') as f:
            for key, value in masterdict.items():
                if not key.startswith('#'):
                    f.write(key + '\t' + str(value) + '\n')

os.system('say "your program has finished"')
