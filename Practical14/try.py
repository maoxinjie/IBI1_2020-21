from xml.dom.minidom import parse
import xml.dom.minidom
import matplotlib.pyplot as plt
import numpy as np

DOMTree = xml.dom.minidom.parse("go_obo.xml")
# input the DOMTree
collection = DOMTree.documentElement
terms = collection.getElementsByTagName('term')

def differentdefstr(terms, macromolecule):
    moleculelist = []
    for term in terms:
        defstr = term.getElementsByTagName('defstr')[0].childNodes[0].data
        term_id = term.getElementsByTagName('id')[0].childNodes[0].data
        if macromolecule in defstr:
            moleculelist.append(term_id)
    return moleculelist
# define a function called differrentdefstr to add the term that relates to the macromolecule we want into a list called moleculelist.
# so we can find a list that contains all the term_id that relate to the macromolecule
DNAlist = differentdefstr(terms, 'DNA')
RNAlist = differentdefstr(terms, 'RNA')
proteinlist = differentdefstr(terms, 'protein')
carbolist = differentdefstr(terms, 'carbohydrate')


molecule_id_dict = {'DNA':DNAlist, 'RNA':RNAlist, 'protein':proteinlist, 'carbohydrate':carbolist}
allChildren = {}
D_match_id = []
R_match_id = []
P_match_id = []
C_match_id = []
for term in terms:
    is_a = term.getElementsByTagName('is_a')[0].childNodes[0].data
    term_id = term.getElementsByTagName('id')[0].childNodes[0].data
    allChildren[term_id] = is_a
    if is_a in DNAlist:
        D_match_id.append(term_id)
print(D_match_id)