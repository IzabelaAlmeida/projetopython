arrayPalavra = ["acbda", "fasdlkh", "poiwqd", "zxcqwtop", "qfgophl"]
sequenciaArray = [] 
for palavra in arrayPalavra:
  sequencia = []
  maiorSequenciaPalavra = []
  subSequencia = palavra[0]
  for letra in palavra[1:]:
    if letra >= subSequencia[-1]:
        subSequencia += letra
    else:
      sequencia.append(subSequencia)
      subSequencia = letra
    sequencia.append(subSequencia)
    maiorSequenciaPalavra = max(sequencia, key=len)
    sequenciaArray.append(maiorSequenciaPalavra)
    
 
maiorSequencia = max(sequenciaArray, key=len)
print(maiorSequencia)