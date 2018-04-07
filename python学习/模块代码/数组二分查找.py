def binary_search(search_list, target):
 left = 0
 right = len(search_list) - 1
 while left <= right:
     mid = (left + right) / 2
     if search_list[mid] < target:
         left = mid + 1
         continue
     if search_list[mid] == target:
         return mid
     if search_list[mid] > target:
         right = mid - 1
 return None
search_list = [1, 3, 4, 6, 8, 9]
print binary_search(search_list, 5)
print binary_search(search_list, 1)
print binary_search(search_list, 3)
print binary_search(search_list, 4)
print binary_search(search_list, 6)
print binary_search(search_list, 8)
print binary_search(search_list, 9)