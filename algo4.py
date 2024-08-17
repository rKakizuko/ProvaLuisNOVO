def calcular_media_e_aprovacao(notas, nota_minima_aprovacao): #criação da função calcular_media_e_aprovacao com vars que serão definidas fora da função e serão passadas por parametro.
    total_notas = 0 #atribuindo valor inicial a var = 0
    num_alunos = len(notas) #atribuindo valor da var em questão pelo tamanho de items do dicionario notas
    aprovados = [] #criação de lista aprovados sem valor
    reprovados = [] #criação de lista reprovados sem valor

    for aluno, nota in notas.items(): #criação de um loop que utiliza vars para continuar até todas serem utilizadas
        total_notas += nota #var cujo valor é atualizado a cada loop.
    if nota >= nota_minima_aprovacao: #criação de condicional para caso var nota seja maior ou igual a var nota_minima_aprovacao adicionar o aluno proprietário da nota á lista aprovados
        aprovados.append(aluno)
    else:
        reprovados.append(aluno) #caso não cumpra a condição imposta anterior mente, adiciona a lista reprovados

    media_turma = total_notas / num_alunos #atribuição de calculo à var media_turma

    return media_turma, aprovados, reprovados #função retorna valores de vars manipuladas dentro dela, mais especificamente uma var com valor int e duas listas. 

notas = { #criação do dicionario que será utilizado na função.
"Alice": 85,
"Bruno": 72,
"Carlos": 60,
"Diana": 95,
"Eduardo": 55
}

nota_minima_aprovacao = 70 #atribuição de valor à var global para poder ser usada na função.

media_turma, aprovados, reprovados = calcular_media_e_aprovacao(notas, nota_minima_aprovacao) #atribuição de valores a vars do que foi retornado da função.

print(f"Média da turma: {media_turma:.2f}") #print contextualizados e formatadas utilizando as vars com valores retornados da função.
print(f"Alunos aprovados: {', '.join(aprovados)}")
print(f"Alunos reprovados: {', '.join(reprovados)}")