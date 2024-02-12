from random import randint, uniform, random
import time

class Pila:
    def __init__(self):
        self.items = []

    def PilaVacia(self):
        return self.items == []

    def Push(self, item):
        self.items.append(item)

    def Pop(self):
        return self.items.pop()
    def Verificar(self):
        return self.items(len(self.items)-1)

    def tamano(self):
        return len(self.items)

    def TLlegada(self):
        Tiempo = randint(0,3)
        return Tiempo

    def TAtn(self):
        Tiempo = randint(0,5)
        return Tiempo

    def Cual(self):
        return randint(1,2)

if __name__ == "__main__":

    P=Pila()
    Objeto = 1

    while True:


        if P.Cual()==1 :
            time.sleep(P.TLlegada())
            P.Push(Objeto)
            Objeto=Objeto+1
        else:
            if P.PilaVacia():
               P.Push(Objeto)
               Objeto=Objeto+1
               time.sleep(P.TLlegada())
            else:    
                P.Pop()
                Objeto=Objeto+1
            print(P.items)                         
   
