from .hp_object import *
from .module_loader import *
from  .module_plotter  import *
from  .module_simulator import *
from  .module_varied import *

class Hidr_Manager:
    def __init__(self, caminho_arq:str ):
        self.Arquivo_Base =  loader.load(caminho_arq)
        self.df = cleaner.clean(self.Arquivo_Base)
