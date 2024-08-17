def calcular_juros_atraso(valor_principal, taxa_juros_anual, dias_atraso): #criação da função calcular_juros_atraso com 3 variáveis.
  
 taxa_juros_diaria = taxa_juros_anual / 365 / 100  #atribuindo à variável taxa_juros_diaria valor resultante de um calculo usando a var taxa_juros_anual.
  
 juros = valor_principal * taxa_juros_diaria * dias_atraso  #atribuindo valor à var juros com a multiplicação de outras var entre si.
  
 valor_total = valor_principal + juros  #atribuindo valor à var valor_total por meio da soma de outras duas var.
 return valor_total, juros  #dando dois valores de retorno à função calcular_juros_atraso usando o valor das var valor_total e juros.
valor_principal = 1000.00  #atribuindo valores às var que serão usadas na função
taxa_juros_anual = 5.0  
dias_atraso = 30  
valor_total, juros = calcular_juros_atraso(valor_principal, taxa_juros_anual, dias_atraso) #atribuindo valor de forma global as var valor_total e juros usando os valores de retorno da função que usou as outras var para fazer os calculos dentro dela.
print(f"Valor total a ser pago: R${valor_total}")  #printando de maneira formatada as duas var com seus contextos.
print(f"Valor dos juros: R${juros:.2f}")
