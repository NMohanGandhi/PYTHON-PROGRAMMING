arr = [6,7,4,7,3,6,7,9,3,2]
arr.sort() #[2, 3, 3, 4, 6, 6, 7, 7, 7, 9]
print(arr)
count = {}
for num in arr:
    if num in count:
       count[num] += 1
       
    else:
        count[num] = 1
print(count)

   
   
