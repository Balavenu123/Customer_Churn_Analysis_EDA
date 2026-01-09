import sys
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
from log_code import setup_logging
logger = setup_logging('main')
from ploting import PLOT

class EDA:
    def __init__(self,path):
        try:
            self.path = path
            self.df = pd.read_csv(self.path)
            # Display the data
            logger.info(f'Data Set :\n{self.df}')
            # shape of the data
            logger.info(f'Data Set shape :\n{self.df.shape}')
            # Checking null values
            logger.info(f'Data Set null values :\n{self.df.isnull().sum()}')
            # value count in gender
            logger.info(f'value counts in gender :\n{self.df['gender'].value_counts()}')
            # SeniorCitizen value count
            logger.info(f'value counts in senior citizen :\n{self.df['SeniorCitizen'].value_counts()}')
            # value count in InternetService
            logger.info(f'value counts in Internetservice :\n{self.df['InternetService'].value_counts()}')
            # value count in paymentmethod
            logger.info(f'value counts in paymentmethod :\n{self.df['PaymentMethod'].value_counts()}')
            # value count in sim
            logger.info(f'value counts in sim :\n{self.df['Sim'].value_counts()}')
            # value count in Region
            logger.info(f'value counts in region :\n{self.df['Region'].value_counts()}')

        except Exception as e:
            error_type, error_msg, error_line = sys.exc_info()
            logger.info(f'Error in line no:{error_line.tb_lineno} due to:{error_msg}')

    # this is for ploting
    def plot(self):
        try:
            PLOT.plots(self.df)
        except Exception as e:
            error_type, error_msg, error_line = sys.exc_info()
            logger.info(f'Error in line no:{error_line.tb_lineno} due to:{error_msg}')

if __name__ == '__main__':
    try:
        obj=EDA('D:\\Projects\\Customer churn eda\\Customer_churn.csv')
        obj.plot()
    except Exception as e:
        error_type, error_msg, error_line = sys.exc_info()
        logger.info(f'Error in line no:{error_line.tb_lineno} due to:{error_msg}')