"""
############################################################
Quarto - Tabuleiro
############################################################

:Author: *Carlo E. T. Oliveira*
:Author: *Kyle Kuo*
:Contact: carlo@nce.ufrj.br
:Date: 2013/04/02
:Status: This is a "work in progress"
:Revision: 0.1.0
:Home: `Labase <http://labase.selfip.org/>`__
:Copyright: 2013, `GPL <http://is.gd/3Udt>`__.
"""
class Casa(object):
    pass
class Tabuleiro(object):
    def __init__(self):
        self.casas = []
    
    def cria(self):
        self.casas = [Casa() for i in range(16)]
    
    pass
