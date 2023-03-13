import random
class Algoritmos:
    def __init__(self):
        self.myList = []
        random.seed(2023)
        for i in range(10):
            num = random.randrange(100)
            self.myList.append(num)
        print(self.myList)
        print("Seleccione que tipo de algoritmo quiere realizar")
        print(" 1: Burbuja menor \n 2: Burbuja mayor \n 3: Burbuja señal \n 4: Shaker sort "
              "\n 5: Insercion directa \n 6: Insercion binaria \n 7: Selección Directa \n 8: Selección Directa"
              "\n 9: QuickSort Recursivo")
        opcion = input()
        self.Ejecuta(opcion)

    def Ejecuta(self, op):
        if op == '1':
            print(self.BurbujaMenor(self.myList))
        if op == '2':
            print(self.BurbujaMayor(self.myList))
        if op == '3':
            print(self.BurbujaSenal(self.myList))
        if op == '4':
            print(self.ShakerSort(self.myList))
        if op == '5':
            print(self.Insercion(self.myList))
        if op == '6':
            print(self.InsercionBinaria(self.myList))
        if op == '7':
            print(self.Seleccion(self.myList))
        if op == '8':
            print(self.Shell(self.myList))
        if op == '9':
          self.QuicksortRecursivo(self.myList)9

 #Transporta el elemento más pequeño hacia la parte izquierda del arreglo
    def BurbujaMenor(self, lista):
        n = len(lista)
        for i in range(n):

            for j in range(1, n-i):
                if lista[j - 1] > lista[j]:
                    aux = lista[j-1]
                    lista[j - 1] = lista[j]
                    lista[j] = aux
        return lista

  # Transporta el elemento más grande hacia la parte derecha del arreglo
    def BurbujaMayor(self, lista):
        n=len(lista)
        for i in range(n):
            for j in range(0, n-1-i):
                if lista[j] > lista[j+1]:
                    aux = lista[j]
                    lista[j] = lista[j+1]
                    lista[j+1] = aux
        return lista

    #IDEA CENTRAL: USAR UNA MARCA O SEÑAL PARA INDICAR QUE NO SE HA PRODUCIDO
    #NINGUN INTERCAMBIO EN UNA PASADA
    def BurbujaSenal(self, lista):
        n=len(lista)
        i = 1
        band = False
        while i <= n-1 and band is False:
            band= True
            for j in range(n-1):
                if lista[j] > lista[j+1]:
                    aux = lista[j]
                    lista[j] = lista[j + 1]
                    lista[j + 1] = aux
                    band = False
            i = i+1
        return lista

    #LA ORDENACIÓN SHAKERSORT ES LA OPTIMIZACIÓN DEL METODO DIRECTO: CADA ETAPA TIENE 2 PASADAS
    # EN LA PRIMERA ETAPA, DE DERECHA A IZQUIERDA SE TRASLADAN LOS ELEMENTOS MÁS PEQUEÑPS
    #EN LA SEGUNDA ETAPA DE IZQUIERDA A DERECHA SE TRASLADAN LOS ELEMENTOS MÁS GRANDES
    #EN CADA ETAPA SE VA ALMACENANDO LA POSICIÓN DEL ELEMENTO INTERCAMBIADO
    def ShakerSort(self, lista):

        n = len(lista)

        k = n
        IZQ = 0
        DER = n-1
        while DER >= IZQ:
            for i in range(DER,IZQ, -1):
                if lista[i-1]>lista[i]:
                    aux= lista[i-1]
                    lista[i-1]=lista[i]
                    lista[i]=aux
                    k = i
            IZQ= k
            for i in range(IZQ, DER+1, 1):
                if lista[i-1] > lista[i]:
                    aux= lista[i-1]
                    lista[i-1]=lista[i]
                    lista[i]=aux
                    k = i
            DER = k-1
        return lista
    #METODO DE ORDENACIÓN POR INSERCIÓN DIRECTA O MÉTODO DE LA BARAJA:
    def Insercion(self, lista):
        n = len(lista)
        for i in range(1, n):
            aux = lista[i]
            k = i - 1
            while k >= 0 and aux < lista[k]:
                lista[k+1] = lista[k]
                k = k - 1
            lista[k + 1] = aux
        return lista
    # METODO DE ORDENACIÓN POR INSERCIÓN BINARIA:
    def InsercionBinaria(self, lista):
        n = len( lista)
        for i in range(1, n):
            aux = lista[i]
            IZQ = 0
            DER = i-1
            while IZQ <= DER:
                M = (IZQ + DER)//2
                if aux <= lista[M]:
                    DER = M - 1
                else:
                    IZQ = M + 1
            j = i - 1
            while j >= IZQ :
                lista[j+1] = lista[j]
                j = j - 1
            lista[IZQ] = aux
        return lista
    #METODO DE ORDENACIÓN POR SELECCION DIRECTA:
    def Seleccion(self, lista):
        n = len(lista)
        for i in range(0, n):
            menor = lista[i]
            k = i
            for j in range(i+1 , n):
                if lista[j] < menor:
                    menor = lista[j]
                    k = j
            lista[k] = lista[i]
            lista[i] = menor
        return lista
    def Shell(self, lista):
        n = len(lista)
        INT = n + 1
        while INT > 1:
            INT = INT // 2
            BAND = True
            while BAND == True:
                BAND = False
                i=0
                while i + INT < n:
                    if lista[i] > lista[i+INT]:
                        aux = lista[i]
                        lista[i] = lista[i+INT]
                        lista[i+INT] = aux
                        BAND = True
                    i = i + 1
        return lista
    #METODO QUICKSORT: METÓDO MÁS EFICIENTE Y VELOS DE OREDNACIÓN INTERNA
    #...METODO QUICKSORT EN VERSIÓN RECURSIVA
    def QuicksortRecursivo(self, nums):
        n = len(nums)
        myList=self.ReduceRecursivo(0, n-1, nums)
        print(myList)

    def ReduceRecursivo(self, INI , FIN ,list):
        IZQ = INI
        DER = FIN
        POS = INI
        BAND = True
        while BAND == True:
            BAND = False
            while list[POS] <= list[DER] and POS != DER:
                DER = DER - 1
            if POS != DER:
                AUX = list[POS]
                list[POS] = list[DER]
                list[DER] = AUX
                POS = DER
                while list[POS] >= list[IZQ] and POS != IZQ :
                    IZQ = IZQ + 1
                if POS != IZQ:
                    BAND = True
                    AUX = list[POS]
                    list[POS] = list[IZQ]
                    list[IZQ] = AUX
                    POS = IZQ
        if POS - 1 > INI:
            self.ReduceRecursivo(INI, POS-1, list)

        if FIN > POS + 1:
            self.ReduceRecursivo(POS+1, FIN, list)
        return list








object = Algoritmos()
