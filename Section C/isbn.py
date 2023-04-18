def isbnInput():
    isbn_number_to_check = input("Enter the ISBN number to verify: ")
    n = len(isbn_number_to_check) 
    if(isbn_number_to_check.isdigit()):
        if(isbn_number_to_check[0:8]):
            if(isbn_number_to_check.upper()=='x' and not isbn_number_to_check[9].isdigit):
                return isbn_number_to_check
        
    if n < 10 and  n != 13:
        return isbnInput()
    if  n < 13 and  n != 10:
        return isbnInput()
    else:
        return isbn_number_to_check    

def isValid(isbn_number_to_check):

    output = "Invalid"
 
    if len(str(isbn_number_to_check)) == 10:
        output = isValidISBN10(isbn_number_to_check)
        if output == "Valid" :
            output = convertISBN10(isbn_number_to_check)
    else:
        output = isValidISBN13(isbn_number_to_check)

    print(output)
    

def isValidISBN10(isbn_number_to_check):

    digits = [10,9,8,7,6,5,4,3,2,1]
    sumOfProduct = 0
    if isbn_number_to_check[9].upper() == 'x':
        sumOfProduct += 10 

    for i in range(10):
    
        sumOfProduct +=int(isbn_number_to_check[i]) * digits[i]

    if sumOfProduct % 11 == 0:
        return "Valid"
    return "Invalid"


def isValidISBN13(isbn_number_to_check):

    digits = [1,3,1,3,1,3,1,3,1,3,1,3,1]
    length = 13
    sumOfProduct = 0

    for i in range(length):
        sumOfProduct +=int(isbn_number_to_check[i]) * digits[i]

    if sumOfProduct % 10 == 0:
        return "Valid"
    return "Invalid" 

def convertISBN10(isbn_number_to_check):

    isbn_number = '978' + isbn_number_to_check[:-1]
    digit = 0
    for i in range(len(isbn_number)):
        if i % 2 == 0:
            digit += int(isbn_number[i])
        else:
            digit += int(isbn_number[i]) * 3
    digit = digit % 10
    isbn13 = str(isbn_number) + str(digit)
    
    return isbn13

if __name__ == "__main__":
    
    isbn_number = isbnInput()
    isValid(isbn_number)