"""
Problem:
You are climbing a staircase. It takes n steps to reach the top.
Each time you can climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Solution:
It is a classic dynamic programming problem.
The key to solving it is recognizing that the number of ways to reach a given step is the sum of the ways to reach the two preceding steps.
This is because, at any step, you could have gotten there by either a single step from teh step before or a double step from two steps
before.
Lets denote the number of ways to reach step 'i' as 'ways[i]'. Then the recurrence relation is 
ways[i] = ways[i-1] + ways[i-2]
For base cases,
ways[0] = 1 (there is one way to be at the start before taking any steps)
ways[1] = 1 (there is one way to reach the first step, which is just a single step)

The solution for 'n' steps is then ways[n]
"""
def climbStairs_optimized(n):
  if n <= 1:
    return 1
  
  a, b = 1, 1

  for i in range(2, n+1):
    a, b = b, a + b

  return b

def climbStairs(n):
  if n <= 1:
    return 1
  
  ways = [0] * (n+1)
  ways[0], ways[1] = 1, 1

  for i in range(2, n + 1):
    ways[i] = ways[i - 1] + ways[i - 2]

  return ways[n]


def main():
  ways = climbStairs(5)
  print(f"ways {ways}")

  ways = climbStairs_optimized(5)
  print(f"ways optimized {ways}")

main()
