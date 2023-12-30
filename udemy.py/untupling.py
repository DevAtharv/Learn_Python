# Functions and Unpacking tuple with python
stock_prices = [("Apple",200),("Google,400"),("Microsoft",100)]
for item in stock_prices:
    print(item)

for ticker,price in stock_prices:
    print(price+(0.1*price))

work_hours = [("abby ,100"),("bill,400"),("cassie,800")]
def employee_check(work_hours):
    
    current_max = 0
    employee_of_month = ''
    for employee, hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_month = employee
        else:
            pass
        
result = employee_check(work_hours)
price(result)