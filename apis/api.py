from dataclasses import dataclass
from abc import ABC, abstractmethod

class Api(ABC):
    '''Represents a generic api'''

    @abstractmethod
    def get_first_registered_candle():
        """
        Find the first day the pair traded,
        useful later when parsing all of the data, 
        as a start date.
        """

    @abstractmethod
    def make_request(self, url, verb='get', code=200, params=None, data=None, headers=None, save_filename="" ):
        """ """