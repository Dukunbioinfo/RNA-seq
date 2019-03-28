from argparse import ArgumentParser, FileType
# fin1 = open(r'D:\rabbit_adyposite\diffExp\lncRNA\d3vsd0.MSTRG','r').readlines()
# fin2 = open(r'D:\rabbit_adyposite\diffExp\lncRNA\d9vsd0.MSTRG','r').readlines()
def unionMSTRG(fin1,fin2):
    a=[]
    for i in fin1:
        a.append(i.strip())
    b=[]
    for i in fin2:
        b.append(i.strip())
    union= list(set(a).union(set(b)))
    for i in union:
        print(i)

if __name__ == '__main__':
    parser = ArgumentParser(description= 'extract transcripts form a gtf file')
    parser.add_argument('MSTRG1',type=FileType('r'))
    parser.add_argument('MSTRG2',type=FileType('r'))
    args = parser.parse_args()
    unionMSTRG(args.MSTRG1,args.MSTRG2)
