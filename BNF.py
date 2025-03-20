# parser for a BNF language
# start rule
# START ='<Expr>'
START = '<sentence>'
# empty symbol
EMPTY = chr(0)
# rules dictionary
# an empty rule, if present, must always be the LAST alternative
# a rule name is surrounded in '<' ... '>'

rules = {
    '<sentence>': ('<simple-sentence><and>',),
    '<and>': ('and<simple-sentence>', EMPTY,),
    '<simple-sentence>': ('<noun-part><verb-part>',),
    '<noun-part>': ('<article><noun><who>',),
    '<who>': ('who<verb-part>', EMPTY,),
    '<verb-part>': ('runs', 'jumps', 'hides', 'knows<noun-part>', 'loves<noun-part>', 'chases<noun-part>', 'owns<noun-part>',),
    '<article>': ('the', 'a',),
    '<noun>': ('man', 'woman', 'dog', 'cat', 'computer',),
}
    # '<intransitive-verb>': ('runs', 'jumps', 'hides', 'knows', 'loves', 'chases', 'owns',),
    # '<verb-part>': ('<intransitive-verb><verb>',),
    # '<verb>': ('<noun-part>', EMPTY,),
# set to True to get trace messages
DEBUG = False

delimiters = ( ' ', '+', '-', '*', '/', '(', ')', )

def rprint(matches, stack):
    # print matches and current stack. top is printed first.
    print("Matched:",matches, end=' ')
    temp=[]
    for k in range(len(stack)-1, -1, -1):
        temp.append(stack[k])
    print("Stack:", temp)
    # only print the 'empty' match once. So remove it.
    temp2 = [m for m in matches if m!='empty']
    matches.clear()
    matches.extend(temp2)
    return

def match(rule, s):
    # return True if s matches the first part of rule
    return rule.startswith(s)

def inputTokenizer(s):
    # split input into tokens based on space ' ' and list of delimiters
    tokens=[]
    token=''
    for c in s:
        if c in delimiters:
            if len(token)>0:
                tokens.append(token)
                token=''
            if c!=' ':
                tokens.append(c)
        else:
            token+=c
    if len(token)>0:
        tokens.append(token)
    return tokens

# given a rule that consists of terminal symbols and rule names
# such as '+<Term>-(<Factor>*<Factor>)
# return a list of token strings
# ['+', '<Term>', '-', '(', '<Factor>', '*', '<Factor>', ')' ]
# The character '\' is processed as an escape character if
# the chars '<' or '>' are used as terminal symbols.

def ruleTokenizer(s):
    tokens=[]
    token=''
    t=0
    escape=False
    for c in s:
        if c=='\\' and escape == False:
            escape=True
        elif escape==True:
            escape=False
            token+=c
        elif c=='<' and t==0: #start of <id>
            if len(token)>0:
                tokens.append(token)
            token='<'
            t=1
        elif c=='>' and t==1: #end of <id>
            token+=c
            t=0
            tokens.append(token)
            token=''
        elif t==0: # not in an <id>
            if c==' ':
                tokens.append(token)
                token=''
            else:
                token+=c
        elif t==1: #middle of <id>
            token+=c
    if len(token)!=0:
        tokens.append(token)
    return tokens

def pushRuleToStack(rule, stack):
    # push in reverse order.
    tokens = ruleTokenizer(rule)
    tokens.reverse()
    for t in tokens:
        stack.append(t)
    return

# algorithm
# 1. push start symbol to stack
# split user input into a list of tokens
#
# 2. while stack not empty
# top = pop stack
# if top is a rule
# if there is only one choice for this rule, then push the rhs(Right Hand Side) to the stack
# if this rule has multiple choices, pick the one that starts with the next input token and
# push that to the stack
# if one of the alternative is <EMPTY> then just continue
# otherwise we have a syntax error
# if top is a terminal symbol
# if top matches next token then discard the token and continue
# otherwise, there is a syntax error
#
# 3. when the stack is empty, if all input tokens have
# been processed then accept the string, otherwise syntax error.
#
print("Type a space between tokens.")
print("Enter DEBUG to switch debug mode on or off");
print("Enter quit to end.")

while True:
    line = input("Enter a string:").strip()
    if line=='quit':
        break
    if line=='DEBUG':
        if DEBUG:
            DEBUG = False
            print("DEBUG off")
        else:
            DEBUG = True
            print("DEBUG on")
        continue
    tokens = inputTokenizer(line)
    if DEBUG: print("input tokens", tokens)

    # push start symbol to stack. Top of stack is last element in list.
    stack = [START]
    accept = True
    matches = []

    while len(stack)>0:
        rprint(matches, stack)
        # pop the stack
        top = stack.pop()
        if DEBUG:
            if len(tokens)>0:
                print("top of stack",top,"next input token",tokens[0],"stack",stack)
        else:
            print("top of stack",top,"no more input tokens. ","stack",stack)
        if (top not in rules and top.startswith('<') and len(top)>1):
            print("Warning: you may be missing a rule for", top)

        if top in rules:
            rhs = rules[top]
            # process a rule
            # are there any choices in the rule?
            if len(rhs)==1:
                # there is only one choice,
                # push that rule to the stack
                pushRuleToStack(rhs[0],stack)
            else:
                # the rule has multiple choice.
                # pick the correct choice from the next input token.
                found=False
                for alt in rhs:
                    if len(tokens)>0 and match(alt,tokens[0]):
                        # found a match. Push that rule to the stack
                        found=True
                        pushRuleToStack(alt, stack)
                        break
                    if alt==EMPTY:
                        # empty rule. Automatic match. Nothing to push.
                        found=True
                        matches.append("empty")
                        break
                if not found:
                    if len(tokens)>0 :
                        print("Syntax error", "token:", tokens[0], "expected:", rhs)
                    
                    else:
                        print("Syntax error", "no token.", "expected:", rhs)
                    accept=False
                    break

        # does top match next input token
        elif len(tokens)>0 and tokens[0]==top:
            # yes, a match. Discard the input token and continue.
            tokens.pop(0)
            matches.append(top)
            continue
        else:
            accept=False ## syntax error in input.
            break

    # come here when stack is empty.
    rprint(matches, stack)
    if accept and len(tokens)==0:
        print("accept")
    else:
        print("reject")

print('Goodbye.')
