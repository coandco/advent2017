import math

INPUT = """set b 99
set c b
jnz a 2
jnz 1 5
mul b 100
sub b -100000
set c b
sub c -17000
set f 1
set d 2
set e 2
set g d
mul g e
sub g b
jnz g 2
set f 0
sub e -1
set g e
sub g b
jnz g -8
sub d -1
set g d
sub g b
jnz g -13
jnz f 2
sub h -1
set g b
sub g c
jnz g 2
jnz 1 3
sub b -17
jnz 1 -23"""

DIGESTED_INPUT = [x.split() for x in INPUT.split("\n")]


def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def do_thing(initial_number, offset):
    r = dict.fromkeys(list("abcdefgh"), 0)
    r['b'] = initial_number
    r['c'] = initial_number + offset
    r['f'] = 0
    while r['b'] != r['c']:
        print("Register states at beginning of loop: %r" % r)
        r['f'] = 1
        r['d'] = 2
        r['e'] = 2
        while r['d'] != r['b']:
            if (r['d'] * r['e']) == r['b']:
                r['f'] = 0
            r['e'] += 1
            if r['e'] != r['b']:
                continue
            r['d'] += 1
            r['e'] = 2
        if r['f'] != 0:
            r['h'] += 1
        r['b'] += 17
    return r['h']


#b = 8
#output = do_thing(b, 51)
#print("Number returned from [%d,%d,%d,%d]: %d" % (b, b+17, b+(17*2), b+(17*3), output))
#exit()


def number_or_register(register_dict, value):
    try:
        test = int(value)
        return test
    except ValueError:
        return register_dict[value]


def do_set(register_dict, instruction, program_counter):
    register_to = instruction[1]
    value_from = number_or_register(register_dict, instruction[2])
    register_dict[register_to] = value_from
    program_counter += 1
    return program_counter


def do_sub(register_dict, instruction, program_counter):
    register_to = instruction[1]
    value_from = number_or_register(register_dict, instruction[2])
    register_dict[register_to] -= value_from
    program_counter += 1
    return program_counter


def do_mul(register_dict, instruction, program_counter):
    register_to = instruction[1]
    value_from = number_or_register(register_dict, instruction[2])
    register_dict[register_to] *= value_from
    program_counter += 1
    return program_counter


def do_mod(register_dict, instruction, program_counter):
    register_to = instruction[1]
    value_from = number_or_register(register_dict, instruction[2])
    register_dict[register_to] %= value_from
    program_counter += 1
    return program_counter


def do_jgz(register_dict, instruction, program_counter, instance=0):
    conditional = number_or_register(register_dict, instruction[1])
    offset = number_or_register(register_dict, instruction[2])
    if conditional > 0:
        program_counter += offset
    else:
        program_counter += 1
    return program_counter


def do_jnz(register_dict, instruction, program_counter):
    conditional = number_or_register(register_dict, instruction[1])
    offset = number_or_register(register_dict, instruction[2])
    if conditional != 0:
        program_counter += offset
    else:
        program_counter += 1
    return program_counter


INSTRUCTION_MAP = {'set': do_set,
                   'sub': do_sub,
                   'mul': do_mul,
                   'mod': do_mod,
                   'jnz': do_jnz,
                   'jgz': do_jgz}

REGISTERS = dict.fromkeys(list("abcdefgh"), 0)
program_counter = 0
mul_counter = 0

while True:
    # If we're out of bounds, terminate
    if program_counter < 0 or program_counter >= len(DIGESTED_INPUT):
        print("Program went out of bounds at address %d" % program_counter)
        break
    current_instruction = DIGESTED_INPUT[program_counter]
    if current_instruction[0] == "mul":
        mul_counter += 1
    #print("Executing line %d: %r" % (program_counter, current_instruction))
    if program_counter == 9:
        print("Breakpoint snapshot for %d %r: %r" % (program_counter, current_instruction, REGISTERS))
    program_counter = INSTRUCTION_MAP[current_instruction[0]](REGISTERS, current_instruction, program_counter)
    #print("Registers: %r" % REGISTERS)
    #if program_counter == 12:
    #    print("Breakpoint snapshot for %d %r: %r" % (program_counter, current_instruction, REGISTERS))

print("Number of times mul is invoked: %d" % mul_counter)

num_primes = 0
total_checked = 0
for i in xrange(109900, 109900+17001, 17):
    print("i is %d" % i)
    total_checked += 1
    if not is_prime(i):
        num_primes += 1

print("Final value of h: %d" % num_primes)
print("Total values checked: %d" % total_checked)
