def calculate(distance,no_of_passengers):
    price_per_litre=70
    price_per_ticket=80
    mileage=10
    amount=price_per_ticket*no_of_passengers
    litre_required= distance/mileage
    litre_cost=litre_required*price_per_litre
    amount=amount-litre_cost
    if(amount<0):
        amount= -1
    return amount
    #Remove pass and write your logic here



#Provide different values for distance, no_of_passenger and test your program
distance=20
no_of_passengers=50
print(calculate(distance,no_of_passengers))
