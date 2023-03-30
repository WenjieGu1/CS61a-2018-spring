import string

from buffer import Buffer
from expr import *

SYMBOL_STARTS = set(string.ascii_lowercase + string.ascii_uppercase + '_')
SYMBOL_INNERS = SYMBOL_STARTS | set(string.digits)
NUMERAL = set(string.digits + '-.')
WHITESPACE = set(' \t\n\r')
DELIMITERS = set('(),:')

def read(s):
    """Parse an expression from a string. If the string does not contain an
    expression, None is returned. If the string cannot be parsed, a SyntaxError
    is raised.

    >>> read('lambda f: f(0)')
    LambdaExpr(['f'], CallExpr(Name('f'), [Literal(0)]))
    >>> read('(lambda x: x)(5)')
    CallExpr(LambdaExpr(['x'], Name('x')), [Literal(5)])
    >>> read('(lambda: 5)()')
    CallExpr(LambdaExpr([], Literal(5)), [])
    >>> read('lambda x y: 10')
    Traceback (most recent call last):
      ...
    SyntaxError: expected ':' but got 'y'
    >>> read('  ')  # returns None
    """
    src = Buffer(tokenize(s))
    if src.current() is not None:
        return read_expr(src)

###########
## Lexer ##
###########
def tokenize(s):
    """Splits the string s into tokens and returns a list of them.

    >>> tokenize('lambda f: f(0, 4.2)')
    ['lambda', 'f', ':', 'f', '(', 0, ',', 4.2, ')']
    """
    src = Buffer(s)
    tokens = []
    while True:
        token = next_token(src)
        if token is None:
            return tokens
        tokens.append(token)

def take(src, allowed_characters):
    """以字符串返还src.current和allowed_characters共有的字符，
    并将src移到下一处循环直到没有共有字符，理想结果为返还同一类型且连续的字符"""
    result = ''
    while src.current() in allowed_characters:
        result += src.remove_front()
    return result

def next_token(src):
    """将src的字符按类别重新组成一个完整的字符串，并将src进一位"""
    take(src, WHITESPACE)  # skip whitespace 跳过连续的空格
    c = src.current()
    if c is None:
        return None
    elif c in NUMERAL: #以字符串形式返还连续数字
        literal = take(src, NUMERAL)
        try:
            return int(literal)
        except ValueError:
            try:
                return float(literal)
            except ValueError:
                raise SyntaxError("'{}' is not a numeral".format(literal))
    elif c in SYMBOL_STARTS: #以字符串形式返还连续的SYMBOL_INNERS
        return take(src, SYMBOL_INNERS)
    elif c in DELIMITERS: #遇到分隔符则src进一位，且返还分隔符
        src.remove_front()
        return c
    else:
        raise SyntaxError("'{}' is not a token".format(c))

def is_literal(s):
    return isinstance(s, int) or isinstance(s, float)

def is_name(s):
    return isinstance(s, str) and s not in DELIMITERS and s != 'lambda'

############
## Parser ##
############
def read_expr(src): #接收的src已经tokenize
    token = src.remove_front()
    if token is None:
        raise SyntaxError('Incomplete expression')
    elif is_literal(token):
        return read_call_expr(src, Literal(token))
    elif is_name(token):
        return read_call_expr(src, Name(token))
    elif token == 'lambda':
        params = read_comma_separated(src, read_param)
        src.expect(':')
        body = read_expr(src)
        return LambdaExpr(params, body)
    elif token == '(':
        inner_expr = read_expr(src)
        src.expect(')')
        return read_call_expr(src, inner_expr)
    else:
        raise SyntaxError("'{}' is not the start of an expression".format(token))

def read_comma_separated(src, reader):
    if src.current() in (':', ')'):
        return []
    else:
        s = [reader(src)]
        while src.current() == ',':
            src.remove_front()
            s.append(reader(src))
        return s

def read_call_expr(src, operator):
    while src.current() == '(':
        src.remove_front()
        operands = read_comma_separated(src, read_expr)
        src.expect(')')
        operator = CallExpr(operator, operands)
    return operator

def read_param(src):
    """src首位是名称则返还名称，且进一位"""
    token = src.remove_front()
    if is_name(token):
        return token
    else:
        raise SyntaxError("Expected parameter name but got '{}'".format(token))
