def calcular_area_comodos(): #criação da função calcular_area_comodos.
    total_area = 0 #definindo valor inicial de var = 0.

    while True: #loop while condicionado por Boolean.

        largura = float(input("Digite a largura do cômodo (em metros): ")) #pedindo para usuario informar valor e atribuindo tal valor(formatado para float) à var.
        comprimento = float(input("Digite o comprimento do cômodo (em metros): ")) #mesma coisa, porém para outra var.

        area_comodo = largura * comprimento #calculo de valor e atribuição deste á uma var.
        print(f"A área deste cômodo é: {area_comodo:.2f} metros quadrados.") #print da var definida na linha acima.

        total_area += area_comodo #calculo continuo de uma var que terá seu valor atualizado a cada loop.

        mais_comodos = input("Deseja adicionar mais cômodos? (s/n): ").strip().lower() #pedindo para usuario informar valor a ser atribuído a var(string) e formatando ela para ficar separada e em lowercase.
        if mais_comodos != 's': #se a var mais_comodos tiver valor diferente de 's', quebra o loop.
            break

        return total_area #retorna valor da var total_area a cada loop, pois a var total_area vai mudando a cada loop.

area_total = calcular_area_comodos() #atribui o valor retornado da funcao à uma var.
print(f"A área total da casa é: {area_total:.2f} metros quadrados.") #exibe o valor desta var formatada e contextualizada para o usuario.