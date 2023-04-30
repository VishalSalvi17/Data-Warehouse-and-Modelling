import itertools

minSupport = int(input("Enter Support: "))

n = int(input("Enter the number of transactions: "))
print("------------------------------")

transactions = {}

for i in range(n):
    transactions[i] = []

for i in range(n):
    itemno = int(input("Enter number of items in transaction: " + str(i + 1) + "\n"))
    for no in range(itemno):
        transactions[i].append(int(input("Enter item " + str(no + 1) + " : ")))

support = {}

for i in range(n):
    for j in range(len(transactions[i])):
        if transactions[i][j] not in support:
            support[transactions[i][j]] = 1
        else:
            support[transactions[i][j]] += 1

print("------------------------------")
print("Support:", support)

todelete = []
for k, v in support.items():
    if v < minSupport:
        todelete.append(k)

for d in todelete:
    del support[d]

print("Support 1 item:", support)

archive = support.copy()

temp = list(support.keys())

itemListCount = 2

supportTemp = {}

while itemListCount < 5:
    list1 = list(itertools.combinations(temp, itemListCount))
    list2 = []

    for i in range(len(list1)):
        list2.append(0)

    count = 0
    for i in list1:
        for j in range(len(transactions.keys())):
            if all(elem in transactions[j] for elem in i):
                list2[count] += 1
        count += 1

    support2 = {}
    for i in range(len(list2)):
        support2[list1[i]] = list2[i]

    todelete = []
    for k, v in support2.items():
        if v < minSupport:
            todelete.append(k)

    for d in todelete:
        del support2[d]

    print("Support", itemListCount, "items:", support2)
    
    itemListCount += 1

    if not support2:
        break

    supportTemp = support2.copy()

    if not archive:
        archive = support2.copy()
    else:
        archive.update(support2)

assRule = {}

for key, value in supportTemp.items():
    for i in key:
        newList1 = []
        newList2 = []
        tup = []
        newList1.append(i)
        for j in key:
            if i == j:
                continue
            else:
                tup.append(j)
        newList1.append(tuple(tup))
        newList2.append(tuple(tup))
        newList2.append(i)

        assRule[tuple(newList1)] = round((archive[key] / archive[i]) * 100, 2)

        if len(tup) == 1:
            assRule[tuple(newList2)] = round((archive[key] / archive[tup[0]]) * 100, 2)
        else:
            assRule[tuple(newList2)] = round((archive[key] / archive[tuple(tup)]) * 100, 2)

print("------------------------------")
print("Association Rules :\n",assRule)