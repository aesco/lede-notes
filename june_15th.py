
# Q2
# owner Jessica Goodman
# name Company LLC
# address 34 45th St
#  the key without quotes is a variable, in this case address, name, owner.


# Q3
results = [company['name'] for company in companies ]			# each of these companies is a dictionary (data type)
print results

# Q4
if rating < target: 
	print "Failed"
elif rating > target * 2:		# elif: only run the next lines only if the first one didn't work (didn't accomplished the condition)
	print "Excellent work"
else:							# you can have only one else
	print "Success"
if target == 0:
	print "Easy"				# it will print "Easy" every time the target is 0, indepently of what happened with the rating


# Q5a
# one way
murder_total = 0
for key in murders.keys():							# Always use .keys() otherwise you'll forget you're working on a dictionary
	murder_total = murder_total + murders[key]
	print murder_total

# other way
sum(murders.values())

# Q5b
sum(murders.values()) - murders['Kings County']

# Q5c
# two ways to sort: .sort() vs. sorted()
# .sort() sort the original list forever
# sorted() give you a brand new list
counties.sort()
counties





