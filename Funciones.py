import json
import itertools
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
        resultStr = ''
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
        resultStr = resultStr + '\n'
        resultStr = resultStr + '\n'.join(str(i) for i in converted_determinants) 

        l2 = []
        attributesCombinations = []
        calculated_determinants = []
        #Find strange objects
        for det in converted_determinants:
            #print(len(det['determinant']))
            #print(det)
            resultStr = resultStr + str(len(det['determinant']))
            resultStr = resultStr + '\n'.join(str(i) for i in det)

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
                        resultStr = resultStr +  ' - CONTAINED: TRUE'
                    else:
                        resultStr = resultStr +  ' - CONTAINED: FALSE'
                   
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
                resultStr = resultStr + '\n'
                resultStr = resultStr + ''.join(str(i) for i in attributesCombinations) 

                result = []
                
                for attr in reversed(attributesCombinations):

                    closure = getClosure(attr, converted_determinants.copy())
                    contained = containsIn(det['determinated'], closure)
                    if contained:
                        result = list(set(det['determinant']) - (set(det['determinant']) - set(attr)))
                        break
                    #print(list(set(det['determinant']) - set(attr))) 
                    resultStr = resultStr + '\n'+list(set(det['determinant']) - set(attr))
                #print(result)
                resultStr = resultStr + ''.join(str(i) for i in attributesCombinations) 
                l2.append({ "determinant": result, "determinated": det['determinated'] })  
            else:
                l2.append(det);
                        
        #print('\n', 'L2 = \n ', l2, '\n')         
        resultStr = resultStr + '\n'
        resultStr = resultStr + '\n'.join(str(i) for i in l2)

        l3 = []
        
        temp_determinants = l2.copy()
        
        #Find redundants functional Dedendencies
        for det in l2:
            #print(det)
            resultStr = resultStr + ''.join(str(i) for i in det)
            temp_determinants.remove(det)
            closure = getClosure(det['determinant'], temp_determinants.copy())
            temp_determinants.append(det)
            contained = (containsIn(det['determinated'], closure) or containsIn(closure, det['determinated']) )
            #print('CLOSURE = ', closure)
            #print('CONTAINED= ', contained)
            resultStr = resultStr + '\nCLOSURE = '
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
        outputStr = '\n'.join(str(i) for i in l3)
        resultStr = resultStr + '\n'.join(str(i) for i in l3)
        setOutputToFile(resultStr)

        #return outputStr
        return l3

def setOutputToFile(datos):
    with open('output.json', 'w') as file:
        json.dump(datos, file)
        
def containsIn(valueToVerify, setToVerify):
    for value in valueToVerify:
        if value not in setToVerify:
            return False    
    return True

def belongsFD(fD, closure):
    
   determinated = fD.split('->')[1].split(',')
        
   return containsIn(determinated, closure)

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
            
    for L in range(0, len(attributes)+1):
                for subset in itertools.combinations(attributes, L):
                    if len(subset) > 0:
                        attributesCombinations.append(list(subset))
    #print('Generando L+...')
    for ct in attributesCombinations:
        result_l.append({",".join(ct): getClosure(ct, determinants.copy())})
        
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
    L3 = []
    determinant = []
    determinated= []
    Z = []
    resultStr = ''
    L3 = calculateMinimalCoating(determinants)
    
    #Se identifican y ordenan los determinantes y determinados
    for det in L3:
        if det['determinated'] not in determinated:
            determinated.append(det['determinated'][0])
        if det['determinant'] not in determinant:
            determinant.append(det['determinant'][0])
    
    #Se calcula Z
    for ai in sorted(attributes):
        if ai not in sorted(determinated):
            Z.append(ai)   
            
    zplus = getClosure(Z,L3.copy())
    
    #print('L3= ',L3)
    resultStr = resultStr+'Z= '+",".join(Z)+'\n'    
    resultStr = resultStr+'Z+= '+",".join(zplus)+'\n'
    
    #Se evalua si Z+ es una llave candidata
    
    
    setOutputToFile(resultStr)
    return resultStr