# mb-2023_poster

## workflow

1. Create a table like https://pathbank.org/downloads/pathbank_all_metabolites.csv.zip for each pathway database
2. Create a table like https://pathbank.org/downloads/pathbank_all_metabolites.csv.zip for each MW "MS (not NMR)" study
3. FILLME

### MW sub workflow

1. FILTER "analysis_type   MS" from study-study_id-ST-named_metabolites.json
2. FILLME

## databases

### KEGG (API)
- KEGG compound mol files in KEGG pathways (retrieved 2023/10/03)

### Metabolomics Workbench
- Metabolomics WorkBench REST service
- refmet.csv from https://www.metabolomicsworkbench.org/databases/refmet/browse.php (A total of 167735 compounds or isobaric mixtures as of 10/06/23)

### PathBank
- Metabolite names linked to PathBank pathways CSV (includes KEGG and ChEBI IDs) from https://pathbank.org/downloads (Generated On Oct 18 2019)

### WikiPathways
- WikiPathways SPARQL queries https://www.wikipathways.org/sparql.html


### keep
- https://docs.chemaxon.com/display/docs/molconvert.md
- https://ftp.ncbi.nlm.nih.gov/pubchem/Compound/Extras/

```
>>> import subprocess
>>> output = subprocess.run(["molconvert", "inchikey", "C01041.mol"], capture_output=True, text=True).stdout
>>> print(output)
InChIKey=CIWBSHSKHKDKBQ-JLAZNSOCSA-N
```


## References
1. Kanehisa, M., Furumichi, M., Sato, Y., Kawashima, M. and Ishiguro-Watanabe, M.; KEGG for taxonomy-based analysis of pathways and genomes. Nucleic Acids Res. 51, D587-D592 (2023).
2. 
