from Bio import SeqIO
import re

def read_ids_from_file(id_file):
    ids = []
    with open(id_file, 'r') as f:
        for line in f:
            line = line.strip()
            if line:
                ids.append(line)
    return ids

def search_and_write(input_file, output_file, ids): 
    with open(output_file, 'w') as output_handle:
        for record in SeqIO.parse(input_file, "fasta"):
            location = record.id.find("|")
            id = record.id[:location]
            if id in ids:
                SeqIO.write(record, output_handle, "fasta")

id_filename = "D:/Workspace/master/provirus/imgvr_accession_ids_protein_general.txt"
input_filename = "D:/Datasets/IMGVR_7.1_hc/IMGVR_7.1_hc_nucleotide.fna"
output_filename = "D:/Workspace/master/provirus/imgvr_sequence_nucleotide.fasta"

ids_to_match = read_ids_from_file(id_filename)
search_and_write(input_filename, output_filename, ids_to_match)