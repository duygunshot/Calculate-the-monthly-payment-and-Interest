#Group7
#Dean Tran, Edwin Rodriguez, Elisa Shukuru
#02/22/2023
"""the purpose of the programming assignment is to calculate the monthly payment and Interest for Incentive A and for 
Incentive B. Additionally, to compute the amount of money saved over five years"""
def monthlyPayment(pv, r, m, t):#Create a function to calculate monthly payment
    i = r / m
    n = m * t
    pmt = pv * (i / (1 - ((1 + i) ** (- n))))
    return pmt

def interest(pmt, m, t, pv):#Create a function to calculate interest paid
    n = m * t
    interest = (pmt * n) - pv
    return interest

price = 45575.25
COMPOUND = 12
time = 5
discountA = 6000
pvA = price - discountA
ANNUAL_INTEREST_RATE_A = 2.675 / 100
pvB = price

pmtA = monthlyPayment(pvA, ANNUAL_INTEREST_RATE_A,COMPOUND, time)#calculate monthly payment for Incentive A
interestA = interest(pmtA, COMPOUND, time, pvA)#calculate interest paid for Incentive A
moneySavedA = price - (pmtA * (time * COMPOUND))#calculate money saved for Incentive A

pmtB = pvB / (time * COMPOUND)#calculate monthly payment for Incentive B
interestB = interest(pmtB, COMPOUND, time,pvB)#calculate interest paid for Incentive B
moneySavedB = price - (pmtB * (time * COMPOUND))#calculate money saved for Incentive B

print(f"Monthly payment for Incentive A is: ${pmtA}")
print(f"Interest paid for Incentive A is: ${interestA}")
print(f"Money saved over five years for Incentive A is: ${moneySavedA}")

print(f"Monthly payment for Incentive B is: ${pmtB}")
print(f"Interest paid for Incentive B is: ${interestB}")
print(f"Money saved over five years for Incentive B is: ${moneySavedB}")

