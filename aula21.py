# Classes abstratas - Abstract Base Class (abc)
# ABCs são usadas como contratos para a definição
# de novas classes. Elas podem forçar outras classes
# a criarem métodos concretos. Também podem ter
# métodos concretos por elas mesmas.
# @abstractmethods são métodos que não tem corpo.
# As regras para classes abstratas com métodos
# abstratos é que elas não podem ser instanciadas diretamente.
# métodos abstratos devem ser implementados nas sublcasses (@abstractmethod).
# Uma classe abstgrata em Python tem sua metaclasse
# sendo ABCMeta.
# É possivel criar @property @setter @classmethod
# @staticmethod e @method como abstratos, para isso
# use @abstractmethod como decorator mais interno.

from abc import ABC, abstractclassmethod

class Log(ABC):
    @abstractclassmethod
    def _log(self, msg): ...

    def log_error(self, msg):
        return self._log(f'Error: {msg}')
    
    def log_sucess(self, msg):
        return self._log(f'Sucess: {msg}')
    

class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__})')


l = LogPrintMixin()
l.log_error('Oi')