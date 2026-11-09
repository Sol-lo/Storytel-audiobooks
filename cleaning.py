import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def cleaning_df(df):
    return(df
           .drop(columns=[
               "Kunde-ID",
                "Antall tegn i boken",
                "Format"]
                 )
           .rename(columns = {"Boktittel" : "tittel",
                   "Bok-ISBN" : "isbn",
                   "Bokmerkeplassering" : "bokmerke",
                   "Startdato" : "start",
                   "Siste bokmerke opprettet" : "slutt"}
                   )
           .assign(start = lambda x : pd.to_datetime(x.start), #lambda means were doing the same to every line in start
                   slutt = lambda x : pd.to_datetime(x.slutt),
                   delta = lambda x : x.slutt - x.start, #how long have I spent reading the book
                   delta_s = lambda x : x.delta.dt.total_seconds() #readingtime (delta) converted to seconds
                   )        
    )