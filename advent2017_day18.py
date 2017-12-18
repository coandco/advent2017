import Queue

INPUT = """set i 31
set a 1
mul p 17
jgz p p
mul a 2
add i -1
jgz i -2
add a -1
set i 127
set p 618
mul p 8505
mod p a
mul p 129749
add p 12345
mod p a
set b p
mod b 10000
snd b
add i -1
jgz i -9
jgz a 3
rcv b
jgz b -1
set f 0
set i 126
rcv a
rcv b
set p a
mul p -1
add p b
jgz p 4
snd a
set a b
jgz 1 3
snd b
set f 1
add i -1
jgz i -11
snd a
jgz f -16
jgz a -19"""

REGISTERS = dict.fromkeys(list("abcdefghijklmnopqrstuvwxyz"), 0)

DIGESTED_INPUT = [x.split() for x in INPUT.split("\n")]

last_sound = None


def number_or_register(register_dict, value):
    try:
        test = int(value)
        return test
    except ValueError:
        return register_dict[value]


def do_sound(register_dict, instruction, program_counter, instance=0):
    global last_sound
    register = instruction[1]
    last_sound = register_dict[register]
    program_counter += 1
    return program_counter


def do_send(register_dict, instruction, program_counter, instance):
    queue = queues[1] if instance == 0 else queues[0]
    queue.put(number_or_register(register_dict, instruction[1]))
    program_counter += 1
    return program_counter


def do_receive(register_dict, instruction, program_counter, instance):
    register_dict[instruction[1]] = queues[instance].get()
    program_counter += 1
    return program_counter


def do_set(register_dict, instruction, program_counter, instance=0):
    register_to = instruction[1]
    value_from = number_or_register(register_dict, instruction[2])
    register_dict[register_to] = value_from
    program_counter += 1
    return program_counter


def do_add(register_dict, instruction, program_counter, instance=0):
    register_to = instruction[1]
    value_from = number_or_register(register_dict, instruction[2])
    register_dict[register_to] += value_from
    program_counter += 1
    return program_counter


def do_mul(register_dict, instruction, program_counter, instance=0):
    register_to = instruction[1]
    value_from = number_or_register(register_dict, instruction[2])
    register_dict[register_to] *= value_from
    program_counter += 1
    return program_counter


def do_mod(register_dict, instruction, program_counter, instance=0):
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


last_sound = None
program_counter = 0

INSTRUCTION_MAP = {'snd': do_sound,
                   'set': do_set,
                   'add': do_add,
                   'mul': do_mul,
                   'mod': do_mod,
                   'jgz': do_jgz}

while True:
    # If we're out of bounds, terminate
    if program_counter < 0 or program_counter >= len(DIGESTED_INPUT):
        print("Program went out of bounds at address %d" % program_counter)
        break
    current_instruction = DIGESTED_INPUT[program_counter]
    if current_instruction[0] == "rcv":
        if current_instruction[1] != 0:
            print("Recovered frequency: %d" % last_sound)
            break
        else:
            program_counter += 1
    else:
        program_counter = INSTRUCTION_MAP[current_instruction[0]](REGISTERS, current_instruction, program_counter)
    print("New program counter: %d" % program_counter)

REGISTERS = dict.fromkeys(list("abcdefghijklmnopqrstuvwxyz"), 0)
MULTI_REGISTERS = [dict(REGISTERS), dict(REGISTERS)]
MULTI_REGISTERS[1]['p'] = 1

INSTRUCTION_MAP = {'snd': do_send,
                   'rcv': do_receive,
                   'set': do_set,
                   'add': do_add,
                   'mul': do_mul,
                   'mod': do_mod,
                   'jgz': do_jgz}

pc_list = [0, 0]
values_sent = [0, 0]
queues = [Queue.Queue(), Queue.Queue()]
halted_flags = [False, False]
cur_instance = 0


while not (halted_flags[0] is True and halted_flags[1] is True):
    if pc_list[cur_instance] < 0 or pc_list[cur_instance] >= len(DIGESTED_INPUT):
        halted_flags[cur_instance] = True
        cur_instance = 1 if cur_instance == 0 else 0
        continue
    current_instruction = DIGESTED_INPUT[pc_list[cur_instance]]
    if current_instruction[0] == 'rcv':
        if queues[cur_instance].empty():
            halted_flags[cur_instance] = True
            cur_instance = 1 if cur_instance == 0 else 0
            continue
        else:
            pc_list[cur_instance] = INSTRUCTION_MAP[current_instruction[0]](MULTI_REGISTERS[cur_instance],
                                                                            current_instruction,
                                                                            pc_list[cur_instance],
                                                                            cur_instance)
    elif current_instruction[0] == 'snd':
        other_instance = 1 if cur_instance == 0 else 0
        halted_flags[other_instance] = False
        values_sent[cur_instance] += 1
        pc_list[cur_instance] = INSTRUCTION_MAP[current_instruction[0]](MULTI_REGISTERS[cur_instance],
                                                                        current_instruction,
                                                                        pc_list[cur_instance],
                                                                        cur_instance)
    else:
        pc_list[cur_instance] = INSTRUCTION_MAP[current_instruction[0]](MULTI_REGISTERS[cur_instance],
                                                                        current_instruction,
                                                                        pc_list[cur_instance],
                                                                        cur_instance)

print("Values sent before both stop: %r" % values_sent)
