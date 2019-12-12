
# coding: utf-8

# In[1]:


# Question:1

def isPositiveInteger(number):
    if int(number) > 0 :
        return True
    else:
        return False
def calcFactorial(number):
    factorial = 1
    if isPositiveInteger(number) == True:
        number = int(number)
        for i in range(1, number + 1):
            factorial = factorial * i
        print(factorial)
    else:
        print("Invalid input")

factCalc = input("Enter any Number to calculate it's factorial: ")
calcFactorial(factCalc)


# In[2]:


# Question:2 Count upper case and lower case by fuction

def CountUpperLower(stns):
    upper=0;
    lower=0;
    for i in st1:
        if i>="A" and i<="Z":
            upper +=1;
        elif i>="a" and i<="z":
            lower +=1;
    print("Upper case",upper);
    print("Lower case", lower);

st1 = input("Enter any String:");
CountUpperLower(st1);


# In[ ]:


# Question:3
List = [];
n = int(input("Enter number of Nums: "));
for i in range(0, n):
    num= int(input());
    List.append(num)
#print(List);
def EvenNum(List):
    for num in List:
        if num % 2==0:  
            print(num, end =", ");
EvenNum(List);


# In[3]:


# Question:4
num = int(input("Enter num to check it is prime or not: "));
def checkPrime(num):
    if num>1:
        for i in range(2,num//2):
            if(num % i)==0:
                print(num, " is not a prime");
                break;
            else:
                print(num, "is a prime number ");
    else:
        print(num, "is not a prime number");

checkPrime(num);


# In[1]:


#Question 5

def checkPaln(string):
 if(string==string[::-1]):
     print("The string is a palindrome")
 else:
     print("Not a palindrome")
string= input("Enter any word : ");
checkPaln(string)


# In[6]:


def display_item(egg,Sanitizer, **other_info):
    print("The egg is : " + egg)
    print("The Sanitizer is : " + Sanitizer)
    for key, value in other_info.items():
        print(key + ": " + value)

display_item(egg="3 dozen", Sanitizer="1 bottle",makeup ="lipstick", oil="4 litre",detergent='Ariel',)


# In[ ]:




