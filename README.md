1. Check for more examples
2. Take a minute to think and let the interviewer know about it
3. Think out loud and point out your solution steps
4. IF I am not sure if its an optimal solution - Does this seem like a good direction, I think this solution should work, but do you think I should look for a better solution
5. Test test test your code

`Classes and Objects`
Encapsulation: The data and the functions associated with an object are contained together within an object, keeping them safe from outside interference
Inheritance - allows class to be arranged in an hirarchial order.

`Time complexity`
Amount of time it takes to run an algorithm in the worst case scenario compared to the length of input.
O(1) - constant time - any direct message or print any value 
O(n) - linear time - simple for loops 
O(log n) - exponential time - binary search
O(n*n) - nested for loops 

`Recursion`
An elegant method of solving a problem where the solution depends on the solutions to smaller occurences of the same problem

`Insertion sort`
traverse from first elemtn to the last until the whole thing is sorted
O(n*n) - not so good 

`Merge Sort`
sort after chunking them in pairs
O(n)
Average runtime - O(n log n)

`Quick Sort`
Divide and conquer
Choosing a pivot and moves the smaller items to the left and vice versa 
Average runtime - O(n log n)

`binary Search`
search the item with the item in the middle of the sorted list 
worst case scenario: O(log n)

`Breadth first search`
algorith for traversing tress and graphs
it explores the root node and the sibling nodes before movign on to the next level of siblings
```
to find the shortest path between 2 nodes in a tree or a unweighted path
```

`Depth first search`
starts at the root node and explores as far down  the path  as possible until hitting the end,  then backtracks to the node that was most recent root node  and explores back again

```
to exhaustively explore every possible path
looking for longest path between two node
```