# RNA-seq
## genes expression explore based on high through-put sequencing data.
### extract.py
Base on the file contain transcript name, extract transcript (transcript line and it's exon line ) from a gtf file.
usage: extractGTF.py gtf_file transcriptName_file
### interSect2Cols.py
calculate intersection of two col, for instance, A file: a col of transcrip name; B: a col of transcript.
### transformMSTRG2ENSBL.py
Stringtie style transcript name to Esembl style name (if exist in Esemble).
### union2Cols.py
Calculate union of two col, for instance, A file: a col of transcrip name; B: a col of transcript.
### hopmapCluster.py
Cluster samples based on defferentially express transcripts FPKM.
