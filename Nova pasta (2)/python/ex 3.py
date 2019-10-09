idadeanos = int(input('digite a quantidade de anos: '))
idademeses = int(input('Digite a quantidade de meses: ')) 
idadedias = int(input('digite a quantidade de dias: '))
#o comando \n serve para quebrar a linha
idaderesult = (idadeanos * 365) + (idademeses * 30) + idadedias

print('a pessoa tem {} dias de vida'. format(idaderesult))