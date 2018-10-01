import json
import itertools

from multiprocessing.pool import ThreadPool
from operator import itemgetter

t = []

def getInputFromFile(route):
    file = open(route, 'r');
    file_content = json.loads(' '.join(file.readlines()))
    file.close();    
    return file_content

def selectTypeInput():   
    try:      
        print("  (1) Ingresar ruta de archivo JSON \n"+
              "  (2) Ingresar Manualmente la información", end="")
        option = int(input("Ingrese la opción: "))
        return option
    except ValueError:
        print("El valor ingresado no es un entero")
        
def getAttributes(jsonInput):
    return jsonInput['T']

def getDeterminants(l):                

        determinants = []
        for item in l:
            #Crea arreglo con determinantes 
            determinant = item.split('->')[0].split(',')
            #Crea arreglo con determinados
            determinated = item.split('->')[1].split(',')
            #Organiza los determinantes
            determinant = sorted(determinant)
            #Organiza los determinados
            determinated = sorted(determinated)
            
            #Convierte en una cadena de strings los determinantes
            determinantTxt = ",".join(determinant)
            #Convierte en una cadena de strings los determinados
            determinatedTxt = ",".join(determinated)
            
            #Valida si una DF es trivial
            if (determinatedTxt in determinantTxt) or (determinatedTxt == determinantTxt):                        
               print("La DF "+item+" es trivial y se elimina")
            else:
                #Si la DF no es trivial la adiciona al arreglo determinants
                element = { "determinant": determinant, "determinated": determinated}
                determinant_list = element["determinant"]
                if len(determinant_list) > 1:
                    determinant_list = sorted(determinant_list)
                    element['determinant'] = determinant_list
                determinants.append(element)
        determinants = sorted(determinants, key=itemgetter('determinant'))
        
        return determinants

def calculateMinimalCoating(determinants):
        #print(json.dumps(determinants, indent=4, sort_keys=True))
        converted_determinants = []
        for det in determinants:
            if len(det['determinated']) > 1:
                #print('get determinant with len equal to 1')
                splitDeterminantsWithLenGreaterThan1(det, converted_determinants)
            else:
                converted_determinants.append(det)
                
        #print(converted_determinants)
        converted_determinants = sorted(converted_determinants, key=lambda item : len(item['determinant']), reverse=True)
        #print('\n DETERMINANTS STEP 1: \n ', converted_determinants, '\n')
        
        resultStr = 'CALCULANDO RECUBRIMIENTO MINIMO'+'\n\n'+'1. Dependencias elementales:\n'
        resultStr = resultStr +  '\n'.join(str(i) for i in converted_determinants) 
        resultStr = resultStr + '\n\n2. Atributos extraños:\n'

        l2 = []
        attributesCombinations = []
        calculated_determinants = []
        #Find strange objects
        for det in converted_determinants:
            #print(len(det['determinant']))
            #print(det)
            #resultStr = resultStr + str(len(det['determinant']))
            #resultStr = resultStr + '\n'.join(str(i) for i in det)

            if len(det['determinant']) == 1 :
                l2.append(det)
            elif len(det['determinant']) == 2 :                
                
                temp_determinant = []
                contained_determinants = []
                for j in det['determinant']:
                    
                    #print('SEARCH: ',searchBy("elementClosure", calculated_determinants, j))
                    searchResult = searchBy("elementClosure", calculated_determinants, j)
                    if(searchResult):
                       #print("USE CLOSURE: ", searchResult["closure"])
                       closure = searchResult["closure"]
                    else:
                       closure = getClosure([j], converted_determinants.copy())
                    
                    calculated_determinants.append({"elementClosure": j , "closure": closure })
                    contained = (containsIn(det['determinated'], closure) or containsIn(closure, det['determinated']) )
                    #print('CLOSURE ',j,'+: ',closure, ' - CONTAINED: ', contained)
                    resultStr = resultStr + '\n'.join(str(i) for i in closure)
                    if(contained):
                        resultStr = resultStr +  ' - CONTAINED: TRUE\n'
                    else:
                        resultStr = resultStr +  ' - CONTAINED: FALSE\n'
                   
                    contained_determinants.append({"determinant": j, "contained": contained })
		
                searchResult = searchBy("contained", contained_determinants, True)
                if searchResult is not False:
                    #print('There is strange object ', [searchResult['determinant']])
                    temp_determinant = [searchResult['determinant']]
                else:
                    #print('There is not strange object ', det['determinant'])
                    temp_determinant = det['determinant']
			     
                if len(temp_determinant) > 0:
                    l2.append({ "determinant": temp_determinant.copy(), "determinated": det['determinated'] })  
            elif len(det['determinant']) > 2:
                
                #Hallar objecto extraño para determinant de más de 3
                for L in range(0, len(det['determinant'])+1):
                    for subset in itertools.combinations(det['determinant'], L):
                        if len(subset) > 0 and len(subset) < len(det['determinant']):
                            attributesCombinations.append(list(subset))
                #print('\n', attributesCombinations, '\n')
                #resultStr = resultStr + '\n'
                #resultStr = resultStr + ''.join(str(i) for i in attributesCombinations) 

                result = []
                
                for attr in reversed(attributesCombinations):

                    closure = getClosure(attr, converted_determinants.copy())
                    contained = containsIn(det['determinated'], closure)
                    if contained:
                        result = list(set(det['determinant']) - (set(det['determinant']) - set(attr)))
                        break
                    #print(list(set(det['determinant']) - set(attr))) 
                    #resultStr = resultStr + '\n'+list(set(det['determinant']) - set(attr))
                #print(result)
                #resultStr = resultStr + ''.join(str(i) for i in attributesCombinations) 
                l2.append({ "determinant": result, "determinated": det['determinated'] })  
            else:
                l2.append(det);
                        
        #print('\n', 'L2 = \n ', l2, '\n')         
        resultStr = resultStr + '\n' +'\n'.join(str(i) for i in l2)

        l3 = []
        resultStr = resultStr + '\n\n3. Dependencias redundantes:\n'
        temp_determinants = l2.copy()
        
        #Find redundants functional Dedendencies
        for det in l2:
            #print(det)
            #resultStr = resultStr + ''.join(str(i) for i in det)
            temp_determinants.remove(det)
            closure = getClosure(det['determinant'], temp_determinants.copy())
            temp_determinants.append(det)
            contained = (containsIn(det['determinated'], closure) or containsIn(closure, det['determinated']) )
            #print('CLOSURE = ', closure)
            #print('CONTAINED= ', contained)
            resultStr = resultStr + '\n\nCLOSURE = '
            resultStr = resultStr + '\n'.join(str(i) for i in closure)
            if(contained):
                resultStr = resultStr + '\nCONTAINED = TRUE'
            else:
                resultStr = resultStr + '\nCONTAINED = FALSE'


            if not contained:
                l3.append(det)
            else:
                temp_determinants.remove(det)
                
        #print('L3 = ', l3, '\n')
        #outputStr = '\n'.join(str(i) for i in l3)
        resultStr = resultStr + '\n\nL3=\n'+'\n'.join(str(i) for i in l3)
        setOutputToFile(resultStr,'A')

        return l3

def setOutputToFile(datos,mode):
    #with open('output.json', 'w') as file:
    #    json.dump(datos, file)
    if mode == 'A':
        file = open('output.out', 'a')
    else:
        file = open('output.out', 'w')
        
    file.write(datos)
        
def containsIn(valueToVerify, setToVerify):
    for value in valueToVerify:
        if value not in setToVerify:
            return False    
    return True

def belongsFD(determined, closure):
   determinedList = determined.split(',')            
   return containsIn(determinedList, closure)

def getClosure(ct, determinants_temp):
    result = ct
    prev_result = []

    while result != prev_result:
        
        prev_result = result

        for idxt, t in enumerate(prev_result):            
            #determinants_to_check = determinants_temp.copy();
        
            for j in reversed(determinants_temp):

                if t in j['determinant']:

                    if containsIn(j['determinant'], prev_result):
                        result = result + list(set(j['determinated']) - set(result))
                        determinants_temp.remove(j)
                
            #determinants_temp = determinants_to_check    
    return sorted(result)

def getClosureL(attributes, determinants):
    
    attributesCombinations = []
    result_l = []
    strResult = "CALCULANDO CIERRE"+"\n\n"
    strResult = strResult + "Se obtienen las siguientes combinaciones "+"\n"
    for L in range(0, len(attributes)+1):
                for subset in itertools.combinations(attributes, L):
                    if len(subset) > 0:
                        strResult = strResult + ','.join(list(subset)) +"\n"
                        attributesCombinations.append(list(subset))
    strResult = strResult + "\nGenerando L+..." +"\n"
    for ct in attributesCombinations:
        result_l.append({",".join(ct): getClosure(ct, determinants.copy())})
        
    setOutputToFile(strResult,'A')
    return result_l

def searchBy(key, listWhichSearch, valueToSearch):
    for item in listWhichSearch:
        if item[key] == valueToSearch:
            return item
    return False

def splitDeterminantsWithLenGreaterThan1(determinant, dictionaryToInsert):
    
    for det in determinant['determinated']:
        dictionaryToInsert.append({"determinant": determinant['determinant'], "determinated": [det]})

def fCalculateKeys(attributes,determinants):
    #Declare
    determinant= []
    determinated= []
    L3= []
    Z=[]
    W=[]
    V=[]
    M1 =[]
    M2=[]
    resultStr = '\n\nCALCULANDO LLAVES\n\n'
    
    L3 = calculateMinimalCoating(determinants)
    
    #Se identifican y ordenan los determinantes y determinados
    for det in L3:
        if det['determinated'][0] not in determinated:
            determinated.append(det['determinated'][0])
        for d in det['determinant']:
            if d not in determinant:
                determinant.append(d)
    
    #Se calcula Z (resta de implicados)
    for ai in sorted(attributes):
        if ai not in sorted(determinated):
            Z.append(ai)   
            
    zplus = getClosure(Z,L3.copy())
    
    resultStr = resultStr+'Z= '+",".join(Z)+'\n'    
    resultStr = resultStr+'Z+= '+",".join(zplus)+'\n'
    
    #Se evalua si Z+ es una llave candidata
    if zplus == attributes:
        resultStr = resultStr+'Z es llave única \n'
    else:
        #Se calcula W (resta de implicantes)
        for ai in sorted(attributes):
            if ai not in sorted(determinant):
                W.append(ai)   
        resultStr = resultStr+'W= '+",".join(W)+'\n'
        
        #Se calcula V=(Attr-[W U Z+])
        for ai in sorted(attributes):
            if ai not in W+zplus:
                V.append(ai)   
        resultStr = resultStr+'V= '+",".join(V)+'\n'
        
        #Se realiza el producto entre Z y V
        for subset in itertools.product(Z,V):
            M1.append(list(subset))
            if getClosure(list(subset),L3.copy()) == attributes:
                M2.append(list(subset))
        
        #Se realizan los productos subsiguientes
        prevLength = 0
        newM1 = M1.copy()
        while True:
            newM1,newM2 = calculateM2(newM1,L3,attributes,V)
            M2 = M2 + newM2
            if prevLength == len(newM1):
                break
            prevLength = len(newM1)

        resultStr = resultStr + 'M1= \n'
        for m in M1:
            resultStr = resultStr+",".join(m)+'\n'
        resultStr = resultStr + 'M2= \n'
        for m in M2:
            resultStr = resultStr+",".join(m)+'\n'
        
    setOutputToFile(resultStr,'A')
    return resultStr,M2

def calculateM2(M1,L3,attributes,V):
    cM1 = []
    cM2 = []
    async_result = []
    pos = 1
    
    #Cantidad de hilos
    pool = ThreadPool(len(M1)) 
    
    #Lanzamiento de hilos
    for m in M1:
        #newM1,newM2 = productThread(m,pos,V,attributes,L3)
        resultThread = pool.apply_async(productThread,(m,pos,V,attributes,L3))
        async_result.append(resultThread)
        pos = pos + 1
    
    #Recuperacion de resultados
    for result in async_result:
        newM1,newM2 = result.get()
        cM1 = cM1 + newM1
        cM2 = cM2 + newM2
        
    return cM1,cM2

def productThread(m,pos,V,attributes,L3):
    subset_aux = []
    M2 = []
    newM1 =[]
    
    for subset in itertools.product(m[0],V[pos:len(V)]):
        subset_aux = list(subset)
        subset_aux = subset_aux + m[1:len(m)]
        if getClosure(subset_aux,L3.copy()) == attributes:
            M2.append(subset_aux)
        else:
            newM1.append(subset_aux)
    
    return newM1,M2