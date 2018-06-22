from apyori import apriori

transactions = [
    ['beer', 'nuts'],
    ['beer', 'cheese'],
]
results = list(apriori(transactions))


print (len(results))
print (results[0])
print (results[1])
print (results[2])
print (results[3])
print (results[4])