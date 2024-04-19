import os
import subprocess

fasta_files = [f for f in os.listdir(os.getcwd()) if f.endswith('.fa')]

for file in fasta_files:
    with open(file, 'r') as f:
        sequence = f.read().strip().split('\n')[1]

    output = subprocess.Popen(['RNAfold', '-d2', '--noLP'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    mfe_output, mfe_error = output.communicate(input=sequence.encode('utf-8'))
    mfe_output = mfe_output.decode('utf-8')

    mfe_energy = mfe_output.strip().split('\n')[1].split()[-1]

    with open(file, 'a') as f:
        f.write('\nMFE Energy: {}'.format(mfe_energy))

