import pandas as pd
from Tree import Tree, Node
class arbol_kd:
    def __init__(self):
        self.arbol = Tree()
        self.df = pd.read_csv('heart_clas.csv')
        cols = list(self.df)[0:-1]
        self.gen_tree(self.df, cols[0], arbol=self.arbol)
        self.r = self.arbol.root
        self.arbol.preorden(self.r)

    def verifylist(self, l):  # Verifica si todos los elementos de la lista son iguales
        return all(x == l[0] for x in l)

    def splitlist(self, l):   # Divide la lista en dos partes iguales o similares
        m = int(len(l)/2)-1
        n = l[m]
        if self.verifylist(l):
            return True
        if l[m] == l[m+1]:  # Si hay dos elementos iguales en el medio, divide la lista lo más balanceado posible
            i1 = l.index(n)
            i2 = l[::-1].index(n)
            if m+1-i1 < m+1-i2:
                m = i1-1
            else:
                m = len(l)-i2-1
        return m+1

    def gen_tree(self, df, col, parent=None, side=None, arbol=None):
        df = df.sort_values(by=[col])  # Ordena el dataframe por la columna
        lista = list(df[col])
        cols = list(df)[0:-1]
        cla = list(df)[-1]  # Clasificación
        m = self.splitlist(lista)  # Indice de la division
        i = (cols.index(col)+1)%len(cols) # Indice de la siguiente columna
        if m is True:
            self.gen_tree(df, cols[i], parent, side, arbol)
            return
        t1 = df.iloc[:m]  # Dataframe de la izquierda
        t2 = df.iloc[m:]  # Dataframe de la derecha
        s1 = list(t1[cla]) # Lista de clasificaciones de la izquierda
        s2 = list(t2[cla]) # Lista de clasificaciones de la derecha
        num = round((t1.iloc[-1][col]+t2.iloc[0][col])/2, 3) # Valor donde se dividen las filas
        nodo = Node(col,num) # Nodo que se va a insertar
        if arbol.root is None: # Si el arbol esta vacio, el nodo se inserta como raiz
            arbol.root = nodo
            nodo.nivel = 1
        else:                  # Si no, se inserta como hijo del nodo padre
            nodo.parent = parent
            if side == 'left':
                parent.left = nodo
                nodo.nivel = parent.nivel+1
            else:
                parent.right = nodo
                nodo.nivel = parent.nivel+1
        if(self.verifylist(s1)): # Si la lista de clasificaciones es homogenea, se inserta como hoja
            nodo.left = Node(s1[0], None)
            nodo.left.nivel = nodo.nivel+1
            nodo.left.parent = nodo
        if(self.verifylist(s2)): # Si la lista de clasificaciones es homogenea, se inserta como hoja
            nodo.right = Node(s2[0], None)
            nodo.right.nivel = nodo.nivel+1
            nodo.right.parent = nodo
        if not self.verifylist(s1) and len(t1) > 1: # Si la lista de clasificaciones no es homogenea y el dataframe no es de una fila, se genera un subarbol
            self.gen_tree(t1, cols[i], nodo, 'left', arbol)
        if not self.verifylist(s2) and len(t2) > 1: # Si la lista de clasificaciones no es homogenea y el dataframe no es de una fila, se genera un subarbol
            self.gen_tree(t2, cols[i], nodo, 'right', arbol)

    def rules(self, leafs): # Reglas de clasificacion
        rules = []
        for l in leafs:
            p = l.parent
            rule = []
            while p.parent is not None:
                rule.append(p.col+'<'+str(p.val))
                p = p.parent
            rules.append(' && '.join(rule)+' => '+str(l.col))
        return rules
    
    def classify_row(self, row):
        p = self.r
        while(p.left is not None and p.right is not None):
            if row[p.col] < p.val:
                p = p.left
            else:
                p = p.right
        return p.col
