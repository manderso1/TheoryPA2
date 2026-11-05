import sys
class CFG:
    def __init__(self, terminals, variables, productions):
        self.terminals = terminals 
        self.variables = variables
        self.productions = productions

    def apply_single_product(self, string, index, left):
        if left == True:
            for s in range(len(string)):
                if string[s] in self.variables:
                    varArray = self.productions.get(string[s], [])[index]
                    return string[:s] + varArray + string[s+1:]
            return string
        elif left == False:
            for s in range(1, len(string) + 1):
                if string[-s] in self.variables:
                    varArray = self.productions.get(string[-s], [])[index]
                    rightside = string[-s+1] if -s+1 < 0 else ""
                    return string[:-s] + varArray + rightside
            return string



def read_from_stdin1():
    terminals = input()
    terminals = eval(terminals)

    variables = sys.stdin.readline()
    variables = eval(variables)

    productions = sys.stdin.readline()
    productions = eval(productions)

    
    return terminals, variables, productions

def read_from_stdin1a():
    terminals, variables, productions = read_from_stdin1()

    mystring = eval(sys.stdin.readline())
    rule_num = eval(sys.stdin.readline())
    left = eval(sys.stdin.readline())

    return terminals, variables, productions, mystring, rule_num, left

if __name__ == "__main__":
    terminals, variables, productions, mystring, rule_num, left = read_from_stdin1a()

    cfg = CFG(terminals, variables, productions)

    print(cfg.apply_single_product(mystring, rule_num, left))
    
