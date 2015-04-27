#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Parrilla:
    """
    La parrilla asa la carne sobre las brasas.
    """

    def __init__(self, carbon):
        self.carbon = carbon
        self._estado = "apagada"

    def prender(self):
        """
        Enciendo el fuego, si tiene carbón.
        """
        assert self.carbon is not None  # it can raise an AssertionError
        self._estado = "prendida"

    def asar(self, carne):
        """
        Deposita la carne sobre las brasas.
        """
        self._carne = carne

        if self._estado == "prendida":
            self._estado = "asando"
        else:
            raise Exception("Tenés que prender el fuego!")

    def como_estamos(self):
        """
        Imprime el estado de la parrilla.
        """
        print "La parrilla está %s" % self._estado
