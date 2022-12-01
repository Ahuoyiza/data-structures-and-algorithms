#problem: https://leetcode.com/problems/two-sum/
# Solution  1 Logic:
# Brute force, use two for loops to traverse the array and check if the current item 
# plus the next item equals target sum
#this will take O(N^2) time complexity

#Solution 2:
#use a hashtable
# 1. store the target sum
# 2. store current num (x)
# 3. At every given point x + y (unknown match) will equals target sum (t)
# therefore: y = t-x
# 4. check if current number fits into the equation(i.e if t-x = y, check if y exists in the array, if it does return its index, else store the current number in the hashtable)
# 5. storing in a hashtable ensures that we only traverse once as whatever has been iterated will be stored there (this definetly will have a space complexity of O(N))
# but in constant time
# time complexity of the overall program is  O(N) (cause we are looping through once) and space O(N) 

#p.s: this is still a work in progress, code will be added shortly 