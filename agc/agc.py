"""OTU clustering"""

#!/bin/env python3
# -*- coding: utf-8 -*-
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#    A copy of the GNU General Public License is available at
#    http://www.gnu.org/licenses/gpl-3.0.html

# [A]
import argparse
# [G]
import gzip
# [O]
import os
# [S]
import statistics
import sys
# [T]
import textwrap

# [C]
from collections import Counter

# [N]
import nwalign3 as nw

__author__ = "ROUAUD Lucas"
__credits__ = __author__
__version__ = "1.0.0"
__maintainer__ = __author__
__email__ = "lucas.rouaud@gmail.com"
__status__ = "Developpement"


def isfile(path):
    """Check if path is an existing file.
      :Parameters:
          path: Path to the file
    """
    if not os.path.isfile(path):
        if os.path.isdir(path):
            msg = f"{path} is a directory"
        else:
            msg = f"{path} does not exist."
        raise argparse.ArgumentTypeError(msg)
    return path


def get_arguments():
    """Retrieves the arguments of the program.
      Returns: An object that contains the arguments
    """
    # Parsing arguments
    parser = argparse.ArgumentParser(description=__doc__,
                                     usage=f"{sys.argv[0]} -h")

    parser.add_argument("-i", "-amplicon_file", dest="amplicon_file",
                        type=isfile, required=True, help=("Amplicon is a "
                                                          "compressed fasta "
                                                          "file (.fasta.gz)"))
    parser.add_argument("-s", "-minseqlen", dest="minseqlen", type=int,
                        default=400, help=("Minimum sequence length for "
                                           "dereplication (default 400)"))
    parser.add_argument("-m", "-mincount", dest="mincount", type=int,
                        default=10, help=("Minimum count for dereplication "
                                          "(default 10)"))
    parser.add_argument("-c", "-chunk_size", dest="chunk_size", type=int,
                        default=100, help=("Chunk size for dereplication "
                                           "(default 100)"))
    parser.add_argument("-k", "-kmer_size", dest="kmer_size", type=int,
                        default=10, help=("kmer size for dereplication "
                                         "(default 10)"))
    parser.add_argument("-o", "-output_file", dest="output_file", type=str,
                        default="OTU.fasta", help="Output file")

    return vars(parser.parse_args())

def read_fasta(amplicon_file, minseqlen):
    """Read a given fasta file.
    """
    return (amplicon_file, minseqlen)


def dereplication_fulllength(amplicon_file, minseqlen, mincount):
    """dereplication_fulllength
    """
    return (amplicon_file, minseqlen, mincount)

def get_identity(alignment_list):
    """Percent identity between two sequences.
    """
    return alignment_list

def abundance_greedy_clustering(amplicon_file, minseqlen, mincount, chunk_size,
                                kmer_size):
    """abundance_greedy_clustering.
    """
    return (amplicon_file, minseqlen, mincount, chunk_size, kmer_size)

def write_OTU(OTU_list, output_file):
    """write_OTU.
    """
    return (OTU_list, output_file)

def get_unique(ids):
    """get_unique.
    """
    return {}.fromkeys(ids).keys()

def common(lst1, lst2):
    """common.
    """
    return list(set(lst1) & set(lst2))

def get_chunks(sequence, chunk_size):
    """Split sequences in a least 4 chunks.
    """
    return (sequence, chunk_size)

def cut_kmer(sequence, kmer_size):
    """Cut sequence into kmers.
    """
    return (sequence, kmer_size)

def get_unique_kmer(kmer_dict, sequence, id_seq, kmer_size):
    """get_unique_kmer.
    """
    return (kmer_dict, sequence, id_seq, kmer_size)

def detect_chimera(perc_identity_matrix):
    """detect_chimera.
    """
    return perc_identity_matrix

def search_mates(kmer_dict, sequence, kmer_size):
    """search_mates.
    """
    return (kmer_dict, sequence, kmer_size)

def chimera_removal(amplicon_file, minseqlen, mincount, chunk_size, kmer_size):
    """chimera_removal.
    """
    return (amplicon_file, minseqlen, mincount, chunk_size, kmer_size)


if __name__ == "__main__":
    True
