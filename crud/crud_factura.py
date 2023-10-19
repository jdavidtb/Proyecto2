from model.factura import Factura
from datetime import datetime
class CRUDFactura:
    _facturas = []

    @classmethod
    def create_factura(cls, fecha_str, valor_total, id_factura, cedula):
        fecha = datetime.strptime(fecha_str, '%Y-%m-%d')
        nueva_factura = Factura(fecha, valor_total, id_factura, cedula)
        cls._facturas.append(nueva_factura)
        return nueva_factura

    @classmethod
    def read_factura(cls, id_factura):
        for factura in cls._facturas:
            if factura.id_factura == id_factura:
                return factura
        return None

    @classmethod
    def update_factura(cls, id_factura, nuevo_valor_total=None, nueva_fecha=None):
        factura = cls.read_factura(id_factura)
        if factura:
            if nuevo_valor_total:
                factura.valor_total = nuevo_valor_total
            if nueva_fecha:
                factura.fecha = nueva_fecha
            return True
        return False

    @classmethod
    def delete_factura(cls, id_factura):
        factura = cls.read_factura(id_factura)
        if factura:
            cls._facturas.remove(factura)
            return True
        return False

