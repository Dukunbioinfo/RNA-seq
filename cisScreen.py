from argparse import ArgumentParser, FileType
#fin1 = open(r'D:\rabbit_adyposite\diffExp\lncRNA\cis_target\upstream.reasult','r').readlines()
def cis(winbed_stdr):    
    mapping = {}
    for i in winbed_stdr:
        line = i.split()
        if line[3] not in mapping.keys():
            mapping[line[3]] = [line[7]]
        else:
            mapping[line[3]].append(line[7])
    for key in mapping:
        if len(mapping[key]) <= 1:
            for i in mapping[key]:
                print(i)
        else:
            for i in mapping[key][0:1]:
                print(i)

if __name__ == '__main__':
    parser = ArgumentParser(description= 'extract transcripts form a gtf file')
    parser.add_argument('winbed_stdr',type=FileType('r'))
    args = parser.parse_args()
    cis(args.winbed_stdr)
