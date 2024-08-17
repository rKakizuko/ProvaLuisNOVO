def calcular_imc(peso, altura): #criação da função calcular_imc usando vars que serão passadas por parametro para a função.

    imc = peso / (altura ** 2) #atribuição de valor a var usando calculo envolvendo outras duas vars.
    return imc #retorna o valor da var atribuida na linha acima

def classificar_imc(imc): #criação da função classificar_imc com uma var que será passada por parametro.

    if imc < 18.5:                  #criação de condicionais que dependendo de qual condicional for cumprida ou caso nenhuma seja cumprida, faz a função retornar uma string em específica.
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    elif 30 <= imc < 34.9:
        return "Obesidade grau 1"
    elif 35 <= imc < 39.9:
        return "Obesidade grau 2"
    else:
        return "Obesidade grau 3"

def sugestao_atividade_fisica(classificacao_imc):#criação da função sugestao_atividade_fisica com var a ser passada por parametro

    if classificacao_imc == "Abaixo do peso": #criação de condicionais que de acordo com o que estiver armazenado dentro da var classificacao_imc faz a função retornar uma string especifica.
        return "Sugere-se atividades de fortalecimento muscular, como musculação, e uma dieta rica em proteínas e calorias."
    elif classificacao_imc == "Peso normal":
        return "Sugere-se a manutenção com atividades aeróbicas regulares, como caminhada, corrida leve e natação, junto a um treino de força moderado."
    elif classificacao_imc == "Sobrepeso":
        return "Sugere-se atividades aeróbicas moderadas, como caminhada rápida, ciclismo e natação, além de exercícios de resistência."
    elif classificacao_imc == "Obesidade grau 1":
        return "Sugere-se atividades de baixo impacto, como caminhadas, natação e hidroginástica, junto a um programa de reeducação alimentar."
    elif classificacao_imc == "Obesidade grau 2":
        return "Sugere-se exercícios de baixo impacto com supervisão, como hidroginástica e pilates, e acompanhamento nutricional."

    else:
        return "Sugere-se atividades físicas supervisionadas por profissionais de saúde, como hidroginástica, fisioterapia, e consultas regulares com um nutricionista."

peso = float(input("Digite seu peso (em kg): ")) #atribuindo valores a vars por meio de dados inseridos manualmente pelo usuário de maneira contextualizada.
altura = float(input("Digite sua altura (em metros): "))

imc = calcular_imc(peso, altura) #atribuindo valores a vars globais para que sejam utilizadas nas funções e em outros casos.
classificacao_imc = classificar_imc(imc)
sugestao = sugestao_atividade_fisica(classificacao_imc)

print(f"Seu IMC é: {imc:.2f}") #exibição das vars com seus respectivos contextos.
print(f"Classificação: {classificacao_imc}")
print(f"Sugestão de atividade física: {sugestao}")