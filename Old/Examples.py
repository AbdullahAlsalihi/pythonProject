

#While Loops

#create a variable that control the loop
cal_other_commision = 'y'

#create the while loop for the commison
while cal_other_commision == 'y':
    sales = float(input('Enter the amount of sales: '))
    comm_rate = float(input('Enter commision rate: '))

    commission = sales * comm_rate

    print('The commission is ', commission)

    cal_other_commision = input("Do you want to calculate another commission (Enter Y for yes): ")


