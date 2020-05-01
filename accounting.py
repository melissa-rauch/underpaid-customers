
#Create function with parameters"orders"
def under_paid(orders):
  #establish melon cost
  melon_cost = 1.00
  #parse line in order into elements
  for line in orders:
    line = line.rstrip()
    elem = line.split("|")
    #assign variables to indexed
    name = elem[1]
    num_melons = elem[2]
    paid = elem[3]
    num_melons = float(num_melons)
    #find expected amount
    cost = num_melons * melon_cost
    #if-statement finding customers who underpaid
    if cost != paid:
      print(f"{name} paid ${paid}, expected {cost}")
  #close file
  orders.close()
#Call function, pass customer-orders document as argument
under_paid(open("customer-orders.txt"))