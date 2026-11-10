import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#making a function that cleans the dataframe
def cleaning_df(df):
    return(df
           .drop(columns=[
               "Kunde-ID",
                "Antall tegn i boken",
                "Format"]
                 ) #choosing which columns to exclude
           .rename(columns = {"Boktittel" : "title",
                   "Bok-ISBN" : "isbn",
                   "Bokmerkeplassering" : "bookmark",
                   "Startdato" : "start",
                   "Siste bokmerke opprettet" : "stop"}
                   ) #renaming columns
           .assign(start = lambda x : pd.to_datetime(x.start), #lambda means were doing the same to every line in start
                   stop = lambda x : pd.to_datetime(x.stop),
                   delta = lambda x : x.stop - x.start, #how long have I spent reading the book
                   delta_s = lambda x : x.delta.dt.total_seconds() #readingtime (delta) converted to seconds
                   ) #rewriting start and stop columns to a better format and making new columns showing how loong it took to read the books   
    )