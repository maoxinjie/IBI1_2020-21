import matplotlib.pyplot as plt
labels = 'USA', 'India', 'Brazil', 'Russia', 'UK'
sizes = [29862124, 11285561, 11205972, 4360823, 4234924]
#the countries are matched with their infection cases
a=sum(sizes)
explode = (0, 0, 0, 0, 0)
#there is no space in the whole pie
plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=False, startangle=90)
plt.axis('equal')
plt.title('Comparing coronavirus infection rates across countries')
plt.show()
frequency_dictionary={'USA':sizes[0]/a, 'India':sizes[1]/a, 'Brazil':sizes[2]/a, 'Russia':sizes[3]/a, 'UK':sizes[4]/a}
print(frequency_dictionary)
