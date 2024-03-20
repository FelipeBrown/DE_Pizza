
class Pizza():
    ingredientes_carne = ['pollo', 'vacuno', 'carne vegetal']
    ingredientes_vegetales = ['tomate', 'aceitunas', 'champiñones']
    tipos_masa = ['tradicional', 'delgada']

    @staticmethod
    def validar_elemento(elemento, valores_posibles):
        return elemento in valores_posibles

    def __init__(self):
        self.ingrediente_proteico = None
        self.primer_ingrediente_vegetal = None
        self.segundo_ingrediente_vegetal = None
        self.tipo_masa = None
        self.es_valida = False

    def hacer_pedido(self):
        self.ingrediente_proteico = input("Ingrese el ingrediente proteico (pollo, vacuno, carne vegetal): ")
        self.primer_ingrediente_vegetal = input("Ingrese el primer ingrediente vegetal (tomate, aceitunas, champiñones): ")
        self.segundo_ingrediente_vegetal = input("Ingrese el segundo ingrediente vegetal (tomate, aceitunas, champiñones): ")
        self.tipo_masa = input("Ingrese el tipo de masa (tradicional, delgada): ")

        self.es_valida = self.validar_pedido()

    def validar_pedido(self):
        ingredientes_validos = (
            self.validar_elemento(self.ingrediente_proteico, self.ingredientes_carne) and
            self.validar_elemento(self.primer_ingrediente_vegetal, self.ingredientes_vegetales) and
            self.validar_elemento(self.segundo_ingrediente_vegetal, self.ingredientes_vegetales) and
            self.validar_elemento(self.tipo_masa, self.tipos_masa)
        )
        return ingredientes_validos
    