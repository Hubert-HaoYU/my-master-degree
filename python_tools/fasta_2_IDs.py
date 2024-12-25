from Bio import SeqIO

def extract_ids_from_fasta(fasta_file, output_file):
    """
    Extracts sequence IDs from a FASTA file using seqio and writes them to a new text file.

    Parameters:
    fasta_file (str): The path to the input FASTA file.
    output_file (str): The path to the output text file where sequence IDs will be written.
    """
    with open(output_file, 'w') as output_handle:
        for record in SeqIO.parse(fasta_file, "fasta"):
            output_handle.write(f"{record.id}\n")

fasta_file_path = "D:/Workspace/master/provirus/nr_sequence_nucleotide.fasta"  # 替换为你的 FASTA 文件路径
output_text_file_path = "D:/Workspace/master/provirus/IDs.txt"  # 替换为你想要保存 ID 的文本文件路径

extract_ids_from_fasta(fasta_file_path, output_text_file_path)