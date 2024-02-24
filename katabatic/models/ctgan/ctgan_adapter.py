from katabatic_spi import KatabaticModelSPI
import pandas as pd
import sdv
from sdv.single_table import CTGANSynthesizer
from sdv.metadata import SingleTableMetadata



# class CtganAdapter(KatabaticModelSPI):
    
#     def load_model(self):
#         self.model = CTGAN() # Initialise and return an instance of the model
#         self.training_sample_size = 0
#         return self.model

#     #TODO: add exception handling to load()
#     def load_data(self, data_pathname):
#         data = pd.DataFrame
#         print("Loading Data...")
#         return data
    
#     #TODO: add exception handling to fit()
#     def fit(self, X_train, y_train, k=0, epochs=10, batch_size=64):   #TODO: remove hard coded numbers
#         self.model.fit(X_train, y_train, k, batch_size=batch_size, epochs=epochs) # TODO: train self.model on the input data
#         self.training_sample_size = X_train.len()
#         return   # Don't need to return anything. 

#     #TODO: add exception handling to generate()
#     def generate(self, size=None):  #Modify so that if size is not specified, default is the training sample size.
        
#         if size==None: 
#             size = self.training_sample_size
#         generated_data = self.model.sample(size)
#         return generated_data
    
class CtganAdapter(KatabaticModelSPI):

    def __init__(self, type='continuous'):
        self.type = None  # Should be either 'discrete' or 'continuous'
        self.constraints = None 
        self.batch_size = None
        self.epochs = None
        self.data = None

    def load_model(self): #Load the model
        metadata = SingleTableMetadata()

        metadata.detect_from_dataframe(self.data)
        self.model = CTGANSynthesizer(metadata)  # Initialise and return an instance of the model
        print("Loading the model")
        return

    def load_data(self, data): #Load data
        self.data = data

    def fit(self, X_train, y_train, k=0, epochs=10, batch_size=64):  #Fit model to data
        self.model.fit(self.data)
        print("Fitting the model")
        return

    def generate(self): #Generate synthetic data
        print("Generating some data")
        return