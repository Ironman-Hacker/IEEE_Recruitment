list1 = list(map(int, input("Enter elements of first list separated by spaces: ").split()))
list2 = list(map(int, input("Enter elements of second list separated by spaces: ").split()))
intersection = list(set(list1) & set(list2)) #it includes numbers which are present in both the lists.
print(intersection)
