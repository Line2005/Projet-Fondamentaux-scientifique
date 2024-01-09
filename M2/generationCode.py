

#################################################################
##         Creation des fonction d'allumage des LEDs           ##
#################################################################


def UneLEDsurdeux():
    fichier=open("genere-code\param.py","w")
    fichier.write("void setup(){\npinMode(4, OUTPUT);\npinMode(5, OUTPUT);\npinMode(6, OUTPUT);\npinMode(11, OUTPUT);\npinMode(10, OUTPUT);\npinMode(9, OUTPUT);\npinMode(8, OUTPUT);\npinMode(7, OUTPUT);\npinMode(2, OUTPUT);\npinMode(3, OUTPUT);\n}\nvoid loop(){\ndigitalWrite(2, HIGH);\ndelay(500);\ndigitalWrite(2, LOW);\ndigitalWrite(4, HIGH);\ndelay(500);\ndigitalWrite(4, LOW);\ndigitalWrite(6, HIGH);\ndelay(500);\ndigitalWrite(6, LOW);\ndigitalWrite(8, HIGH);\ndelay(500);\ndigitalWrite(8, LOW);\ndigitalWrite(10, HIGH);\ndelay(500);\ndigitalWrite(10, LOW);\ndigitalWrite(3, HIGH);\ndelay(500);\ndigitalWrite(3, LOW);\ndigitalWrite(5, HIGH);\ndelay(500);\ndigitalWrite(5, LOW);\ndigitalWrite(7, HIGH);\ndelay(500);\ndigitalWrite(7, LOW);\ndigitalWrite(9, HIGH);\ndelay(500);\ndigitalWrite(9, LOW);\ndigitalWrite(11, HIGH);\ndelay(500);\ndigitalWrite(11,LOW);\n}")
    fichier.close()

def UneLEDsurtrois():
    fichier=open("genere-code\param.py","w")
    fichier.write("void setup(){\npinMode(4, OUTPUT);\npinMode(5, OUTPUT);\npinMode(6, OUTPUT);\npinMode(11, OUTPUT);\npinMode(10, OUTPUT);\npinMode(9, OUTPUT);\npinMode(8, OUTPUT);\npinMode(7, OUTPUT);\npinMode(2, OUTPUT);\npinMode(3, OUTPUT);\n}\nvoid loop(){\ndigitalWrite(2, HIGH);\ndelay(500);\ndigitalWrite(2, LOW);\ndigitalWrite(5, HIGH);\ndelay(500);\ndigitalWrite(5, LOW);\ndigitalWrite(8, HIGH);\ndelay(500);\ndigitalWrite(8, LOW);\ndigitalWrite(11, HIGH);\ndelay(500);\ndigitalWrite(11, LOW);\ndigitalWrite(4, HIGH);\ndelay(500);\ndigitalWrite(4, LOW);\ndigitalWrite(7, HIGH);\ndelay(500);\ndigitalWrite(7, LOW);\ndigitalWrite(10, HIGH);\ndelay(500);\ndigitalWrite(10, LOW);\ndigitalWrite(3, HIGH);\ndelay(500);\ndigitalWrite(3, LOW);\ndigitalWrite(6, HIGH);\ndelay(500);\ndigitalWrite(6, LOW);\ndigitalWrite(9, HIGH);\ndelay(500);\ndigitalWrite(9,LOW);\n}")
    fichier.close()
    
def Modechenille():
    fichier=open("genere-code\param.py","w")
    fichier.write("void setup(){\npinMode(4, OUTPUT);\npinMode(5, OUTPUT);\npinMode(6, OUTPUT);\npinMode(11, OUTPUT);\npinMode(10, OUTPUT);\npinMode(9, OUTPUT);\npinMode(8, OUTPUT);\npinMode(7, OUTPUT);\npinMode(2, OUTPUT);\npinMode(3, OUTPUT);\n}\nvoid loop(){\ndigitalWrite(2, HIGH);\ndelay(200);\ndigitalWrite(2, LOW);\ndigitalWrite(3, HIGH);\ndelay(200);\ndigitalWrite(3, LOW);\ndigitalWrite(4, HIGH);\ndelay(200);\ndigitalWrite(4, LOW);\ndigitalWrite(5, HIGH);\ndelay(200);\ndigitalWrite(5, LOW);\ndigitalWrite(6, HIGH);\ndelay(200);\ndigitalWrite(6, LOW);\ndigitalWrite(7, HIGH);\ndelay(200);\ndigitalWrite(7, LOW);\ndigitalWrite(8, HIGH);\ndelay(200);\ndigitalWrite(8, LOW);\ndigitalWrite(9, HIGH);\ndelay(200);\ndigitalWrite(9, LOW);\ndigitalWrite(10, HIGH);\ndelay(200);\ndigitalWrite(10, LOW);\ndigitalWrite(11, HIGH);\ndelay(200);\ndigitalWrite(11,LOW);\n}")
    fichier.close()
    
def Modetransition():
    fichier=open("genere-code\param.py","w")
    fichier.write("void setup(){pinMode(4, OUTPUT);\npinMode(5, OUTPUT);\npinMode(6, OUTPUT);\npinMode(11, OUTPUT);\npinMode(10, OUTPUT);\npinMode(9, OUTPUT);\npinMode(8, OUTPUT);\npinMode(7, OUTPUT);\npinMode(2, OUTPUT);\npinMode(3, OUTPUT);\n}\nvoid loop(){\ndigitalWrite(2, HIGH);\ndelay(500); \ndigitalWrite(3, HIGH);\ndelay(500);\ndigitalWrite(2, LOW);\ndelay(500); \ndigitalWrite(4, HIGH);\ndelay(500);\ndigitalWrite(3, LOW);\ndelay(500); \ndigitalWrite(5, HIGH);\ndelay(500); \ndigitalWrite(4, LOW);\ndelay(500); \ndigitalWrite(6, HIGH);\ndelay(500); \ndigitalWrite(5, LOW);\ndelay(500); \ndigitalWrite(7, HIGH);\ndelay(500); \ndigitalWrite(6, LOW);\ndelay(500); \ndigitalWrite(8, HIGH); \ndelay(500); \ndigitalWrite(7, LOW);\ndelay(500); \ndigitalWrite(9, HIGH);\ndelay(500); \ndigitalWrite(8, LOW);\ndelay(500); \ndigitalWrite(10, HIGH);\ndelay(500); \ndigitalWrite(9, LOW);\ndelay(500); \ndigitalWrite(11, HIGH);\ndelay(500); \ndigitalWrite(10, LOW);\ndelay(500);\ndigitalWrite(2,HIGH);\ndelay(500);\ndigitalWrite(11,LOW);\n}")
    fichier.close()


#################################################################
##     Creation des fonction d'allumage de la LED au choix     ##
#################################################################


def LEDune():
    fichier=open("genere-code\param.py","w")
    fichier.write("void setup(){\npinMode(2,OUTPUT);\n}\nvoid loop(){\ndigitalWrite(2,HIGH);\n}")
    fichier.close()
    
def LEDdeux():
    fichier=open("genere-code\param.py","w")
    fichier.write("void setup(){\npinMode(3,OUTPUT);\n}\nvoid loop(){\ndigitalWrite(3,HIGH);\n}")
    fichier.close()
    
def LEDtrois():
    fichier=open("genere-code\param.py","w")
    fichier.write("void setup(){\npinMode(4,OUTPUT);\n}\nvoid loop(){\ndigitalWrite(4,HIGH);\n}")
    fichier.close()
    
def LEDquatre():
    fichier=open("genere-code\param.py","w")
    fichier.write("void setup(){\npinMode(5,OUTPUT);\n}\nvoid loop(){\ndigitalWrite(5,HIGH);\n}")
    fichier.close()
    
def LEDcinq():
    fichier=open("genere-code\param.py","w")
    fichier.write("void setup(){\npinMode(6,OUTPUT);\n}\nvoid loop(){\ndigitalWrite(6,HIGH);\n}")
    fichier.close()
    
def LEDsix():
    fichier=open("genere-code\param.py","w")
    fichier.write("void setup(){\npinMode(7,OUTPUT);\n}\nvoid loop(){\ndigitalWrite(7,HIGH);\n}")
    fichier.close()
    
def LEDsept():
    fichier=open("genere-code\param.py","w")
    fichier.write("void setup(){\npinMode(8,OUTPUT);\n}\nvoid loop(){\ndigitalWrite(8,HIGH);\n}")
    fichier.close()
    
def LEDhuit():
    fichier=open("genere-code\param.py","w")
    fichier.write("void setup(){\npinMode(9,OUTPUT);\n}\nvoid loop(){\ndigitalWrite(9,HIGH);\n}")
    fichier.close()
    
def LEDneuf():
    fichier=open("genere-code\param.py","w")
    fichier.write("void setup(){\npinMode(10,OUTPUT);\n}\nvoid loop(){\ndigitalWrite(10,HIGH);\n}")
    fichier.close()
    
def LEDdix():
    fichier=open("genere-code\param.py","w")
    fichier.write("void setup(){\npinMode(11,OUTPUT);\n}\nvoid loop(){\ndigitalWrite(11,HIGH);\n}")
    fichier.close()
