from argparse import ArgumentParser, FileType
# fin = open(r'D:\rabbit_adyposite\quality\mRNAInsample.gtf','r').readlines()
# need = open(r'D:\rabbit_adyposite\diffExp\mRNA\d.MSTRG','r').readlines()
def transform(gtf_file, MSTRG):
    a = {}
    for i in gtf_file:
        line = i.split()
        if line[2] == 'transcript':
            a[line[11][1:-2]] = line[17][1:-2]
    for i in MSTRG:
        print(a[i.strip()])

if __name__ == '__main__':
    parser = ArgumentParser(description= 'extract transcripts form a gtf file')
    parser.add_argument('gtf_file',type=FileType('r'))
    parser.add_argument('MSTRG',type=FileType('r'))
    args = parser.parse_args()
    transform(args.gtf_file,args.MSTRG)
