number=int(input())
bil=""

#collect numbers by three and put into list
def find_three_numbers(threes):
    a=threes%10
    b=(threes%100-a)//10
    c=(threes%1000-b-a)//100
    return(c,b,a)

#find numbers by three (hundrets, hundrets of thousends, billions )   

first_three=number%1000
second_three=(number-first_three)//1000
three=number//1000000

one=find_three_numbers(first_three)#list of numbers
two=find_three_numbers(second_three)

#returns ones
def check1(number):
    if number==1:
        bil="one"
    elif number==2:
        bil="two"
    elif number==3:
        bil="three"
    elif number==4:
        bil="four"
    elif number==5:
        bil="five"
    elif number==6:
        bil="six"
    elif number==7:
        bil="seven"
    elif number==8:
        bil="eight"
    elif number==9:
        bil="nine"
    else:
        bil=""

    return(bil)
#returns tens
def check2(number):
    if number==1:
        bil="one"
    elif number==2:
        bil="twenty"
    elif number==3:
        bil="thirty"
    elif number==4:
        bil="fourty"
    elif number==5:
        bil="fifty"
    elif number==6:
        bil="sixty"
    elif number==7:
        bil="seventy"
    elif number==8:
        bil="eighty"
    elif number==9:
        bil="ninety"
    else:
        bil=""

    return(bil)
#returns teens
def check3(number):
    if number==1:
        bil="eleven"
    elif number==2:
        bil="twelve"
    elif number==3:
        bil="thirteen"
    elif number==4:
        bil="fourteen"
    elif number==5:
        bil="fifteen"
    elif number==6:
        bil="sixteen"
    elif number==7:
        bil="seventeen"
    elif number==8:
        bil="eightteen"
    elif number==9:
        bil="nineteen"
    else:
        bil=""

    return(bil)

#check billions
bil_res=check1(three)
if three==1:
    print(bil_res+" billion", end=" ")
else:
    print(bil_res+" billions", end=" ")
#check hundreds thousends   
hund_thous=check1(two[0])
if two[0]==1:
    print(hund_thous+" hundred", end=" ")
else:
    print(hund_thous+" hundreds", end=" ")
#check tens thousends
if two[1]==1:
    tens_thous=""
else:
    tens_thous=check2(two[1])
print(tens_thous, end=" ")
#check thousends
if two[1]==1:
    ones_thous=check3(two[2])
else:
    ones_thous=check1(two[2])
print(ones_thous + " thousands", end=" ")

#check hundrets
hund=check1(one[0])
if one[0]==1:
    print(hund+" hundred", end=" ")
else:
    print(hund+" hundreds", end=" ")
#check tens
if one[1]==1:
    tens=""
else:
    tens=check2(one[1])
print(tens, end=" ")
#check ones
if one[1]==1:
    ones=check3(one[2])
else:
    ones=check1(one[2])
print(ones, end=" ")
































