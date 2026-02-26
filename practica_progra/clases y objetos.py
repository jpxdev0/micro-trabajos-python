class celular:
    def __init__(self,marca,modelo,camara):
        # el init es un metodo constructor de instancia, por que se lo pasan cuando creas un objeto de la clase, y se lo utiliza para inicializar las propiedades del objeto, osea para asignar valores a las propiedades del objeto
        # el self es como autoproclmar el nombre del objeto ejemplo:
        # primero se crea la propiedad de self que seria  self.marca(ejemplo) 
        #y luego se le asigna el valor marca que es el parametro que se le da a la funcion init
        # osea para entender mejor el self.marca es una propiedad de self y el otro marca es el parametro que se asigna entre los parentecis del init
        self.marca = marca
        self.modelo = modelo
        self.camara = camara 

    
celular1 = celular("samsung","a12","48mp")
#al momento de poner celular1 = celular, al momento de poner celular invocamos al constructor(init) de la clase celular
# y al momento de poner entre los parentesis los parametros que se le asignan a la funcion init, se le asignan a las propiedades de self
celular2 = celular("iphone","14","48mp")
print(celular1.camara)
print(celular2.camara)
