class Node:
    def __init__(self, col, val):
        self.col = col # Columna
        self.val = val # Valor
        self.left = None
        self.right = None
        self.parent = None
        self.nivel = None
        self.x = None
        self.y = None

class Tree:
    def __init__(self):
        self.root = None
        self.pre = []
        self.wrong = 0
        self.correct = 0

    def preorden(self, node):
        if node is not None:
            self.pre.append(node)
            self.preorden(node.left)
            self.preorden(node.right)

    def hojas(self):
        return [n for n in self.pre if n.left is None and n.right is None]

    def altura(self, node):
        if node is None:
            return 0
        else:
            return 1 + max(self.altura(node.left), self.altura(node.right))
    
    def test(self, df):
        p = self.root
        for i in range(len(df)):
            while(p.left is not None and p.right is not None):
                if df.iloc[i][p.col] < p.val:
                    p = p.left
                else:
                    p = p.right
            if p.col == df.iloc[i][-1]:
                self.correct += 1
            else:
                self.wrong += 1
            p = self.root
        return self.correct, self.wrong, self.correct/(self.correct+self.wrong)*100
    