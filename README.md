# MathSets

This script gets math sets and some number and checks
if given number belongs to some subrange from the given sets intersection.

## Initial math sets are given as dictionary {key: value}:
* Key is name of sub set
* Value is sub set, is given as list, for example:
  * `[['-inf', -10], [10, '+inf']]`
  * `[['-inf', -41], [-18, 24], [51, 62], [103, '+inf']]`
  * `[[-89, -61], [61, 72]]`

### Task 1
* return the initial number, if it belongs to some subrange from the math sets intersection
* return the nearest endpoint(s) to the initial number otherwise

### Task 2
* return the subrange from the math sets intersection, if initial number belongs to this subrange
* return the nearest range(s) from the math sets intersection otherwise
  
## Script runs on Python 3.9