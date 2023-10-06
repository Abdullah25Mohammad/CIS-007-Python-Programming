#10.13
#Eliminate duplicates
#Abdullah Mohammad
#1/20/23

def eliminateDuplicates(lst):
    resultList = []
    for i in lst:
        if i not in resultList:
            resultList.append(i)
    return resultList

def main():
    lst = input("Enter a list: ")
    lst = lst.split()

    print("The resulting list with no duplicates is: ", str(eliminateDuplicates(lst)))
main()