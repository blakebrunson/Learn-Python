# Assignment
# Students in primary school often arrange arithmetic problems vertically to make them easier to solve. For example, "235 + 52" becomes:

#   235
# +  52
# -----

# Create a function that receives a list of strings that are arithmetic problems and returns the problems arranged vertically and side-by-side. The function should optionally take a second argument. When the second argument is set to True, the answers should be displayed.

# For example

# Function Call:
# arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])

# Output:

#    32      3801      45      123
# + 698    -    2    + 43    +  49
# -----    ------    ----    -----


# Function Call:
# arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)

# Output:

#   32         1      9999      523
# +  8    - 3801    + 9999    -  49
# ----    ------    ------    -----
#   40     -3800     19998      474


# RULES

# The function will return the correct conversion if the supplied problems are properly formatted, otherwise, it will return a string that describes an error that is meaningful to the user.

# Situations that will return an error:
# If there are too many problems supplied to the function. The limit is five, anything more will return:
# Error: Too many problems.
# The appropriate operators the function will accept are addition and subtraction. Multiplication and division will return an error. Other operators not mentioned in this bullet point will not need to be tested. The error returned will be:
# Error: Operator must be '+' or '-'.
# Each number (operand) should only contain digits. Otherwise, the function will return:
# Error: Numbers must only contain digits.
# Each operand (aka number on each side of the operator) has a max of four digits in width. Otherwise, the error string returned will be:
# Error: Numbers cannot be more than four digits.
# If the user supplied the correct format of problems, the conversion you return will follow these rules:
# There should be a single space between the operator and the longest of the two operands, the operator will be on the same line as the second operand, both operands will be in the same order as provided (the first will be the top one and the second will be the bottom.
# Numbers should be right-aligned.
# There should be four spaces between each problem.
# There should be dashes at the bottom of each problem. The dashes should run along the entire length of each problem individually. (The example above shows what this should look like.)



def arithmetic_arranger(lst, answers=None):
    inputCount = 0
    showAnswers = 0
    leng = 0
    folder = list()
    for item in lst :
        if type(item) == str : 
            inputCount = inputCount + 1
            folder.append(item.split())
        else :
            arranged_problems = "error message goes here - one or more invalid imputs."
            return arranged_problems
    
    if answers == True :
        showAnswers = 1

    if inputCount > 5 :
        arranged_problems = "Error: Too many problems."
        return arranged_problems

    import re
    for item in folder :
        for piece in item : 
            if len(piece) > 4 :
                arranged_problems = "Error: Numbers cannot be more than four digits."
                return arranged_problems
            elif re.search('[A-Za-z]+',piece) != None :
                arranged_problems = "Error: Numbers must only contain digits."
                return arranged_problems

    for item in folder :
        leng = len(item[0])
        if len(item[2]) > leng :
            leng = len(item[2])
            topAlign = len(item[2]) - len(item[0])
            bottomAlign = 0
            item.append(topAlign)
            item.append(bottomAlign)
        else :
            topAlign = 0
            bottomAlign = len(item[0]) - len(item[2])
            item.append(topAlign)
            item.append(bottomAlign)

        operator = item[1]
        if operator == "+" :
            result = int(item[0]) + int(item[2])
            item.append(str(result))
            item.append(leng)
            item.append(leng + 2 - len(str(result)))
        elif operator == "-" :
            result = int(item[0]) - int(item[2])
            item.append(str(result))
            item.append(leng)
            item.append(leng + 2 - len(str(result)))
        else : 
            arranged_problems = "Error: Operator must be '+' or '-'."
            return arranged_problems
        
# Below could be re-written as a While loop in much fewer lines

    if inputCount == 5 :
        arranged_problems = ('  ' + folder[0][3] * ' ' + folder[0][0] + '      ' + folder[1][3] * ' ' + folder[1][0] + '      ' + folder[2][3] * ' ' + folder[2][0] + '      ' + folder[3][3] * ' ' + folder[3][0] + '      ' + folder[4][3] * ' ' + folder[4][0] + '\n' + folder[0][1] + ' ' + folder[0][4] * ' ' + folder[0][2] + '    ' + folder[1][1] + ' ' + folder[1][4] * ' ' + folder[1][2] + '    ' + folder[2][1] + ' ' + folder[2][4] * ' ' + folder[2][2] + '    ' + folder[3][1] + ' ' + folder[3][4] * ' ' + folder[3][2] + '    ' + folder[4][1] + ' ' + folder[4][4] * ' ' + folder[4][2] + '\n' + (folder[0][6] + 2) * '-' + '    ' + (folder[1][6] + 2) * '-' + '    ' + (folder[2][6] + 2) * '-' + '    ' + (folder[3][6] + 2) * '-' + '    ' + (folder[4][6] + 2) * '-')
        if showAnswers == 1 :
            arranged_problems = (arranged_problems + '\n' + folder[0][7] * ' ' + folder[0][5] + '  ' + folder[1][7] * ' ' + folder[1][5] + '  ' + folder[2][7] * ' ' + folder[2][5] + '  ' + folder[3][7] * ' ' + folder[3][5] + '  ' + folder[4][7] * ' ' + folder[4][5])

    elif inputCount == 4 :
        arranged_problems = ('  ' + folder[0][3] * ' ' + folder[0][0] + '      ' + folder[1][3] * ' ' + folder[1][0] + '      ' + folder[2][3] * ' ' + folder[2][0] + '      ' + folder[3][3] * ' ' + folder[3][0] + '\n' + folder[0][1] + ' ' + folder[0][4] * ' ' + folder[0][2] + '    ' + folder[1][1] + ' ' + folder[1][4] * ' ' + folder[1][2] + '    ' + folder[2][1] + ' ' + folder[2][4] * ' ' + folder[2][2] + '    ' + folder[3][1] + ' ' + folder[3][4] * ' ' + folder[3][2] + '\n' + (folder[0][6] + 2) * '-' + '    ' + (folder[1][6] + 2) * '-' + '    ' + (folder[2][6] + 2) * '-' + '    ' + (folder[3][6] + 2) * '-')
        if showAnswers == 1 :
            arranged_problems = (arranged_problems + '\n' + folder[0][7] * ' ' + folder[0][5] + '    ' + folder[1][7] * ' ' + folder[1][5] + '    ' + folder[2][7] * ' ' + folder[2][5] + '    ' + folder[3][7] * ' ' + folder[3][5])

    elif inputCount == 3 :
        arranged_problems = ('  ' + folder[0][3] * ' ' + folder[0][0] + '      ' + folder[1][3] * ' ' + folder[1][0] + '      ' + folder[2][3] * ' ' + folder[2][0] + '\n' + folder[0][1] + ' ' + folder[0][4] * ' ' + folder[0][2] + '    ' + folder[1][1] + ' ' + folder[1][4] * ' ' + folder[1][2] + '    ' + folder[2][1] + ' ' + folder[2][4] * ' ' + folder[2][2] + '\n' + (folder[0][6] + 2) * '-' + '    ' + (folder[1][6] + 2) * '-' + '    ' + (folder[2][6] + 2) * '-')
        if showAnswers == 1 :
            arranged_problems = (arranged_problems + '\n' + folder[0][7] * ' ' + folder[0][5] + '    ' + folder[1][7] * ' ' + folder[1][5] + '    ' + folder[2][7] * ' ' + folder[2][5])

    elif inputCount == 2 :
        arranged_problems = ('  ' + folder[0][3] * ' ' + folder[0][0] + '      ' + folder[1][3] * ' ' + folder[1][0] + '\n' + folder[0][1] + ' ' + folder[0][4] * ' ' + folder[0][2] + '    ' + folder[1][1] + ' ' + folder[1][4] * ' ' + folder[1][2] + '\n' + (folder[0][6] + 2) * '-' + '    ' + (folder[1][6] + 2) * '-')
        if showAnswers == 1 :
            arranged_problems = (arranged_problems + '\n' + folder[0][7] * ' ' + folder[0][5] + '    ' + folder[1][7] * ' ' + folder[1][5])

    elif inputCount == 1 :
        arranged_problems = ('  ' + folder[0][3] * ' ' + folder[0][0] + '\n' + folder[0][1] + ' ' + folder[0][4] * ' ' + folder[0][2] + '\n' + (folder[0][6] + 2) * '-')
        if showAnswers == 1 :
            arranged_problems = (arranged_problems + '\n' + folder[0][7] * ' ' + folder[0][5])
    
    else:
        print('No valid inputs')
    
    return arranged_problems


print(arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", True]))



