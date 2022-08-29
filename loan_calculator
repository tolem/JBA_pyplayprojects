
# write your code here
import argparse
from math import ceil, log


parser = argparse.ArgumentParser(description="This program prints differentiated payments")
parser.add_argument("-tp", "--type", choices=["annuity","diff"],
                    help="You specify either annuity or diff")

parser.add_argument("-prpl", "--principal", 
                    help="You specify the loan principal")

parser.add_argument("-pay", "--payment", 
                    help="You specify the payment")
                
parser.add_argument("-pd", "--periods", 
                    help="You specify the payment")
                

parser.add_argument("-intr", "--interest", 
                    help="You specify the payment")


                    




args = parser.parse_args()
args_list = [args.principal, args.payment, args.interest, args.periods]
none_count = sum([True for s in args_list if s is None])
num_count = [float(g) for g in args_list if g is not None]
neg_count = sum([True for num in num_count if num < 0])


if args.type not in ["annuity","diff"] or (none_count > 1) or (neg_count > 0):
    print("Incorrect parameters")
    


def diff_cal(pay, pd, irt, diff_mode=False):
    """ calculates differentiated payments! """
    interest = ((irt/100)/12)
    balance = 0
    
    for m in range(1,pd+1):
        diff_pay = ceil((pay/pd) +  interest * (pay - ((pay * (m - 1))/pd) ))
        balance += diff_pay

        if diff_mode:
            print("Month {month}: payment is {due}".format(month=m, due=diff_pay))
            
    return balance



if args.type == "annuity":
    if (args.payment and args.principal and args.interest):
        z = int(args.principal) # prinicpal
        x = int(args.payment) # payment
        y = float(args.interest) # interest
        i = (y /100) / 12
        m = x / (x - (i * z) ) 
        n = ceil(log(m, 1 + i)) # payment period 
        years = n // 12
        months = n % 12
        plural = "s" if years > 1 else ""
        
        print(f"It will take {years} year{plural} to repay the loan") if (years == 1 or months == 0) else print(f"It will take {years} years and {months} months to repay this loan!")
        due_amount = n * x
        overpayment = due_amount - z 
        print(f"Overpayment = {overpayment}")




    elif  (args.principal and args.periods and args.interest): 
        zz = int(args.principal) # principal
        xx = int(args.periods ) # period 
        yy = float(args.interest) # interest rate
        i = (yy/100) / 12  # interest
        payment = zz * ( (i * (1 + i)**xx ) / ((1 + i)**xx - 1 ))
        monthly_payment = ceil(payment)
        
        print(f"Your annuity payment = {monthly_payment}!")
        due_amount = monthly_payment * xx
        overpayment = due_amount - zz
        print(f"Overpayment = {overpayment}")
        
        


    elif (args.payment and args.periods and args.interest):
        z = float(args.payment)
        x = int(args.periods)
        y = float(args.interest)
        i = (y /100) / 12
        
        loan_prinicipal = ceil(z / ( (i * (1 + i)**x) / ((1 + i)**x  - 1)))
        print(f"Your loan principal = {loan_prinicipal}!")
        
        due_amount = z * x
        overpayment = due_amount - loan_prinicipal
        print(f"Overpayment = {overpayment}")
        
    else:
        print("Incorrect parameters")

elif args.type == "diff":
 
    
    if args.payment is None:
        loan_prinicipal, loan_period, loan_interest = float(args.principal), int(args.periods), float(args.interest)
        due_amount = diff_cal(loan_prinicipal,loan_period,loan_interest, True)
        overpayment = loan_prinicipal - due_amount
        print(f"Overpayment = {overpayment}")
        
    print("Incorrect parameters")
           
    
else:
    print("Incorrect parameters")
