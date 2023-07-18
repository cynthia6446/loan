
"""

# -*- coding: utf-8 -*-

Spyder Editor

Created on Wed Jun 14 18:46:39 2023

@author: chenriquez4
"""
"""
Pmt = r * PV/(1-(1+r)0**-n)
Pmt is how much you pay back/mon is number of months 
r is interest rate per month
n is number of months
"""
  


def computesPmt(PV, r, n):
    
    """
    Parameters
    ----------
    PV : TYPE
    DESCRIPTION
    r : TYPE
    DESCRIPTION. 
    n : TYPE 
    DESCRIPTION.
    
    Returns 
    -------
    Pmt : TYPE float
    DESCRIPTION. amt paid per month
    """
    
    r =r/100 #convert APR to a decimal
    r = r/12

    Pmt = r * PV/(1-(1+r)**-n)
    return Pmt
def computesPV(Pmt, r, n):
        
    """
    compute what your payment is if you borow
    PC at r% interest for n months
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
    r = r/12 #convertsto % per month

    PV= (1-(1+r)**(-n)) *Pmt / r
    return PV
def computesN(pmt, Pv, r):
    """
    

    Parameters
    ----------
    pmt : TYPE float
        DESCRIPTION. monthly payment
    Pv : TYPE float 
        DESCRIPTION.amount borrowed         
    r : TYPE float 
        DESCRIPTION interest rate, APR.

    Returns
    -------
    N: Type intefer 
    DESCRIPTION. number of months to pay back the loan

    """

    import numpy as np
    #convert r (APR) to a decimal, per month
    r = r/12 # converts to % per month
    r = r/100 #converts % to a decimal 
    
    #given Pmt, Pv, r, we compute n
    
    n = -np.log( 1-PV*r/pmt) / np.log(1+r)
    n = round(n,1)

    return n 
if __name__ == "__main__":

    import numpy as np     

while(True):
    choice = int(input('enter choice 1 for PV, 2 for Pmt or 3 for n-> '))
    if (choice == 1 or choice ==2 or choice ==3): 
        break
   
    else:
        print(f"enter a 1, a 2, or a 3, you entered {choice}\n")
        
        
if choice == 1:
    #compute PV; input pmt, r, n
    pmt = input('enter pmt: ')
    pmt = float(pmt)
    #equivalent PV = float(input('enter PV: '))
    print(f'pmt = {pmt: 0.2f} \n')
    
    r = input('interest APR:')
    r = float(r)
    
    print(f"interest = {r: 0.3f} \n")
    
    n= int(input('how many months: '))
    print(f'\nn = {n} months \n')
    
    PV = computesPV(pmt, r, n)
    #PV = np.round(pmt, 2)
    print(f"amount I can borrow is ${PV: 0.2f}")        
        
        
        

if choice ==2: 
    #compute pmt; input pv, r, n

    PV = input('enter PV:')
    PV = float(PV) 
    # equivalently PV = float(input('enter PV: '))
    print(f"PV ={PV} \n")
    
    r = input("interest APR:")
    r = float(r)
    
    print(f"interest = {r: 0.3f}\n")
    
    n= int(input('how many months:'))
    print(f"\nn= {n} months\n")

    pmt = computesPmt(PV, r, n)
    pmt = np.round(pmt, 2)
    print(f"payment is ${pmt: 0.2f} per month\n")



