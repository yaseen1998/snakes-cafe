meal=[{'menu':
['Wings',
'Cookies',
'Spring Rolls'],
      'name':'Appetizers'},
     {'menu':
['Salmon',
'Steak',
'Meat Tornado',
'A Literal Garden'],
      'name':'Entrees'},
     {'menu':
['Ice Cream',
'Cake',
'Pie'],
      'name':'Desserts'},
      {'menu':
['Coffee',
'Tea',
'Unicorn Tears'],
       'name':'Drinks'},]

def printmenu():
    entrance = """
    **************************************
    **    Welcome to the Snakes Cafe!   **
    **    Please see our menu below.    **
    **
    ** To quit at any time, type "quit" **
    **************************************
    """
    exit = """
    ***********************************
    ** What would you like to order? **
    ***********************************
    """
    print(entrance)
    for j in range(len(meal)):
        print('----------')
        print(meal[j]['name'])
   
        for i in range(len(meal[j]['menu'])):
            print(meal[j]['menu'][i])
    
    print(exit)

def printorder(result,resultOfquant):
    print('your order is : ')
    for i in range(len(result)):
        print(f'{result[i]} : {resultOfquant[i]}')

def checkOrder(order,resulrOfOrder,resultOfquant,count):
    if order in resulrOfOrder:
        ind = resulrOfOrder.index(order)
        resultOfquant[ind]=input(f'this item is exist edit the  quantity {resultOfquant[ind]} : ')
        return [resultOfquant,ind]
    else:
        return(count.append(1))

def OrderLoop(order,resultOforder,resultOfquant,count,countlist):
     for j in range(len(meal)):
            
            if order in (meal[j]['menu']):   
                check = checkOrder(order,resultOforder,resultOfquant,count)
                if check:
                    resultOfquant=check[0]
                    quantOfOrder=check[0][check[1]]
                    count[check[1]]+=1
                    print(f'** {count[check[1]]} order of {order} : {quantOfOrder} have been added to your meal **')

                else:
                    quantOfOrder = input('how match do you want ')
                    resultOfquant.append(quantOfOrder)
                    resultOforder.append(order)
                    print(f'** {count[countlist]} order of {order} : {quantOfOrder} have been added to your meal **')
                    countlist+=1
                break
            if j==len(meal)-1:
                print('sorry but we do not have this in our menu yet')
                break

def customerorder():
    printmenu()
    order = input('> ')
    resultOforder = []
    resultOfquant = []
    count = []
    countlist=0
    while order != 'quit':
        OrderLoop(order,resultOforder,resultOfquant,count,countlist)
        order = input('> ')
        
    printorder(resultOforder,resultOfquant)


customerorder()
