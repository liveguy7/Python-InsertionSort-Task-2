
def insertion_sort(lst):
  for i in range(1, len(lst)):
    j = i
    while j > 0 and lst[j] < lst[j-1]:
      #lst[j], lst[j-1] = lst[j-1], lst[j]
      tmp = lst[j]
      lst[j] = lst[j-1]
      lst[j-1] = tmp
      j -= 1
  return lst

lst = [4,5,9,1,56,90,24,11,89,56,2]
print(insertion_sort(lst))

