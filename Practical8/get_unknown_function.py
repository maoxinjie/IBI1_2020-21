import re
a = open('unknown_function.fa', 'w')
Saccharomyces = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r')
recording = False
gene_map = {}
gene_name = ""
gene_sequence = ""
# set the initial dictionary and list
for line in Saccharomyces:
    if  line.startswith('>'):
        # select each gene for it begins with a ">"
        if recording:
            gene_map[gene_name] = gene_sequence
            # in the dictionary 'gene_map', gene_name is related to the gene_sequence 
        recording = 'unknown function' in line
        # select the gene with unknown function
        gene_name = re.findall(r'gene:(\S+)', line)[0]
        # find all the gene_name
        gene_sequence = ""
    elif recording:
        for i in range(0, len(line)-1):
            # the '\n' is one character, so I set the range between 0 to len(line)-1
            gene_sequence = gene_sequence + line[i:i+1]
for gene_name, gene_sequence in gene_map.items():
    print(f'{gene_name:15}  {gene_sequence}')
    # set the space of 15 character.
    a.write(f'{gene_name:15}  {gene_sequence}\n')
a.close()
