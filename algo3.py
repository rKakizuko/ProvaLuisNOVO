def diagnosticar_diabetes(glicemia_em_jejum, glicemia_pos_prandial): #criação da função diagnosticar_diabetes usando as var glicemia_em_jejum e glicemia_pos_prandial que serão definidas fora da função.

    if glicemia_em_jejum >= 126 or glicemia_pos_prandial >= 200: #caso a var em questão seja menor ou igual 126 ou a outra var seja maior ou igual a 200, a função retorna Diabetes
        return "Diabetes"
    elif 100 <= glicemia_em_jejum < 126 or 140 <= glicemia_pos_prandial < 200: #caso a var glicemia_em_jejum esteja entre 100 e 126 ou a var glicemia_pos_prandial esteja entre 140 e 200, retorna Pré-diabetes
        return "Pré-diabetes"
    else:
        return "Normal" #se não cumprir nenhum dos casos acima, retorna Normal.

glicemia_em_jejum = float(input("Digite o valor da glicemia em jejum (mg/dL): ")) #pede para o usuario informar valores que serão atribuidos as vars de maneira contextualizada.
glicemia_pos_prandial = float(input("Digite o valor da glicemia pós-prandial (mg/dL): "))

resultado = diagnosticar_diabetes(glicemia_em_jejum, glicemia_pos_prandial) #atribui valor que foi retornado da funçao a uma var resultado.
print(f"O diagnóstico é: {resultado}") #printa valor dentro de resultado formatado com contexto.