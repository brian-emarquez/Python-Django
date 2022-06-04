class Input:
    """
    Autor: Suling Vera
    Fecha de creación: 2021
    Fecha de modificación:2022 
    Descripción:
    01 - Create class
    """

    def __init__(self, txid, vout):
        self.data = {
            "txid": txid,
            "vout": vout
        }

    def __str__(obj):
        return '{}'.format(
            obj.data
        )


class Transaction:
    """
    Autor: Suling Vera
    Fecha de creación: 2021
    Fecha de modificación:2022 
    Descripción:
    01 - Create class
    """

    def __init__(self, inputs, outputs):
        self.inputs = []
        self.outputs = []

    def __str__(obj):
        return '{} - {}'.format(
            obj.inputs.__str__(),
            obj.outputs
        )

    def format(self):
        return self
