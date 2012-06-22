groceries=['bananas','strawberries','apples','bread']
groceries.append('champagne')
print groceries
print'-------------------------------------------------------------------'
groceries.remove('bread')
print groceries
print'---------------------------------------------------------------------'
grocery_aisle={'bananas':'b','strawberrise':'s','apples':'a','bread':'b','champagne':'c'}
for key,value in grocery_aisle.iteritems():
    print '\t',key,'\t',value,'\n'
print'-------------------------------------------------------------------'
grocery_price={'Apples':'7.3','Bananas':'5.5','bread':'1.0','Carrots':'10.0','Champagne':'20.90','Strawberries':'32.6'}
for key,value in grocery_price.iteritems():
    print '\t',key,'\t',value,'\n'
print'----------------------------------------------------------------------'
grocery_price['Strawberries']='63.43'
for key,value in grocery_price.iteritems():
    print '\t',key,'\t',value,'\n'
print'----------------------------------------------------------------------'
grocery_price['Chicken']='6.5'
for key,value in grocery_price.iteritems():
    print '\t',key,'\t',value,'\n'
print '---------------------------------------------------------------------'
""" I would use the list data structure. This becomes it's easier making
modifications to the items within the lists."""
print
in_stock=['bananas','strawberrise','apples','bread','champagne']
for i in in_stock:
    print i
    print'---------------------------------------------------------------------'
always_in_stock=('bananas','strawberrise','apples','bread','champagne')
print always_in_stock
print'---------------------------------------------------------------------'
print"Come to Shoprite! We always sell:"
for i in always_in_stock:
    print i
