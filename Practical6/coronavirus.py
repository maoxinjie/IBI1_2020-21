import matplotlib.pyplot as plt
labels = 'USA', 'India', 'Brazil', 'Russia', 'UK'
sizes = [29862124, 11285561, 11205972, 4360823, 4234924]
#the countries are matched with their infection cases
explode = (0, 0, 0, 0, 0)
#there is no space in the whole pie
plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=False, startangle=90)
plt.axis('equal')
plt.show()
frequency_dictionary={'USA':49.0, 'India':18.5, 'Brazil':18.4, 'Russia':7.2, 'UK':6.9}
print(frequency_dictionary)
