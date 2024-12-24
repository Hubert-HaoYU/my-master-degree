# Hao YU
# 2024.12.24
from Bio import Entrez
Entrez.email = "cya.hao@outlook.com"

protein_id_list_filepath = input("Protein Accession ID List:")
nucleotide_id_list_filepath = input("Nucleotide Accession ID List:")

with open(protein_id_list_filepath, "r") as input:
    with open(nucleotide_id_list_filepath, "w") as output:
        for line in input.readlines():
            line = line.strip()
            handle = Entrez.efetch(db = "ipg", id = line, rettype = "gb", retmode = "txt")
            record = Entrez.read(handle)
            handle.close()
        for seq_record in record:
            nucleotide_id = seq_record["ACCESSION"]
            output.write(nucleotide_id)
        output.close()
    input.close()