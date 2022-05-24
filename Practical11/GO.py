from xml.dom.minidom import parse
import xml.dom.minidom
import matplotlib.pyplot as plt
from numpy import*


DOMTree =xml.dom.minidom.parse("go_obo.xml")
collection = DOMTree.documentElement
terms= collection.getElementsByTagName("term")
print('the total number of terms:', terms.length) # to show the total number of terms


dic={}#key：term id data，value：direct parents id data
dic_result={}#key：term id data， value：childNodes number
if_tra=[]#mark for each term. Marking whether it is assosicated with translation
tran_result=[]#
average_list=[]

#For every term, put all parentNodes into a set.
def fun(now_id,parent):
    pa_now=dic[now_id]#find direct parents id data 
    if len(pa_now):#if have direct parents
        for j in pa_now:#each direct parent put into a set called parent
            parent.add(j)
            fun(j,parent)#nest, find direct parent's parents until all are included

#dic, key：term id data & value：direct parents id data
for term in terms:
    ids=term.getElementsByTagName('id')[0].childNodes[0].data#find term id data
    is_a_id=[]# store direct parents
    for is_a in term.getElementsByTagName('is_a'):
        is_a_id.append(is_a.childNodes[0].data)#find term <is_a> id data
    dic[ids]=is_a_id
# dic_result key ：term id data， value：childNodes number
    dic_result[ids]=0
#judge each term, whether it is associated with translation.
    if term.getElementsByTagName("defstr")[0].childNodes[0].data.find("translation"or"Translation")!=-1:
        if_tra.append("yes")#mark the term with a list (contain "yes" or "no")
    else:
        if_tra.append("no")

# dic_result key ：term id data， value：childNodes number
for key in dic.keys():
    
    parent=set()#one set for each term, containing the term's all parentNodes
    fun(key,parent)
# Parent term id's childnode number +1
    for k in parent:
        dic_result[k]+=1

#
for i,(k,v)in enumerate(dic_result.items()):
    average_list.append(v)
    if if_tra[i]=="yes":
#If a term is associated with translation, its childnodes number will be add to this list
        tran_result.append(v)
        
            
            


# draw the boxplot of all terms and terms related to translation
plt.boxplot(dic_result.values(),vert=True,whis=1.5,patch_artist=True,notch=False)
plt.title('Distribution of child nodes across terms')
plt.xlabel("all terms in GO")
plt.ylabel('childNodes number')
plt.show()

plt.boxplot(tran_result,vert=True,whis=1.5,patch_artist=True,notch=False)
plt.title('Distribution of child nodes across terms associated with translation')
plt.xlabel('terms related to translation')
plt.ylabel('childNodes number')
plt.show()

#judge whether 'translation'terms contain more childNodes than overall GO
ave=mean(average_list)
ave_tr=mean(tran_result)
if ave>ave_tr:
    print("The translation terms contain, on average, a smaller number	of child nodes than the	overall	Gene Ontology.")
else:
    print("The translation terms contain, on average, a greater number	of child nodes than the	overall	Gene Ontology.")







