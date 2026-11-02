import sys
class Grammars:
    def __init__(self, terminals, variables, productions):
        self.terminals = terminals 
        self.variables = variables
        self.productions = productions

    def apply_single_product(self, string, index, left):
        if left == True:
            pass



        



    def read_from_stdin1():
        terminals = input()
        terminals = eval(terminals)

        variables = sys.stdin.readline()
        variables = eval(variables)

        productions = sys.stdin.readline()
        productions = eval(productions)

        mystring = sys.stdin.readline()
        mystring = eval(mystring)

        rule_num = sys.stdin.readline()
        rule_num = eval(rule_num)

        left = sys.stdin.readline()
        left = eval(left)

        return terminals, variables, productions, mystring, rule_num, left

CFG = Grammars()