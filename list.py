
class nodes:
    def __init__(self,value):
        self.value=value
        self.nexts=None
    def __repr__ (self,values):
        if self.nexts!=None:
            values=values+self.value+"\n"
            self.nexts.__repr__(values)
            
        return values

    def report(self):
        ttrue=True
        back=self.nexts
        
        while ttrue:
            
            if back!=None:
                
                print(back.value)
                back=back.nexts
            else:
                ttrue=False
            
           
tree=nodes("list")
back=tree
for a in range(16):
    back.nexts=nodes("item "+str(a))
    back= back.nexts

tree.report()
