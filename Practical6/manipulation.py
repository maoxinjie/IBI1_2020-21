import numpy as np
gene_lengths=np.array([9410,394141,4442,105338,19149,76779,126550,36296,842,14981])
exon_counts=np.array([51,1142,42,316,25,650,32533,57,1,523])
average_exon_length= gene_lengths / exon_counts
#measure the average exon length across all 10 genes
average_exon_length.sort()
#sort the values for the average exon length across all 10 genes
print(average_exon_length)
import matplotlib.pyplot as plt
plt.title('the distribution of average exon length')
plt.boxplot(average_exon_length, patch_artist = True, boxprops = {'color':'orangered','facecolor':'pink'})
plt.show()

