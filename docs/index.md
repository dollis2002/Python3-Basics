# Python3 Basics
by DHNAM

## Variables and data types
Python doesn't require the user to declare or reference variables, that's one benefit of a high-level language.
Assigning a value will automatically reference the variable to its type.
```
a = 1 # int (integer)
b = 3.14 # float
c = 'H' # str (string)
d = 'Hello world' # str (string)
```
If you'd like to get the type of an already defined value, use the `type(variable)` function.
[See example code](code/variables.py)

### Naming variables
Don't forget that a variable name should also start with a letter, not a number or symbol and it is case-sensitive. Some characters, strings, and symbols are reserved by Python, this means Python has uses for them so you can't name a variable with this reserved names. Some reserved names are `str, char, list, tuple, dict, int, float` or any object, function, and method name.

## Basic data structures
Data structures store many variables into one, generally they are called arrays in other languages.
Python manages three data structures as standard: lists, tuples, and dictionaries. These can also be stored inside a variable
```
lis = [1, 2, a, 'a'] 
tup = (11, a, b, c, 'hello')
dic = {'one' : 1, 'two' : 2, 'pi' : c}
```
-Lists are containers with multiple variables, separated by a comma and surrounded by \[brakets\].
-Tuples are lists, but variables are inmutable, surrounded by parentheses.
-Dictionaries work with key:value pairs, order doesn't matter.

### Accessing variables in data structures
For `list` and `tuple` use indexes to call up a variable at a certain position. The first position is given with index 0 and so on.
Use the syntax `struct[index]` to call a variable from a `list` or `tuple`, where `struct` is of type `list` or `tuple`.
A `dict` uses the keys to access the value associated, so order doesn't matter. Use `dicname['key']` to access the value associated to that key. 
[See example code](code/datastructures.py)

## Arithmetic operators
The operators work similar if not the same as other languages.
| Operator | Description |
|--------- | ----------- |
| + | Add |
| - | Substract |
| * | Substract |
| / | Divide |
| // | Cocient division |
| % | Residual division |

## If else conditionals
Conditionals check if the given statement is true or false, and execute the code below depending on them. They rely on boolean operators to check conditions and logical operators to check multiple conditions.

`if` checks the condition, but if the condition is not met, the code below `else` executes (optional).

### Boolean operators
| Operator | Description |
|--------- | ----------- |
| > | Greater than |
| < | Lesser than |
| >= | Greater or equal than |
| <= | Lesser or equal than |
| == | Equal to |
| != | Not equal to |

```
a = 1
b = 2
c = 2

if a > b: 
    c = 5
else:
    c = a+b
```
# Logical operators
| Operator | Description |
|--------- | ----------- |
| and | Greater than |
| < | Lesser than |
| >= | Greater or equal than |
| <= | Lesser or equal than |
| == | Equal to |
| != | Not equal to |
| // | Cocient division |
| % | Residual division |






