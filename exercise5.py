belove = 0.10
above = 0.25
less = int(input("Enter amount of contaniers less than one litre: "))
more = int(input("Enter amount of contaniers more than one litre: "))
refund = belove*less + above*more

print("Your Refund is=","{}$".format(refund))
