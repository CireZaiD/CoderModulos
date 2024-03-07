class Ciclista:
    def __init__(self, estilo):
        self.estilo = estilo

    def hacer_bici(self):
        return 'Estoy armando la bici'

    def __str__(self):
        return f'soy un ciclista del estilo {self.estilo}'