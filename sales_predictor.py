import numpy as np

def get_customer_info():
    if response == 'yes':
        intercept = -2.09049696
        X1 = int(raw_input('What\'s the manufacturer of their current car? '))
        X2 = int(raw_input('What are the current vehicle deal terms? '))
        X3 = int(raw_input('How many payments are remaining on the current vehicle deal terms? '))
        logodds = intercept +  X1*(-0.220447271306) + X2*(-0.0150766560171) + X3*(-0.0698020516319)
        odds = np.exp(logodds)
        prob = odds/(1 + odds)
        prob
        if prob < .25:
            print prob
            print ('Give customer to seasoned sales associate.')
        else:
            if prob > .25 & prob < .75:
                print calc
                print('Give cstomer to mid level sales associate.')
            else:
                if prob > .75:
                    print calc
                    print('Let a newbie test their skills :)!')
    else:
        if response == 'no':
            print('Please return when you\'d like to predict a customer sale.')
            print('Enjoy your day!')

print ('Welcome to the Sales predictor!')
a = raw_input('Are you looking to predict a customer outcome? ')
response = a.lower()
while response == 'yes':
    get_customer_info()
    response = raw_input('Would you like to predict another customer outcome? ')
print ('Thank you for using Sales Predictor 1.0 beta!')

