def calcular_custo_viagem(distancia, custo_combustivel, consumo_veiculo, numero_pedagios, custo_pedagio): #criação da função calcular_custo_viagem usando vars que serão passadas por parametro.

    custo_combustivel_total = (distancia / consumo_veiculo) * custo_combustivel 

    custo_pedagio_total = numero_pedagios * custo_pedagio                   #atribuindo valores a vars locais utilizando outras vars (globais e locais) e cálculos matemáticos.

    custo_total = custo_combustivel_total + custo_pedagio_total

    return custo_total, custo_combustivel_total, custo_pedagio_total #função retorna os valores armazenados nas vars manipuladas localmente.

distancia = float(input("Digite a distância da viagem (em km): "))                      #atribuição de valores a vars manualmente feitos pelo usuário e com contexto em cada uma, além de formatação para float.
custo_combustivel = float(input("Digite o custo do combustível por litro (em R$): "))
consumo_veiculo = float(input("Digite o consumo do veículo (km por litro): "))
numero_pedagios = int(input("Digite o número de pedágios no percurso: "))
custo_pedagio = float(input("Digite o custo de um pedágio (em R$): "))

custo_total, custo_combustivel_total, custo_pedagio_total = calcular_custo_viagem(distancia, custo_combustivel, consumo_veiculo, numero_pedagios, custo_pedagio) #atribuição de valores a vars com os valores retornados da função.

print(f"Custo total da viagem: R${custo_total:.2f}") #exibição dos valores das vars com seus respectivos contextos.
print(f"Custo total com combustível: R${custo_combustivel_total:.2f}")
print(f"Custo total com pedágios: R${custo_pedagio_total:.2f}")