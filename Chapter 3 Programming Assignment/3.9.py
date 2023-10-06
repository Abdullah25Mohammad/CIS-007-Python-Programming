#3.9
#Financial application: payroll
#Abdullah Mohammad
#1/4/23

Name = input("Enter employee's name: ")
NumHoursWorked = eval(input("Enter number of hours worked in a week: "))
HourlyPayRate = eval(input("Enter hourly pay rate: "))
FedTaxRate = eval(input("Enter federal tax withholding rate: "))
StateTaxRate = eval(input("Enter state tax withholding rate: "))

print()


GrossPay = NumHoursWorked * HourlyPayRate

print("Employee Name: ", Name)
print("Hours Worked: ", format(NumHoursWorked, ".1f"))
print("Pay Rate: $", format(HourlyPayRate, ".2f"))
print("Gross Pay: $", format(GrossPay, ".2f"))

FedTaxDeductions = FedTaxRate * GrossPay
StateTaxDeductions = StateTaxRate * GrossPay
TotalDeductions = FedTaxDeductions + StateTaxDeductions

NewPay = GrossPay - TotalDeductions

print("Deductions:")
print("  Federal Withholding (", format(FedTaxRate, ".1%"), "): ", FedTaxDeductions)
print("  State Withholding (", format(StateTaxRate, ".1%"), "): ", StateTaxDeductions)
print("  Total Deduction: ", TotalDeductions)

print("New Pay: ", NewPay)
