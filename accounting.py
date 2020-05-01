melon_cost = 1.00
#Create function with parameters"orders"
def under_paid(orders):
  #establish melon cost

  #parse line in order into elements
  for line in orders:
    line = line.rstrip()
    elem = line.split("|")
    #assign variables to indexed
    name = elem[1]
    num_melons = float(elem[2])
    paid = float(elem[3])

    #find expected amount
    cost = num_melons * melon_cost
    #print what customers paid and expected amts
    print(f"{name} paid ${paid}, expected ${cost}0.")
    #if-statement finding customers who overpaid
    if cost != paid:
      if cost < paid:
        payment_status = ("OVERPAID")
      #if-statement finding customers who underpaid
      elif cost > paid:
        payment_status = ("UNDERPAID") 
      print(f"{name} has {payment_status}.")
  #close file
  orders.close()
#Call function, pass customer-orders document as argument
under_paid(open("customer-orders.txt"))