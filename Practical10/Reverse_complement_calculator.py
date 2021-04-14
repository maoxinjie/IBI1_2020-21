import re
def reverse_complement(seq):
    seq = seq.lower()
    complement1=re.sub(r'a',r'T',seq)
    complement2=re.sub(r't',r'A',complement1)
    complement3=re.sub(r'c',r'G',complement2)
    complement4=re.sub(r'g',r'C',complement3)
    reverse=complement4[::-1]
    return reverse
seq = 'ATgcTgaa'
print(reverse_complement(seq))
# or
# def reverse_complement(seq):
#   seq = seq.lower()
#   complement=seq.replace('a','T')
#   complement=complement.replace('t','A')
#   complement=complement.replace('c','G')
#   complement=complement.replace('g','C')
#   reverse=complement[::-1]
#   return reverse
a = input()
seq = str(a)
print(reverse_complement(seq))