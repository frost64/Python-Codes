## IMPORTS GO HERE if required
import math
## END OF IMPORTS 


#### YOUR CODE FOR netIncome GOES HERE ####
def netIncome(currentSalary,incomeTax=2.0):
	incomeTaxRatio=incomeTax/100.0
	netSalary= (currentSalary) - (currentSalary * incomeTaxRatio)
	return netSalary

#### End OF MARKER


