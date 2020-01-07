import math;

def fuelForEachModuloParte2(masa):
    fuel=masa//3-2    
    if (fuel<=0):
        return 0
    else:
        return fuel+fuelForEachModuloParte2(fuel)

def fuelForEachModuloParte1(masa):
    fuel=masa//3-2    
    return fuel

def calcularFuel():
    stream = open('masa.csv','r')
    fuelParte1=0
    fuelParte2=0
    for modulo in stream.readlines():
        fuelParte1+= fuelForEachModuloParte1(int(modulo))
        fuelParte2+= fuelForEachModuloParte2(int(modulo))
    stream.close()
    writeResultsIntoFile('parte1.txt',fuelParte1)
    writeResultsIntoFile('parte2.txt',fuelParte2)

def writeResultsIntoFile(fileName,results):
    archivoResultado=open (fileName,'w')
    archivoResultado.write(str(results))
    archivoResultado.close()

calcularFuel()
