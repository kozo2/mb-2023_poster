# mb-2023_poster

## workflow

1. Create a table like https://pathbank.org/downloads/pathbank_all_metabolites.csv.zip for each pathway database
2. Get all "MS" (not NMR) MWB study IDs
3. Get all refmet IDs for each MWB study ID
4. FILLME

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


## References
1. Kanehisa, M., Furumichi, M., Sato, Y., Kawashima, M. and Ishiguro-Watanabe, M.; KEGG for taxonomy-based analysis of pathways and genomes. Nucleic Acids Res. 51, D587-D592 (2023).
2. 
