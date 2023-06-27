# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 18:46:39 2023

@author: chenriquez4

Pmt = r * PV/(1-(1+r)0**-n)
Pmt is how much you pay back/mon is number of months 
r is interest rate per month
n is number of months

"""
    Pmt = r * PV/(1-(1+r)**-n)
    return Pmt

def computesPmt(PV, r, n):
    """

    Parameters
    ----------
    Pmt : TYPE float 
    DESCRIPTION. how much i can afford for monthly payment
    
    r : TYPE
        DESCRIPTION. interest rate APR
    n : TYPE integer
        DESCRIPTION. number of months 

    Returns
    -------
    PV : TYPE
        DESCRIPTION. amount of $ I can afford to borrow 
    
    formula:
        pv= (1-(1+r)**(-n) *Pmt/r)
    """
    r =r/100 #convert APR to a decimal
    r = r/12
    
    pv = (1-(1+r)**(-n) *Pmt/r)
    return PV
    
    
    
    
    
   

# input the PV 
import numpy as np

while(True):
    choice = int(input('enter choice 1 for PV, 2 for Pmt -> '))
    if (choice == 1 or choice ==2): 
        break
   
    else:
        print(f"enter a 1 or a 2, you entered {choice}\n")
        
if choice ==2: 
    n = 48
    PV = input('enter PV:')
    PV = float(PV) 
    # equivalently PV = float(input('enter PV: '))
    print(f"PV ={PV} \n")
    
    r = input("interest APR:")
    r = float(r)/100
    r = r/12
    print(f"interest = {r: 0.3f}\n")
    
    n= int(input('how many months:'))
    print(f"\nn= {n} months\n")

pmt = computesPmt(PV, r, n)
pmt = np.round(pmt, 2)
print(f"payment is {pmt: } per month\n")

if choice == 1:
    
    n= int(input('no of months'))
    
Pv = computesPV(85.61, 5, 12)
print(fPv)






