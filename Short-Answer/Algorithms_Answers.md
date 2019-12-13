#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n).  Here 'a' grows at a constant rate of n^2, and the while-loop 
terminates when 'a' reaches n^3.  Since n^3/n^2 = n, it always takes n 
iterations for the while-loop to terminate.

b) O(n log(n)).  Here the outer for-loop takes n operations to terminate.  The 
inner while loop, by contrast, takes log(n) operations to terminate; this is 
because the loop terminates when j is equivalent to n, and j grows 
exponentially, doubling each iteration.  Thus, the nested loops take n*log(n) 
iterations to terminate.

c) O(n).  Here bunnyEars is called recursively until 'bunnies' reaches 0, with 
'bunnies' reducing by 1 each time.  Thus, it always takes n iterations for the 
recursive function to terminate.

## Exercise II

This can be approached as a binary search problem.  You are searching through 
n floors to find floor f such that when you drop an egg from the floor, it does 
not break.  Thus, you should start at the middle floor (the n//2th floor) and 
drop an egg.  If the egg breaks, you should rule out the higher floors, and 
search for f in the lower floors; if the egg does not break, you should rule 
out the lower floors, and search for f in the higher floors.  Either way, you 
should continue searching for f at the floor located in the middle of the 
remaining possibilities.  Eventually, you will rule out all possibilities 
except floor f.