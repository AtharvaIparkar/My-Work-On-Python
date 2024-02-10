#Program to calculate net salary
basicsalary=int(input("Enter the basic salary: ")) #take input from user
hra=basicsalary*0.1 #calculate hra by multipying basicsalary with 0.1
print("hra is: ",hra) #print hra
ta=basicsalary*0.05 #calculate ta by multipying basicsalary with 0.05
print("ta is: ",ta) #print ta
grossSalary=basicsalary+hra+ta #calculate gross salary by adding basicsalary,hra and ta
print("grossSalary is: ",grossSalary) #print gross salary
pt=grossSalary*0.02 #calculate pt by multipying grossSalary with 0.02
print("pt is:",pt) #print pt
NetSalary=grossSalary-pt #calculate net salary by substracting pt from grossSalary 
print("Your net salary is: ",NetSalary) #print net salary
