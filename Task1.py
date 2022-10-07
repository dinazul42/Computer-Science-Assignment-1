import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--task', type=str,help=("gets the value of the program you wish to apply ") )
parser.add_argument('--arg',type=str,help=("gets the value of the argument the user wish to work with in each program"))
args = parser.parse_args()

def vowels(string:str):
    """
    This function takes a string from the user by the parser and return the number of the appearances of
    the vowels letters.
    :param string:gets a str from the user.
    :return:the number of the appearances of the vowels letters on that string.
    """
    vowel_list = [ "y", "o", "i", "a", "u", "e", "Y", "O", "I", "E", "A", "U" ]
    b = [ element for element in string if element in vowel_list ]
    return len (b)


def perfect_power(value1):
    """ This function takes from the user the numeric value of the nth place on the perfect power list, that contains
    100 values, and returns the value of the wanted number.
    :param value1:value1 is the nth place in a list of 100 number that defined as perfect powers .
    :return: the number on the list.
    """
    result=[]
    result2=[]
    for i in range (1, 100):
        for j in range (2, 10) :
            result.append (i ** j)
            [ result2.append (item) for item in result if item not in result2 ]
            result2.sort()
    return result2[value1-1]


def lazy (n):
    """This function takes the number of the cuts from a whole and returns the maximum numeric value
    of the pieces as a result,or as called the " lazy number" .
    :param n: number of the cuts
    :return:the maximum number of the pieces as a result.
    """
    return (((n-1)**2+(n-1) +2) // 2)

if args.task == "vowels" :
       print (vowels(args.arg))
elif args.task=="perfect":
    print(perfect_power(int(args.arg)))
elif args.task=="lazy":
    print (lazy(int(args.arg)))
else:
    print("wrong input")

