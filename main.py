import customer
import employee

def main():
    #Customer 2 Creating Order 2
    customer.new_order('janedoe@gmail.com', 'jane doe', '1-111-111-1111', 1, 'Project 1', 'Simple Website')

    #Customer 1 views Order 1 
    customer.view_order(1)

    #Customer 1 views Orders
    customer.view_all_orders(1)

    #Customer 2 Submits Order 2 Cancelation 
    customer.request_order_cancelation(2,2)

    #Employee Cancels Order 2
    employee.cancel_order(2)

    #Customer 1 Submits chnages to order 1


    #Employee makes changes to order 1


    #Employee adds a Feature to Order 1


    #Employee changes Order 1  to Payment stage


    #Customer 1 Makes Payment 1 to Order 1


    #Customer 1 submits Payment 1 Cancelation 


    #Employee cancels Payment 1


    print()

main()