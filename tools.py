sequence_AA = "KKKKKKKKKKKKKKKKKKKKKKKKKKKKK"
sequence_lyzozymepoulet = "KVFGRCELAAAMKRHGLDNYRGYSLGNWVCAAKFESNFNTQATNRNTDGSTDYGILQINSRWWCNDGRTPGSRNLCNIPCSALLSSDITASVNCAKKIVSDGNGMNAWVAWRNRCKGTDVQAWIRGCRL"



def calc_hydrophobicity(sequence):
    # Define hydrophobicity values for individual amino acids
    hydrophobicity_values = {
        'A': 1.8,
        'R': -4.5,
        'N': -3.5,
        'D': -3.5,
        'C': 2.5,
        'Q': -3.5,
        'E': -3.5,
        'G': -0.4,
        'H': -3.2,
        'I': 4.5,
        'L': 3.8,
        'K': -3.9,
        'M': 1.9,
        'F': 2.8,
        'P': -1.6,
        'S': -0.8,
        'T': -0.7,
        'W': -0.9,
        'Y': -1.3,
        'V': 4.2
    }

    hydrophobicity = 0
    for aa in sequence:
        if aa in hydrophobicity_values:
            hydrophobicity += hydrophobicity_values[aa]
    return hydrophobicity

frequency = "att"
string = "attgttgattgccgtattgatt"

def find_and_write_all_frequency_recurrences(string, frequency):
    """
    This function searches for all recurrences of a given frequency of nucleotids in the input string of nucleotides and writes the results to a file.
    """
    start = 0
    result = []
    while True:
        index = string.find(frequency, start)
        if index == -1:
            break
        result.append(index)
        start = index + 1
    
    with open("frequency_recurrence_result.txt", "w") as file:
        if result:
            file.write("The frequency '{}' was found at the following positions in the input string:\n".format(frequency))
            for i, pos in enumerate(result):
                file.write("Position {}: {}\n".format(i+1, pos))
        else:
            file.write("The frequency '{}' was not found in the input string.".format(frequency))

#find_and_write_all_frequency_recurrences(string, frequency)

def calc_pI(sequence):
    # Define pK ranges for individual amino acids
    pK_ranges = {
        'K': (10.4, 10.8),
        'R': (12.0, 12.5),
        'H': (6.0, 7.4),
        'D': (3.8, 4.4),
        'E': (4.0, 4.8),
        'C': (8.0, 8.5),
        'Y': (9.6, 10.1),
        'N': (7.5, 8.7),
        'Q': (5.0, 6.0),
        'W': (5.2, 5.4),
        'S': (5.6, 5.9),
        'T': (5.6, 6.1),
        'M': (5.5, 5.8),
        'A': (6.0, 7.6),
        'F': (4.0, 4.5),
        'G': (9.0, 10.0),
        'I': (6.0, 6.5),
        'L': (6.0, 6.5),
        'P': (7.2, 8.8),
        'V': (6.0, 6.5),
    }

    # Define function to calculate net charge at given pH
    def calc_net_charge(pH, pK_ranges, sequence):
        net_charge = 0
        for aa in sequence:
            if aa in pK_ranges:
                pK_min, pK_max = pK_ranges[aa]
                if pH <= pK_min:
                    net_charge += 1
                elif pH >= pK_max:
                    net_charge -= 1
                else:
                    net_charge += (10**(pK_min - pH) - 10**(pK_max - pH)) / (1 + 10**(pK_min - pH) + 10**(pH - pK_max))
        return net_charge

    # Use bisection method to find pI with 0.01 pH unit precision
    a = 0
    b = 14
    while (b - a) > 0.01:
        c = (a + b) / 2
        if calc_net_charge(c, pK_ranges, sequence) > 0:
            a = c
        else:
            b = c

    return (a + b) / 2


def calculate_thermal_stability(sequence):
    # Initialize the thermal stability to zero
    stability = 0.0
    
    # Runs through each amino acid in the sequence
    for aa in sequence:
    # Adds amino acid dependent stability value to total stability (empirical and arbitrary weights, and not depending of the temperature)
        if aa == 'A':
            stability += 0.5
        elif aa == 'C':
            stability += 0.3
        elif aa == 'D':
            stability -= 0.8
        elif aa == 'E':
            stability -= 0.7
        elif aa == 'F':
            stability += 1.2
        elif aa == 'G':
            stability += 0.0
        elif aa == 'H':
            stability += 0.5
        elif aa == 'I':
            stability += 1.0
        elif aa == 'K':
            stability -= 1.5
        elif aa == 'L':
            stability += 1.0
        elif aa == 'M':
            stability += 0.6
        elif aa == 'N':
            stability -= 0.5
        elif aa == 'P':
            stability -= 0.3
        elif aa == 'Q':
            stability -= 0.7
        elif aa == 'R':
            stability -= 2.5
        elif aa == 'S':
            stability -= 0.1
        elif aa == 'T':
            stability += 0.4
        elif aa == 'V':
            stability += 0.7
        elif aa == 'W':
            stability += 1.3
        elif aa == 'Y':
            stability += 0.9
        elif aa == 'U':
            stability += 0.2  # S??l??nocyst??ine
        elif aa == 'O':
            stability += 0.0  # Pyrrolysine
    
    # Return the total thermal stability
    return stability

print("Le point iso??lectrique est d'environ", calc_pI(sequence_AA), ", ce r??sultat peut varier en fonction des conditions environnementales.", "\nL'Hydrophbicit?? de la prot??ine est d'environ", calc_hydrophobicity(sequence_AA), "\nLa stabilit?? thermique est d'environ", calculate_thermal_stability(sequence_AA))


"""Dans la fonction que j'ai cod??e pr??c??demment, je n'ai pas sp??cifi?? de temp??rature particuli??re ?? laquelle la stabilit?? thermique doit ??tre 
calcul??e. La stabilit?? thermique est une propri??t?? physique qui d??pend de la temp??rature ?? laquelle la prot??ine est expos??e. 
En g??n??ral, la stabilit?? thermique est mesur??e ?? une temp??rature de 25??C ou de 37??C, qui sont des temp??ratures couramment utilis??es pour 
les exp??riences de biologie mol??culaire. Cependant, la stabilit?? thermique peut varier en fonction de la temp??rature, et certaines prot??ines 
peuvent ??tre plus stables ou moins stables ?? des temp??ratures diff??rentes.

Il est important de noter que dans la fonction que j'ai cod??e, les valeurs de stabilit?? que j'ai utilis??es pour 
chaque acide amin?? sont des valeurs arbitraires qui ne sont pas bas??es sur des mesures exp??rimentales pr??cises. Ces valeurs ont ??t?? choisies ?? 
titre d'exemple pour illustrer le principe g??n??ral de la fonction. En pratique, les valeurs de stabilit?? d??pendent des propri??t??s 
physico-chimiques de chaque acide amin?? et sont souvent d??termin??es exp??rimentalement ?? l'aide de techniques telles que la calorim??trie 
?? haute pr??cision ou la spectroscopie de fluorescence."""

"""La stabilit?? thermique d'une prot??ine est une mesure de sa capacit?? ?? maintenir sa structure tridimensionnelle ?? une temp??rature donn??e. 
Une valeur de stabilit?? thermique positive indique que la prot??ine est stable ?? cette temp??rature, c'est-??-dire qu'elle conserve sa structure 
tridimensionnelle. ?? l'inverse, une valeur de stabilit?? thermique n??gative indique que la prot??ine est instable ?? cette temp??rature, c'est-??-dire 
qu'elle risque de se d??naturer et de perdre sa structure tridimensionnelle.

Dans le contexte de la fonction que nous avons cod??e, une stabilit?? thermique positive signifie que la prot??ine cod??e par la s??quence d'acides
amin??s en entr??e est stable ?? une temp??rature donn??e, tandis qu'une stabilit?? thermique n??gative indique qu'elle est instable. Cependant, il est 
important de noter que les valeurs de stabilit?? calcul??es par cette fonction sont des valeurs arbitraires que j'ai choisies ?? titre d'exemple et 
que la stabilit?? thermique r??elle d'une prot??ine d??pend de nombreux facteurs, tels que sa s??quence d'acides amin??s, sa structure 
tridimensionnelle, sa composition en acides amin??s, son environnement, etc."""