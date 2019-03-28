
##extract gtf file base on transcript name

from argparse import ArgumentParser, FileType
def extract_transcripts(gtf_file, transcript_file):
    uixo = []
    for i in transcript_file:
        uixo.append(i.strip())
    for i in gtf_file:
        if i[0]!='#':
            line = i.split()
            if (line[9][1:-2]) in uixo:
                print(i.strip())

if __name__ == '__main__':
    parser = ArgumentParser(description= 'extract transcripts form a gtf file')
    parser.add_argument('gtf_file',type=FileType('r'))
    parser.add_argument('transcriptName_file',type=FileType('r'))
    args = parser.parse_args()
    extract_transcripts(args.gtf_file,args.transcriptName_file)
