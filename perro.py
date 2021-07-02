class Perro:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def sit(self):
        print(f'{self.name} esta sentado')
    def roll_over(self):
        print(f'{self.name} se volteo')
    def get_info(self):
        print(f"{self.name} es mi nombre" f"{self.age} es mi edad")
    
mi_perro= Perro("Mimi",10)
x=0
while x==0:
    print("Que quieres hacer?")
    hacer=input()
    if hacer == "voltear":
        mi_perro.roll_over()
    if hacer == "sentar":
        mi_perro.sit()
    if hacer == "info":
        mi_perro.get_info()

