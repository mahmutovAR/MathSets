# MathSets

This script gets math sets and some number and checks
if given number belongs to some subrange from intersection of the initial sets.

## Initial math sets are given as dictionary {'name (if needed)': ['sub set']}:
* The sub set is given as `list`, for example:
  * `[['-inf', -10], [10, '+inf']]`
  * `[['-inf', -41], [-18, 24], [51, 62], [103, '+inf']]`
  * `[[-89, -61], [61, 72]]`

### Task 1
* script returns the initial number, if it belongs to some subrange from the math sets intersection
* script returns the nearest endpoint(s) to the initial number otherwise

### Task 2
* script returns the subrange from the math sets intersection, if initial number belongs to it
* script returns the nearest range(s) from the math sets intersection otherwise
  
## Script runs on Python 3.9