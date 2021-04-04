import re
a = input()
b = open('output.fa', 'w')
A = open(a, 'r')
genes = {'TTT':'F', 'TCT':'S', 'TAT':'Y', 'TGT':'C',
'TTC':'F', 'TCC':'S', 'TAC':'Y', 'TGC':'C',
'TTA':'L', 'TCA':'S', 'TAA':'O', 'TGA':'X',
'TTG':'L', 'TCG':'S', 'TAG':'U', 'TGG':'W',
'CTT':'L', 'CCT':'P', 'CAT':'H', 'CGT':'R',
'CTC':'L', 'CCC':'P', 'CAC':'H', 'CGC':'R',
'CTA':'L', 'CCA':'P', 'CAA':'Q', 'CGA':'R',
'CTG':'L', 'CCG':'P', 'CAG':'Z', 'CGG':'R',
'ATT':'I', 'ACT':'T', 'AAT':'N', 'AGT':'S',
'ATC':'I', 'ACC':'T', 'AAC':'B', 'AGC':'S',
'ATA':'J', 'ACA':'T', 'AAA':'K', 'AGA':'R',
'ATG':'M', 'ACG':'T', 'AAG':'K', 'AGG':'R',
'GTT':'V', 'GCT':'A', 'GAT':'D', 'GGT':'G',
'GTC':'V', 'GCC':'A', 'GAC':'D', 'GGC':'G',
'GTA':'V', 'GCA':'A', 'GAA':'E', 'GGA':'G',
'GTG':'V', 'GCG':'A', 'GAG':'E', 'GGG':'G',}
protein = ''
recording = False
protein_map = {}
cur_seq = ""
gene_name = ""
for line in A:
    if  line.startswith('>'):
        if recording:
            protein_map[gene_name] = cur_seq
        recording = 'unknown function' in line
        gene_name = re.findall(r'gene:(\S+)', line)[0]
        cur_seq = ""
    elif recording:
        for i in range(0, len(line)-1, 3):
            # the \n is one character, so it is len(line)-1
            cur_seq = cur_seq + genes[line[i:(i+3)]]
for gene_name, cur_seq in protein_map.items():
    print(f'{gene_name:15}  {len(cur_seq)}\n{cur_seq}')
    b.write(f'{gene_name:15}  {len(cur_seq)}\n{cur_seq}\n')
b.close()