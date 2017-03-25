#! /usr/bin/env python3
# coding = utf-8

# exp_calc.py - 表达式计算

# 定义一些全局的数据

# 运算符号优先级, 给开括号“(”一个很低的优先级，保证其他运算符都不会将其弹出，只有对应的
# “)” 才能弹出它
priority = {'(': 1, "+": 3, "-": 3, "*": 5, "/": 5}
# 中缀表达式时，将括号也考虑为运算符
infix_operators = "+-*/()"


def tokens(line):
    """
    生成器函数，逐一生成line中的一个个项。项是浮点数或运算符。
    本函数不能处理一元运算符。也不能处理带符号的浮点数。
    """
    i, llen = 0, len(line)
    while i < llen:
        while line[i].isspace():
            i += 1
        if i >= llen:
            break
        if line[i] in infix_operators:
            yield line[i]
            i += 1
            continue
        # 下面处理运算对象
        j = i + 1
        while (j < llen and not line[j].isspace() and
               line[j] not in infix_operators):
            # 处理负指数
            if ((line[j] == 'e' or line[j] == 'E') and
                    j + 1 < llen and line[j + 1] == '-'):
                j += 1
            j += 1
        yield line[i:j]
        i = j


def trans_infix_suffix(line):
    "将中缀表达式转换成后缀表达式"
    st = []
    exp = []
    for x in tokens(line):
        # 运算对象直接送出
        if x not in infix_operators:
            exp.append(x)
        # 左括号进展
        elif (not st) or x == '(':
            st.append(x)
        # 处理右括号的分支
        elif x == ')':
            while st and st[-1] != '(':
                exp.append(st.pop())
            # 如果没有配对的 “(”, 解析失败
            if not st:
                raise SyntaxError("Missing '('.")
            st.pop()
        else:
            while st and priority[st[-1]] >= priority[x]:
                exp.append(st.pop())
            st.append(x)
    # 送出栈里剩下的运算符，如果还有“(”就是不匹配
    while st:
        if st[-1] == '(':
            raise SyntaxError("Extra '('.")
        exp.append(st.pop())
    return exp


def suffix_exp_evaluator(exp):
    "基于后缀表达式的四则运算"
    operators = '+-*/'
    stack = []
    for x in exp:
        # 如果不在
        if x not in operators:
            stack.append(float(x))
            continue
        if len(stack) < 2:
            # 栈内元素不够时抛异常
            raise SyntaxError('Short of operand(s)')
        # 弹出操作数
        a = stack.pop()
        b = stack.pop()
        if x == '+':
            c = a + b
        elif x == '-':
            c = a - b
        elif x == '*':
            c = a * b
        else:
            c = a / b
        # 将计算结果压入栈
        stack.append(c)
    # 返回结果
    if len(stack) == 1:
        return stack.pop()
    raise SyntaxError('Extra operand(s).')


def infix_exp_calculator():
    while True:
        try:
            line = input('Infix Expression: ')
            if line == 'q':
                return
            exp = trans_infix_suffix(line)
            res = suffix_exp_evaluator(exp)
            print(res)
        except Exception as ex:
            print('Error:', type(ex), ex.args)

if __name__ == '__main__':
    infix_exp_calculator()
