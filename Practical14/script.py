from xml.dom.minidom import parse
import xml.dom.minidom
import matplotlib.pyplot as plt
import numpy as np

# input the DOMTree
DOMTree = xml.dom.minidom.parse("go_obo.xml")
collection = DOMTree.documentElement
terms = collection.getElementsByTagName('term')

isMacro={'DNA':{}, 'RNA':{}, 'protein':{}, 'carbohydrate':{}}
idMap = {}
def hasMacro(cur_id, Macro):
    # if already searched, return result directly
    if cur_id in isMacro[Macro]:
      return isMacro[Macro][cur_id]
    
    # if cur defstr has term, store the result and return
    defstr = idMap[cur_id].getElementsByTagName('defstr')[0].childNodes[0].nodeValue
    if Macro in defstr:
        isMacro[Macro][cur_id] = True
        return True

    # recursively searching its parents until one contains Macro or all is searched
    for parent in idMap[cur_id].getElementsByTagName('is_a'):
        if hasMacro(parent.childNodes[0].nodeValue, Macro):
            isMacro[Macro][cur_id] = True
            break
    
    # if not found Macro in any of its parent, set the result to false
    if not cur_id in isMacro[Macro]:
      isMacro[Macro][cur_id] = False

    #return the result
    return isMacro[Macro][cur_id]

# set the initial lists 
DNAlist = []
RNAlist = []
proteinlist = []
carbolist = []

for term in terms:
  idMap[term.getElementsByTagName('id')[0].childNodes[0].nodeValue] = term

# get all GO_id that contain the macromolecules
for term in terms:
    if hasMacro(term.getElementsByTagName('id')[0].childNodes[0].data, 'DNA'):
        DNAlist.append(term.getElementsByTagName('id')[0].childNodes[0].data)
    if hasMacro(term.getElementsByTagName('id')[0].childNodes[0].data, 'RNA'):
        RNAlist.append(term.getElementsByTagName('id')[0].childNodes[0].data)
    if hasMacro(term.getElementsByTagName('id')[0].childNodes[0].data, 'protein'):
        proteinlist.append(term.getElementsByTagName('id')[0].childNodes[0].data)
    if hasMacro(term.getElementsByTagName('id')[0].childNodes[0].data, 'carbohydrate'):
        carbolist.append(term.getElementsByTagName('id')[0].childNodes[0].data)

print('DNAchildnodes: ', len(DNAlist))
print('RNAchildnodes: ', len(RNAlist))
print('proteinchildnodes: ', len(proteinlist))
print('carbohydratechildnodes: ', len(carbolist))

# paint the pie chart
labels = ['DNA','RNA','protein','carbohydrate']
sizes = [len(DNAlist),len(RNAlist),len(proteinlist),len(carbolist)]
explode = (0,0,0,0.1)
plt.pie(sizes,explode=explode,labels=labels,autopct='%1.1f%%',shadow=True,startangle=150)
plt.title('the number of childNodes of Macromolecules')
plt.show()

