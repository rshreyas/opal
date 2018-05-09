#!/usr/bin/env python
'''
Some shared Python functions for Opal helper scripts.
'''
import re

def fasta_reader(f):
    '''Generator expression that returns a fasta sequence
        
        Ignores quality score string of FASTQ file
    '''
    seq = ''
    name = ''
    ignore_line = False
    first_line = True
    while True:
        line = f.readline()
        if line=='':
            if seq=='':
                break
            else:
                yield (name, seq)
                name = ''
                seq = ''
        elif line[0]=='>':
            if first_line:
                first_line = False
                pass
            else:
                yield (name, seq)
            name = line[1:].rstrip('\n')
            seq = ''
            ignore_line = False
        elif line[0]=='+':
            # Ignore quality score strings
            ignore_line = True
        else:
            if ignore_line:
                pass
            else:
                seq = seq + line.rstrip('\n')


complement = {}
for letter in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
    complement[letter] = letter.upper()
complement['A']='T'
complement['T']='A'
complement['C']='G'
complement['G']='C'
def reverse_complement(dna):
    '''Takes the DNA reverse complement, but ignores letters other than ATCG, and fails on non-alphabetical input'''
    return ''.join([complement[base] for base in dna[::-1]])

def get_all_substrings(input_string, k):
    length = len(input_string)
    return [input_string[i:i+k] for i in range(length - k + 1)]

pat = re.compile('^[ACGTacgt]*$')
def check_acgt(s):
    return pat.match(s)

