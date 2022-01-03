def group_by_owners(files):
    diccionario = {}
    contador = 0
    claves = list(files.keys())
    for i in files.values():
        diccionario[i] = list() #claves[contador]
    for i in files.values():
        diccionario[i].append(claves[contador])
        contador += 1

    return diccionario

if __name__ == "__main__":    
    files = {
        'Input.txt': 'Randy',
        'Code.py': 'Stan',
        'Output.txt': 'Randy'
    }   
    print(group_by_owners(files))