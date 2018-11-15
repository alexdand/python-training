'''
Created on Nov 12, 2018

@author: Administrator
'''

months = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')

for month in months:
    print(month)

i = 0
while i < len(months):
    print(months[i])
    i+=1

print(f'January appears {months.count("January")} times in months')

print(f'August is the number {months.index("August")} index in months')

# Similar to lists we can iterate using indexes
print(months[0:3])
print(months[::-1])
