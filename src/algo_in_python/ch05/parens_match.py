#! /usr/bin/env python3
# coding = utf-8

# parens_match.py - 检测一段文本中的括号是否匹配


def check_parens(text):
    "括号配对检测函数，text是被检查的正文串"
    parens = '()[]{}'
    open_parens = '([{'
    opposite = {')': '(', ']': '[', '}': '{'}

    def parentheses(text):
        "括号生成器，每次调用都返回text里的下一个括号及其位置"
        i, text_len = 0, len(text)
        while True:
            while i < text_len and text[i] not in parens:
                i += 1
            if i >= text_len:
                return
            yield text[i], i
            i += 1

    stack = []
    for ch, i in parentheses(text):
        print(stack)
        if ch in open_parens:
            stack.append(ch)
        elif (not stack) or (stack.pop() != opposite[ch]):
            print("Unmatching is found at", i, "for", ch)
            return False
        else:
            # 这是一次括号配对成功，什么也不做，继续
            pass
    print('All parentheses are correctly matched.')
    return True

if __name__ == '__main__':
    text = '[( 1 + 2 + 3 + (4 + 5))])'
    print(check_parens(text))
