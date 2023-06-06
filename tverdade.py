def verificar_expressao(expressao):
    contador = 0
    caracteres_proibidos = "+\-/#$'%*=@"

    for caractere in expressao:
        if caractere.isdigit() or caractere in caracteres_proibidos:
            return False
        if caractere == '(':
            contador = contador + 1
        elif caractere == ')':
            contador = contador - 1
            if contador < 0:
                return False

    if contador == 0:
        return True

def extrair_variaveis(expressao):
    variaveis = []
    for caractere in expressao:
        if caractere.isalpha() and caractere not in variaveis:
            variaveis.append(caractere)

    if len(variaveis) > 0:
        return variaveis
    else:
        return False


def gerar_combinacoes(variaveis):
    n = len(variaveis)
    valores = [True, False]
    combinacoes = []

    for i in range(2**n):
        d = {}
        for j in range(n):
            d[variaveis[j]] = valores[(i >> j) & 1]
        combinacoes.append(d)
    return combinacoes
 
def analisar_expressao(expressao, combinacoes):
    expressao = expressao.replace("&", "and")
    expressao = expressao.replace("|", "or")
    expressao = expressao.replace("!", "not ")
    resultados = []
    for combinacao in combinacoes:
        resultados.append(eval(expressao, {}, combinacao))
    return resultados

def imprimir_tabela(variaveis, expressao, combinacoes, resultados):
    for var in variaveis:
        print(var, end="\t")
    print(expressao)
    for index, combinacao in enumerate(combinacoes):
        for var in variaveis:
            print(combinacao[var], end="\t")
        print(resultados[index])

def menu():
    menu = """Observações:
1. esse programa entende até 4 entradas (A, B, C e D)
2. digite uma expressão válida
3. considere que: 
    &\t: E
    |\t: OU
    !\t: Negação
"""    
    print(menu)
    return menu

if __name__ == '__main__':
    iniciar = True
    _ = menu()
    while iniciar:
        # expressao = input("Digite uma expressão válida: ")
        expressao = "(A & B) | !C"
        expr_valida = verificar_expressao(expressao)
        variaveis = extrair_variaveis(expressao)
        if expr_valida and variaveis:
            print("Expressão é válida, segue a tabela verdade")
            combinacoes = gerar_combinacoes(variaveis)
            resultados = analisar_expressao(expressao, combinacoes)
            # print(combinacoes)
            imprimir_tabela(variaveis, expressao, combinacoes, resultados)
          
            terminar = input("Deseja finalizar? (s/n) ")
            if terminar in "sS":
                iniciar = False
            else:
                continue
        else:
            print("Expressão inválida, tente novamente")

    print("Obrigado por usar a calculadora")