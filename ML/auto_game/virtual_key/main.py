from subprocess import Popen, PIPE
from time import sleep

control_f4_sequence = '''keydown Control_L
key F4
keyup Control_L
'''

shift_a_sequence = '''keydown Shift_L
key A
keyup Shift_L
'''

key_L = '''key Left
'''
key_R = '''key Right
'''
key_U = '''key Up
'''
key_D = '''key Down
'''

def keypress(sequence):
    p = Popen(['xte'], stdin=PIPE)
    p.communicate(input=sequence)

#   keypress(shift_a_sequence)
#   keypress(control_f4_sequence)

while 1:
    keypress(key_U)
    keypress(key_D)
    sleep(0.3)
