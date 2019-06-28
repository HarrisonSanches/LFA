from lark import Lark
gramatica = """
	start:expr 
	expr: (term) (("+" | "-") (term))?
	term : (factor) (("*" | "/" | "//" | "%") (factor))?
	factor : (base) ("^" (factor))?
	base : ("+" | "-") (base) | NUMBER | "(" expr ")"

    %import common.SIGNED_NUMBER -> NUMBER
    %import common.WS_INLINE
    %ignore WS_INLINE
    """


parser = Lark(gramatica)


def main(args):
	
	expression = input("")
	try:
		expressao = parser.parse(expression)
		print("Expressão matemática válida")
	except:
		print('Expressão matemática incorreta')
 
	return 0

if  __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
