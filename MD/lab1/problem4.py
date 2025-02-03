from typing import Set
from typing import List
from prettytable import PrettyTable
import re

class Solution:
    res_chars = {"*", "!", "+", "(", ")", " ", "  ", "   "}
    opps = { "!" : " not ", "+": " or ", "*": " and "}

    def extractVariables(self, expression_string: str):
        unique_variables: Set[str] = set()

        for i in range(len(expression_string)):
            if (
                expression_string[i] not in self.res_chars
                and expression_string[i] not in unique_variables
            ):
                unique_variables.add(expression_string[i])

        return sorted(unique_variables)

    def generateTruthTable(self, expression_string: str):
        table = PrettyTable()
        table.field_names = []

        unique_variables_list: List[str] = self.extractVariables(expression_string)
        table.field_names = unique_variables_list + [expression_string]

        expression_template = expression_string
        for opp in self.opps.keys():
            expression_template = expression_template.replace(opp, self.opps[opp])

        for i in range(2**len(unique_variables_list)):
            expression_res = expression_template
            row = []
            for j in range(len(unique_variables_list)):
                pattern = re.compile(rf"\b{unique_variables_list[j]}\b")
                if i & (1 << j):
                    expression_res = pattern.sub("True", expression_res)
                    row.append(1)
                else:
                    expression_res = pattern.sub("False", expression_res)
                    row.append(0)

            res = eval(expression_res)
            row.append(1 if res else 0)
            table.add_row(row)

        print(table)

solution = Solution()

print("Expression example: (!x + y) * z + (!z * y * k)")
input = input("Input the expression: ")
print(solution.generateTruthTable(input))

