#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) The runtime is O(n). This is because the number of operations will increase
linearly along with an increase in the input n. The algorithm will still only
run through the data one time in full no matter how large the input n is.

b) The runtime is O(n log n). This is because the for loop that deals with the
variable i is O(n) time, and the while loop inside the for loop is log n time.
The log n comes from the fact that j is doubling itself with every pass, while n
is only increasing by one. This leads me to believe that as n increases
linearly, the j < n stop condition will only increase by a factor of logn.

c) The runtime is O(n). This is because the recursion will run linearly as the
input n increases. The algorithm is performing an operation on the n input one
time or each increase in the input n, leading to a linear time complexity.

## Exercise II

This problem is a great example of a time when we should apply a binary search
algorithm. In this example, our building floors are the sorted array. The start
and end value are the bottom and top floors, respectively. Floor f is our target
floor, at which the egg will break.

Applying the binary search method to this problem, we should start at the middle
floor of the building, drop an egg off said floor, and record whether or not the
egg broke.

If the egg broke, we know we have to go to a lower floor. The next best action
for this is heading straight to the floor right in the middle of the floor that
we just threw the egg off and the gound floor. Repeating this process until we
eventually locate floor f (or in this case f-1) where the egg no longer breaks.

If the egg did not break, we know we have to go to a higher floor. The next best
action for this is heading to the floor right in the middle of the current floor
and the top floor. Repeating this process until we eventually locate floor f
where the egg breaks.

The runtime complexity of this will be O(logn) because we are effectively
eliminating half of the possible floors to try with every egg drop.

IF we had any more information to work with, such as splatter radius, we might
be able to add in another strategy for where we can narrow down how many floors
we need to move after each egg drop. But based on the information given, a worst
case of O(logn) is the best we can achieve.

```python
def building_binary(floors, f):
    lowest_floor = 0 #ground floor
    highest_floor =len(floors) - 1 #top floor (not counting roof i suppose)
    while lowest_floor <=highest_floor:
        middle_floor = highest_floor - (highest_floor - lowest_floor) //2
        if floors[middle_floor] == f:
            return middle_floor
        elif floors[middle_floor] < f:
            lowest_floor = middle_floor + 1
        else:
            highest_floor = middle_floor - 1

    return “THE EGG NEVER BROKE??” # or -1
```
