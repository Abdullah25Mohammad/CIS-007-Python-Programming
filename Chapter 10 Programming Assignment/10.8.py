#10.8
#Find the index of the smallest element
#Abdullah Mohammad
#1/20/23

def indexOfSmallestElement(list):
    minOfList = min(list)
    return list.index(minOfList)

def main():
    list = input("Enter a list: ")
    list = list.split()

    list = [eval(i) for i in list]

    if len(list) > 1:
        print("The index of the smallest element is", indexOfSmallestElement(list))
    else:
        print("There is only 1 element in the list")

main()
