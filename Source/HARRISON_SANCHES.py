from lark import Lark
#GRAMÁTICA DEFINIDA CONFORME ESPECIFICAÇÃO DO TRABALHO 1
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

#UTILIZANDO A GRAMATICA PRA GERAR O PARSER
parser = Lark(gramatica)


def main(args):
	#INPUT PARA EXPRESSÃO MATEMÁTICA
	expression = input("")
	#VERIFICAÇÃO DE RETORNO DE VALIDAÇÃO
	try:
		expressao = parser.parse(expression)
		print("Expressão matemática válida")
	except:
		print('Expressão matemática incorreta')
 
	return 0

if  __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
