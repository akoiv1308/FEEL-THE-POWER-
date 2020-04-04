import random
import matplotlib.pyplot as plt

def avgList(simList):
  sum = 0
  for i in range(len(simList)):
    sum += simList[i]
  return (sum/len(simList))

finalvalue = []
more = 0
less = 0

for g in range(1000):
  myData = []
  for i in range(15):
    first = random.randint(0,9)
    second = random.randint(0,9)  
    if first > second:
      final = str(first) + str(second)
      print(final)
    elif second > first:
      final = str(second) + str(first)
    elif first == second:
      final = str(second) + str(first)
      
    myData.append(int(final))

  if avgList(myData) >= 70:
    more += 1
  else:
    less += 1
    
  finalvalue.append(avgList(myData))
print(finalvalue)


labels = 'Average more than 70', 'Average less than 70'
sizes = [more, less]

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
ax1.axis('equal')
plt.savefig('graph.png')