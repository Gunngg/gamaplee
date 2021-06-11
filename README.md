# Gamaplee
GAMAPLEE (the greatest and most awesomeset programming language to ever exist) is an esolang inspired by brainfuck and implemented in python

Data is stored on an infinite square grid. Each cell holds a number - numbers can be positive or negative, whole, rational or irrational. You can move the pointer in different directions to access different cells and modify the values of those cells.
## Commands
~~(i shouldnt have added that many)~~

Anything after a # symbol until the end of the line will be ignored
#### Move the pointer..
**\>** - to the right

**<** - to the left

**^** - up

**v** - down

#### Transfer current cell's value..
**)** - to the right

**(** - to the left

**A** - up

**V** - down

#### Duplicate current cell's value..
)' - to the right

(' - to the left

A' - up

V' - down

#### Transfer current cell's value 2 cells..
**).** - to the right

**(.** - to the left

**A.** - up

**V.** - down

#### Duplicate current cell's value 2 cells..
**),** - to the right

**(,** - to the left

**A,** - up

**V,** - down

#### Basic 
**\+** - adds one to the current cell

**-** - subtracts one from the current cell

**f** - flips the current value. If its 0 the value of the cell below becomes 1, if its not 0 value below becomes 0

**~** - ends the program

**m** - moves the pointer in a random direction horizontally/vertically

**M** - moves the pointer in a random direction diagonally

**m'**/**M'** - moves the pointer in a random direction horizontally/vertically/diagonally

**:** - copies current cell's value for later

**;** - replaces current cell's value with the copied one

**+.** - adds 1 to the copied value

**-.** - subtracts 1 from the copied value

**x** - set copied value to 0

**F** - works the same way as **f** but everything is done with just the copied value

**\_** - sets current cell's value to 0

**?** - sets current cell's value to a random ascii character value (between 33 and 126 inclusive)

#### Loops and stuff

**[ ]** - if current cell's value isnt 0, does whats inside the brackets, otherwise skips them

**[' ]** - if current cell's value IS 0, does whats inside the brackets, otherwise skips them

**[. ]** - if copied value isnt 0, does whats inside the brackets, otherwise skips them

**[, ]** - if copied value IS 0, does whats inside the brackets, otherwise skips them

**{ }** - repeats whats inside the brackets n times where n is the current cell's value

**{' }** - same as above but sets current value to 0 before repeating

**{. }** - repeats whats inside the brackets n times where n is the currently copied value

**{, }** - same as above but sets copied value to 0 before repeating

(1 and 2 are basically brackets)

**1z 2** - loops stuff inside the brackets until it "finds" a cell whose value is zero

**1Z 2** - loops stuff inside the brackets until CURRENT cell's value is 0

#### Input/output

**n** - gets users input as a number and stores it in the current cell

**N** - same as above but stores the ascii value of the number

**i** - same as n but can also get strings as input - (numbers saved as themselves, symbols as ascii)

**I** - stores all characters as ascii

**o** - outputs the current cell's value with a new line (opposite of n)

**O** - o without newline

**o'**/**O'** - o without newline but with space

**q** - outputs the ascii character with the cell's value with a new line (opposite of I)

**Q** - q without newline

**q'**/**Q'** - q without newline but with space

**c** - outputs numbers 0-9 as themselves, everything else as ascii with a new line (opposite of i)

**C** - c without newline

**c'**/**C'** - c without newline but with space

#### Operators

**=** - [eq] if current value is equal to value above then value below is set to 1, otherwise its 0

**='** - [not eq] if current value is NOT equal to value above then value below is set to 1, otherwise its 0

**>'** - [greater] if current value is greater than value above then value below is 1, otherwise is 0

**>.** - [greater or eq] if current value is greater or equals the value above then value below is 1, otherwise 0

**<'** - [less] if current value is less than value above then value below is 1 otherwise 0

**<.** - [less or eq] if current value is less or equals value above then value below is 1 otherwise 0

**&** - [and] if current value and value above arent 0, value below becomes 1, otherwise 0

**&'** - [nor] if current value and value above ARE both 0, value below gets set to 1, otherwise it gets set to 0

**|** - [or] if current value OR value above arent zero, value below is 1, otherwise 0

**|'** - [xor] same as above but there should but its only 1-0 or 0-1 (it cant be 1-1)

#### Math - does the thing to the value above (if required) and saves below

**+'** - addition

**-'** - subtraction

**\*** - multiplication

**/** - division

**^'** - exponent

**s** - squares current cell's value and saves below

**t** - raises current cell's value to the power of itself

**r** - nth root (n is the value above)

**R** - square root

**%** - modulo

**!** - factorial

## Examples
More examples can be found in the example programs folder

### Hello world
This should output "Hello, World!"
```
+++svA'-*vQ ^^    # prints H and moves to 9
+sv+Q             # prints e
+++++++QQ         # prints ll
+++Q >            # prints o and moves
++++sv-----*vQ' ^ # prints comma + space and moves
_++v*v-Q          # prints W
^^^< Q            # moves to o and prints
+++ Q             # prints r
++++-'vQ          # prints l
A^-'v++Q          # prints d
-^_+++v/vQ        # prints the exclamation mark
```
inline `+++svA'-*vQ^^+sv+Q+++++++QQ+++Q>++++sv-----*vQ'^_++v*v-Q^^^<Q+++Q++++-'vQA^-'v++Q-^_+++v/vQ`
### Cat
`1zIq2`
Simply asks user for input and immediately outputs it
