import pandas as pd
import pickle

mw_df = pd.read_table("data/mw/refmet_in_allmsstudies_hasinchikey.tsv")

kegg_df = pd.read_table("data/kegg/pathway_inchikey_dict.tsv")
pathbank_df = pickle.load("data/pathbank/pathbank_all_metabolites.pkl.gz")
wikipathways_df = pd.read_csv("data/wikipathways/wikipathways2inchikey.csv")
