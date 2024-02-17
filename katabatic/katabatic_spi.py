# The Model Service Provider Interface (SPI) provides an abstract base class (ABC) for all model adapters to implement.

from abc import ABC, abstractmethod

class KatabaticModelSPI(ABC):

    @abstractmethod
    def load_model(): #Load the model
        pass

    @abstractmethod
    def load_data(): #Load data
        pass

    @abstractmethod
    def fit(self):  #Fit model to data
        pass

    @abstractmethod
    def generate(self): #Generate synthetic data
        pass


#For the Katabatic Metric SPI, the input must be data/a model and the output must be a result.
# Each Evaluation method must be applicable to tabular data.
class KatabaticMetricSPI(ABC):

    @abstractmethod
    def evaluate(): #Load the model
        pass

    @abstractmethod
    def load_data(): #Load data
        pass

    @abstractmethod
    def fit(self):  #Fit model to data
        pass

    @abstractmethod
    def generate(self): #Generate synthetic data
        pass

        
    