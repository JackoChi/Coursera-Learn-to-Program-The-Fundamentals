def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    return len(dna)


def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    return len(dna1) > len(dna2)


def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    count = 0
    
    for char in dna:
        if char in nucleotide:
            count = count + 1
    return count

def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """
    return dna2 in dna1

def is_valid_sequence(dna):
    ''' (str) -> bool
    
    Return True if and only if the DNA sequence is valid 
    (that is, it contains no characters other than 'A', 'T', 'C' and 'G'). 
    
    Precondition:  A string is not a valid DNA sequence 
    if it contains lowercase letters.
    
    >>> is_valid_sequence('ATCGGC')
    True
    >>> is_valid_sequence('ABCDEF')
    False
    >>> is_valid_sequence('')
    False
    '''
    count = 0
    
    if dna.islower() == True:
        return False
    else:
        for char in dna:
            if char == 'A' or char == 'T' or char == 'C' or char == 'G':
                count = count + 1
    
        if count == len(dna):
            return True
        else:
            return False
    
def insert_sequence(dna1, dna2, index):
    ''' (str, str, int) -> str
    
    Return the DNA sequence obtained by inserting the second DNA sequence
    into the first DNA sequence at the given index.
    
    >>> insert_sequence('CCGG', 'AT', 2)
    CCATGG
    >>> insert_sequence('AATT', 'CCGG', 4)
    AATTCCGG
    
    '''
    if is_valid_sequence(dna1) == True and is_valid_sequence(dna2) == True:
        return dna1[:index] + dna2 + dna1[index:]
    else: 
        return 'Please insert a valid DNA'
    
def get_complement(dna):
    ''' (str) -> str
    
    Return the nucleotide's complement.
     
    >>> get_complement('A')
    T
    >>> get_complement('T')
    A
    >>> get_complement('C')
    G
    >>> get_complement('G')
    C
     
    '''
    for char in dna:
        if char == 'A':
            return 'T'
        elif char == 'T':
            return 'A'
        elif char == 'C':
            return 'G'
        elif char == 'G':
            return 'C'
        else:
            return None
        
def get_complementary_sequence(dna):
    ''' (str) -> str
    
    Return the DNA sequence that is complementary to the given DNA sequence.
    
    >>> get_complementary_sequence('AT')
    TA
    >>> get_complementary_sequence('ACGTACG')
    TGCATGC
    
    '''
    
    compl_seq = ''
    
    for char in dna:
        compl_seq = compl_seq + get_complement(char)
    return compl_seq
            
     
    
    
