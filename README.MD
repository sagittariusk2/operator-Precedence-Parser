
# Operator Precedence Parser

An operator-precedence parser is **a simple shift-reduce parser that is capable of parsing a subset of LR(1) grammars**.
More precisely, the operator-precedence parser can parse all LR(1) grammars where two consecutive nonterminals and epsilon never appear in the right-hand side of any rule.
### Grammar has two conditions :
1. The should not have two consecutive nonterminals.
2. Epsilon (ε) should never appear on the right side of any rule.

# Objective
The objective of this project is to apply operator precedence parser in python language.
- It is more user friendly as it takes input of orders among terminals through `.csv` file.
- Values in `stack` and `pointer of input string` is shown at every step of shift and reduction process.

# Working
1. It takes an input string. *i.e.*
```
i+i*i
```
string is given input by ```user```.

2. It takes the grammar on which the string should be checked.
```
E->E+E
E->E-E
E->E*E
E->E/E
E->i
```
grammar is given input as a ```grammar1.txt``` file.

3. A precedence order among the terminals is also given as input.

|        | +  | -  | *  | /  | i  | $  |
| :----- | :- | :- | :- | :- | :- | :- |
| **+**  | >  | >  | <  | <  | <  | >  |
| **-**  | >  | >  | <  | <  | <  | >  |
| **\*** | >  | >  | >  | >  | <  | >  |
| **/**  | >  | >  | >  | >  | <  | >  |
| **i**  | >  | >  | >  | >  | E  | >  |
| **$**  | <  | <  | <  | <  | <  | A  |

This is given input through `orders.csv` file.

3. Now parser checkes for the **validity of the grammar and validity of string on the given grammar** and prints the desired **parse tree**.


# Tech Stack

**Language :** Python


# Screenshots
### Final output
![App Screenshot](https://github.com/sagittariusk2/operator-Precedence-Parser/blob/main/screenParse.png?raw=true)
### Values of stack and input string at every step
![Parse Tree](https://github.com/sagittariusk2/operator-Precedence-Parser/blob/main/generated_parse_tree.png?raw=true)


# Authors

- [@Ritesh Ranjan (2019UCP1356)](https://github.com/sagittariusk2) MNIT, Jaipur
- [@Rohit Lohar (2019UCP1373)](https://www.linkedin.com/in/rohit-lohar-297627200/) MNIT, Jaipur

