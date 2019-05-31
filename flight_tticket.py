

def calculate_total_ticket_cost(no_of_adults, no_of_children):
    total_ticket_cost=0
    adults_cost=no_of_adults*37550.0
    children_cost=no_of_children*(12516.666)
    ticket_cost=adults_cost+children_cost
    service_tax=ticket_cost*(0.07)
    total_ticket_cost=ticket_cost+service_tax
    total_discount=total_ticket_cost*(0.1)
    total_ticket_cost=total_ticket_cost-total_discount
    return total_ticket_cost
#Provide different values for no_of_adults, no_of_children and test your program
total_ticket_cost=calculate_total_ticket_cost(5,2)
print("Total Ticket Cost:",total_ticket_cost)
