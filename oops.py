import sys
import csv
from copy import deepcopy
def main():
    capital = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    small = list("abcdefghijklmnopqrstuvwxyz")

    oper = list("+-*/&|")
    input_string = "i+i*i"

    # Checking  in the given input string  if the last  character of the string is any airthmatic operator then  string is not valid.
    if input_string[len(input_string)-1] in oper or input_string[0] in oper:
        print("GIVEN STRING IS NOT VALID STRING.....REJECTED  FURTHER")
        return

    # Checking if two airthmatic operators found adjacent in given input string then string is not valid.
    for i in range(len(input_string)-1):
        if input_string[i] in oper and input_string[i+1] in oper or input_string[i] in small and input_string[i+1] in small:
            print("GIVEN STRING IS NOT VALID STRING.....REJECTED  FURTHER")
            return
    
    input_ind = list(input_string)
    input_ind.append('$')
    master = {}
    master_list = []
    non_terminals = []
    grammar = open('grammar1.txt', 'r')
    master = {}
    terminal_in_given_grammar = []
    for row in grammar:
        i = len(row)
        for j in range(i):
            if row[j] == "\n" or row[j] == " ":
                i = j
                break
        master_list.append(row[0:i])
        x = row.split('->')
        non_terminals.append(x[0])
        second = x[1]
        ind = len(second)
        for i in range(len(second)):
            if second[i] == "\n" or second[i] == " ":
                ind = i
                break
        sec_part = second[0:ind]
        master[sec_part] = x[0]
        for i in range(len(sec_part)-1):
            #  checking if two non terminals are found adjacent then it is invalid grammar
            if sec_part[i] in capital and sec_part[i+1] in capital or sec_part[i] in small and sec_part[i+1] in small:
                print("GIVEN GRAMMAR IS NOT OPERATOR GRAMMAR.....REJECTED  FURTHER")
                return
        for i in range(len(sec_part)-1):
            #  checking if two operators  are found adjacent then it is invalid grammar
            if sec_part[i] in oper and sec_part[i+1] in oper:
                print("GIVEN GRAMMAR IS NOT OPERATOR GRAMMAR.....REJECTED  FURTHER")
                return
        for i in range(len(sec_part)):
            # checking if  RHS of productions contain any null symbol represented by ^ or ~  then it is not operator grammar.
            if sec_part[i] in oper:
                # the name should be operator_in_given_grammer as you are appending operator
                terminal_in_given_grammar.append(sec_part[i])
            if sec_part[i] == "^" or sec_part[i] == "~":
                print("GIVEN GRAMMAR IS NOT OPERATOR GRAMMAR.....REJECTED  FURTHER")
                return
    
    # print(terminal_in_given_grammar,oper)
    for i in input_ind:
        if i in oper and i not in terminal_in_given_grammar:
            print("OPERATORS PRESENT  IN INPUT STRING  NOT FROM OPERATORS PRESENT  IN GIVEN GRAMMAR .....REJECTED  FURTHER")
            return
    
    order_table = []

    # printing the operator parser table
    with open('order.csv', 'r') as file2:
        order = csv.reader(file2)
        for row in order:
            order_table.append(row)
    operators = order_table[0]
    stack = []
    stack.append('$')
    # print(master)
    print("The given Production rules of the Grammars are: ", master_list, "\n")
    print("The given Productions  of the Grammars are: ", master, "\n")
    print("The given operators  of the Grammars are: ", operators, "\n")
    print("The non-terminal symbols are: ", non_terminals, "\n\n")
    print("<<-----------------------------The operator precedence table is---------------------------->>")
    for row in order_table:
        print("                            ", row)
    print("\n\n")
    print('{:50s}'.format(str("stack")), '{:60s}'.format(str("input_ind")),
          '{:25s}'.format(str("precedence")), '{:30s}'.format(str("action")))
    print()
    flag = 1
    LHS = ""
    RHS = ""
    what_to_action = ""
    given_string=[]
    given_stack=[]
    while flag:
        if input_ind[0] == '$' and len(stack) == 2:
            flag = 0

        length = len(input_ind)
        buffer_inp = input_ind[0]
        
        # checking if front of stack is 'id' and input string front is also 'id' at any situation comes for comparison then it is error. 
        if(stack[-1]==input_ind[0] and stack[-1]=='i'):
            print("Invalid Grammar  or Invalid Input String")
            return
        
        # position of buffer_input in 2-d parsing table ie (temp1,temp1)
        temp1 = operators.index(str(buffer_inp))
        # print("stack", stack, stack[-1])
        buffer_stack = ""
        if stack[-1] in non_terminals:
            buffer_stack = stack[-2]
        else:
            buffer_stack = stack[-1]
        temp2 = operators.index(str(buffer_stack))
        precedence = order_table[temp2][temp1]
        action = ""
        if precedence == '<':
            action = 'shift'
        elif precedence == '>':
            action = 'reduce'
        given_string=deepcopy(input_ind)
        given_stack=deepcopy(stack)
        if action == 'shift':
            stack.append(buffer_inp)
            input_ind.remove(buffer_inp)
        elif action == 'reduce':
            for key, value in master.items():
                var1 = ''.join(stack[-1:])
                var2 = ''.join(stack[-3:])
                if str(key) == str(buffer_stack):
                    LHS = value
                    RHS = stack[-1]
                    stack[-1] = value
                    break
                elif key == var1 or stack[-3:] == list(var1):
                    LHS = value
                    RHS = "".join(stack[-3:])
                    stack[-3:] = value
                    break
                elif key == var2:
                    LHS = value
                    RHS = "".join(stack[-3:])
                    stack[-3:] = value
      
        if action == 'shift':
            what_to_action = buffer_inp
        elif action=='reduce':
            what_to_action = '('+LHS+' -> '+RHS+')'
        else:
            what_to_action="Accepted"
        
        print('{:50s}'.format(str(given_stack)), '{:60s}'.format(str(given_string)),
              '{:25s}'.format(str(precedence)), '{:30s}'.format(str(action)+" "+what_to_action))
        print()
        del buffer_inp, temp1, buffer_stack, temp2, precedence

    if flag == 0:
        print("\n<<--------------------------------------------------STRING   ACCEPTED---------------------------------------->>")
    else:
        print("\n<<--------------------------------------------------STRING   REJECTED---------------------------------------->>")


if __name__ == "__main__":
    sys.exit(main())
