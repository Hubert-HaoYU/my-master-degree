from Bio import Entrez
import time
import threading

Entrez.email = "cya.hao@outlook.com"
global total_tasks

def readInputFile(inputFilePath):
    with open(inputFilePath, "r") as inputFile:
        lines = inputFile.readlines()
        global total_tasks
        total_tasks = len(lines)
        accession_id_nucleotide = []
        for i in lines:
            i = i.strip()
            accession_id_nucleotide.append(i)
    return accession_id_nucleotide

def worker(accession_id_nucleotide, outputFilePath, thread_id):
    with open(outputFilePath, "a") as outputFile:
        for i in accession_id_nucleotide:
            try:
                time.sleep(0.5)
                handle = Entrez.efetch(db="nucleotide", id=i, rettype="fasta", retmode="text")
                record = str(handle.read())
                outputFile.write(record + "\n")
                outputFile.flush()
                print(f"Thread {thread_id}: Processed {i}")
            except Exception as e:
                print(f"Thread {thread_id}: Error processing {i} - {e}")

def ncbi_fetching_and_writting(accession_id_nucleotide, outputFilePath, num_threads=4):
    threads = []
    tasks_per_thread = len(accession_id_nucleotide) // num_threads
    for i in range(num_threads):
        start_index = i * tasks_per_thread
        end_index = None if i == num_threads - 1 else (i + 1) * tasks_per_thread
        sub_accession_id_nucleotide = accession_id_nucleotide[start_index:end_index]
        if sub_accession_id_nucleotide:  # 确保每个线程都有任务
            thread = threading.Thread(target=worker, args=(sub_accession_id_nucleotide, outputFilePath, i + 1))
            threads.append(thread)
            thread.start()
            print(f"Thread {i+1} started")  # 确认线程启动
        else:
            print(f"Thread {i+1} has no tasks")

    for thread in threads:
        thread.join()

# 调用函数
accession_id_nucleotide = readInputFile("D:/Workspace/master/provirus/nr_accession_ids_nucleotide_simplified_missed.txt")
outputFilePath = "D:/Workspace/master/provirus/nr_sequence_nucleotide.fasta"
ncbi_fetching_and_writting(accession_id_nucleotide, outputFilePath, num_threads=4)