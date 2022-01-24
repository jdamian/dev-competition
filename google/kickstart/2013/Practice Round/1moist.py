t = int(input())

for i in range(1, t + 1):
  n = int(input())
  cost = 0

  for j in range(0,n):

    line = input()

    if j==0:
      deck = [line]
      continue    

    for k in range(len(deck),0,-1):
      if k==1:                        # compare the first  element
        if line < deck[0] :
          deck.insert(0,line)
          cost += 1

      if deck[len(deck)-1] < line and k==len(deck):            # compara el ultimo elemento
        deck.insert(k,line)
        break

      if line < deck[k-1] and line > deck[k-2]:            # compara el ultimo elemento
        deck.insert(k-1,line)
        cost += 1
        break

  print("Case #{}: {}".format(i, cost))
  # print(deck)