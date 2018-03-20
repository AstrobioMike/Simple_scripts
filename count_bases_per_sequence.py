#!/usr/bin/env python

### Script that spits out a tab-delimited file with two columns containing the header and the number of bases for each sequence of a multifasta file ###

from Bio import SeqIO
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-i", "--input_fasta", help="Original fasta file", action="store", dest="input_fasta", default=True)
parser.add_argument("-o", "--output_txt_file", help="Name of output txt file", action="store", dest="output_file", default=True)

args = parser.parse_args()

in_fasta = open(args.input_fasta, "r")
out_file = open(args.output_file, "w")

for seq_record in SeqIO.parse(in_fasta, "fasta"):
  out_file.write(seq_record.id + "\t" + str(len(seq_record.seq)) + "\n")
  
in_fasta.close()
out_file.close()

