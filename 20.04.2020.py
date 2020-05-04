
# coding: utf-8

# In[12]:


class Item (object):
    def __init__ (self,n,v,w):
        self.name=n
        self.value=v
        self.weight=w
    def getName(self):
        return self.name
    def getValue(self):
        return self.value
    def getWeight(self):
        return self.weight
    def __str__ (self):
        result=""<"+self.name+","+str(self.value)\+","+str(self.weight)+">" "
        return result


# In[13]:


def value (item):
    return item.getValue()
def weightInverse(item):
    return 1.0/item.getWeight()
def density(item):
    return item.getValue()/item.getWeight()


# In[14]:


def greedy(items,maxWeight,keyFunction):
    itemsCopy=sorted(items,key=keyFunction,reverse=True)
    result=[]
    totalValue,totalWeight=0.0,0.0
    for i in range (len(itemsCopy)):
        if (totalWeight+itemsCopy[i].getWeight())<=maxWeight:
            result.append(itemsCopy[i])
            totalWeight+=itemsCopy[i].getWeight
            totalValue+=itemsCopy[i].getValue
    return (result,totalValue)


# In[15]:


def buildItems():
    names=["lamba","telefon","saat","buzdolabı","kalem"]
    values=[81,12,44,122,5]
    weights=[2,4,5,25,1]
    Items=[]
    for i in range(len(values)):
        Items.append(Item(names[i],values[i],weights[i]))
    return Items
def testGreedy(items,maxWeight,keyFunction):
    taken,val=greedy(items,maxWeight,keyFunction)
    print("total value of items taken is",val)
    for item in taken:
        print(" ",item)
        
def testGreedys(maxWeight=25):
    items=buildItems()
    print("\n use greedy by value to fill knapsack of size",maxWeight)
    testGreedy(items,maxWeight,value)
    print("\nuse greedy by weight to fill knapsack of size",maxWeight)
    testGreedy(items,maxWeight,weightInverse)
    print("\n use greedy by density to fill knapsack of size",maxWeight)
    testGreedy(items,maxWeight,density)


# In[16]:


def chooseBest(pset,maxWeight,getVal,getWeight):
    bestVal=0.0
    bestSet=None
    for items in Pset:
        itemsVal=0.0
        itemsWeight=0.0
        for item in items:
            itemsVal+=getVal(item)
            itemsWeight+=getWeight(item)
        if itemsWeight <=maxWeight and itemsVal>bestVal:
            bestVal=itemsVal
            bestSet=items
        return (bestSet,bestVal)
def testBest(maxWeight=25):
    items=buildItems()
    pset=genPowerset(items)
    taken,val=chooseBest(pset,maxWeight,Item.getValue,Item.getWeight)
    print("total value of items taken is",val)
    for item in taken:
        print(item)
        


# In[18]:


from pprint import pprint as pp
from itertools import chain,combinations
def powerset(iterable):
    "powerset([1,2,3])-->() (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s=list(iterable)
    return chain.from_iterable(combinations(s,r) for r in range (len(s)+1))
pp(set(powerset({1,2})))

