# by Uvajda (Karl Zander) - KryptoMagick 2021

''' Document Decryptor version ADA '''

version = "ADA"

class Record:
    text ={}
    keys = {}
    modulus = 0
    mask = 0
    result = {}
    path = {}

def _file_reader(filename, record):
    fd = open(filename, "r")
    data = fd.read()
    fd.close()
    textline = data.split('\n')[0]
    keyline = data.split('\n')[1]
    text = textline.split()
    key = keyline.split()
    textline_len = len(textline)
    
    for c in range(textline_len):
        record.text[c] = textline[c]
        record.keys[c] = keyline[c]
    return record

def _alphabet_generator(n):
    alphabet = {}
    alphabet_list = []
    for c in range(n):
        x = c % 26
        letter = chr(x  + 65)
        alphabet[x % 26] = letter
        alphabet_list.append(letter)
    return alphabet, alphabet_list

def _code_generator(text, alphabet, key, mask):
    textlen = len(text)
    modulus = textlen
    msg = []
    if mask == 4:
        msg0 = []
        msg1 = []
        msg2 = []
        m = []
        msg0_m = []
        msg1_m = []
        msg2_m = []
        msg0_p = []
        msg1_p = []
        msg2_p = []

        for x in range(textlen):
            number = ord(text[x]) - 65
            key_number = ord(key[x]) - 65
            output = (number + key_number) % 26
            letter = alphabet[output]
            msg0.append(letter)
        L0 = _line_converter("".join(msg0))
        L0_m = _line_multiplier(L0, L0, modulus)
        L0_p = _line_power(L0, L0, modulus)

        base = L0
        itera = 1000
        jump = 39

        floor0B = _floor_makerB(base, itera, jump)
        floor0BA = _floor_makerBA(base, itera, jump)
        floor0BB = _floor_makerBB(base, itera, jump)
        floor0BC = _floor_makerBC(base, itera, jump)
        
        wall0B = _wall_makerB(jump, itera, base)
        wall0BA = _wall_makerBA(jump, itera, base)
        wall0BB = _wall_makerBB(base, itera, jump)
        wall0BC = _wall_makerBC(base, itera, jump)
        
        for x in range(textlen):
            number = ord(text[x]) - 65
            key_number = ord(key[x]) - 65
            output = (key_number - number) % 26
            letter = alphabet[output]
            msg1.append(letter)
        L1 = _line_converter("".join(msg1))
        L1_m = _line_multiplier(L1, L1, modulus)
        L1_p = _line_power(L1, L1, modulus)
        
        base = L1
        itera = 1000
        jump = 39

        floor1B = _floor_makerB(base, itera, jump)
        floor1BA = _floor_makerBA(base, itera, jump)
        floor1BB = _floor_makerBB(base, itera, jump)
        floor1BC = _floor_makerBC(base, itera, jump)

        wall1B = _wall_makerB(jump, itera, base)
        wall1BA = _wall_makerBA(jump, itera, base)
        wall1BB = _wall_makerBB(base, itera, jump)
        wall1BC = _wall_makerBC(base, itera, jump)
        
        for x in range(textlen):
            number = ord(text[x]) - 65
            key_number = ord(key[x]) - 65
            output = (key_number + number) % 26
            letter = alphabet[output]
            msg2.append(letter)
        L2 = _line_converter("".join(msg2))
        L2_m = _line_multiplier(L2, L2, modulus)
        L2_p = _line_power(L2, L2, modulus)
        
        base = L2
        itera = 1000
        jump = 39
        
        floor2B = _floor_makerB(base, itera, jump)
        floor2BA = _floor_makerBA(base, itera, jump)
        floor2BB = _floor_makerBB(base, itera, jump)
        floor2BC = _floor_makerBC(base, itera, jump)
        
        wall2B = _wall_makerB(jump, itera, base)
        wall2BA = _wall_makerBA(jump, itera, base)
        wall2BB = _wall_makerBB(base, itera, jump)
        wall2BC = _wall_makerBC(base, itera, jump)
    return msg0, msg1, msg2, L0, L0_m, L0_p, L1, L1_m, L1_p, L2, L2_m, L2_p, modulus, floor0B, floor0BA, floor0BB, floor0BC, floor1B, floor1BA, floor1BB, floor1BC, floor2B, floor2BA, floor2BB, floor2BC, wall0B, wall0BA, wall0BB, wall0BC, wall1B, wall1BA, wall1BB, wall1BC, wall2B, wall2BA, wall2BB, wall2BC

def _double_func_add(alphabet, text):
    textlen = len(text)
    msg = []
    for x in range(textlen):
        number = ord(text[x]) - 65
        output = (number + number) % 26
        letter = alphabet[output]
        msg.append(letter)
    return "".join(msg)

def _double_func_sub(alphabet, text):
    textlen = len(text)
    msg = []
    for x in range(textlen):
        number = ord(text[x]) - 65
        for y in range(number):
            alphabet.append(alphabet.pop(0))
        letter = alphabet[number]
        msg.append(letter)
    return "".join(msg)

def _double_func_sub_sub(alphabet, text):
    textlen = len(text)
    msg = []
    for x in range(textlen):
        number = ord(text[x]) - 65
        output = (number - number) % 26
        letter = alphabet[output]
        msg.append(letter)
    return "".join(msg)

def _path_shift(alphabet, text, s=1):
    textlen = len(text)
    msg = []
    for x in range(textlen):
        number = ord(text[x]) - 65
        for y in range(s):
            alphabet.append(alphabet.pop(0))
        letter = alphabet[number]
        msg.append(letter)
    return "".join(msg)

def _left_shift_beta(alphabet, text, s=1):
    textlen = len(text)
    msg = []
    for x in range(textlen):
        number = ord(text[x]) - 65
        for y in range(s):
            alphabet.insert(0, alphabet.pop(25))
        letter = alphabet[number]
        msg.append(letter)
    return "".join(msg)

def _right_shift_beta(alphabet, text, s=1):
    textlen = len(text)
    msg = []
    for x in range(textlen):
        number = ord(text[x]) - 65
        for y in range(s):
            alphabet.insert(0, alphabet.pop(25))
        letter = alphabet[number]
        msg.append(letter)
    return "".join(msg)

def _right_shift_alpha(alphabet, text, s):
    result = []
    textlen = len(text)
    for x in range(textlen):
        number = ord(text[x]) - 65
        output = (number + s) % 26
        letter = alphabet[output]
        result.append(letter)
    return "".join(result)

def _left_shift_alpha(alphabet, text, s):
    result = []
    textlen = len(text)
    for x in range(textlen):
        number = ord(text[x]) - 65
        output = (number - s) % 26
        letter = alphabet[output]
        result.append(letter)
    return "".join(result)

def _betel_shift_alpha(alphabet, keyword):
    result = []
    textlen = len(keyword)
    shift_order = [1, 9, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0]
    for x in range(11):
        number = ord(keyword[x]) - 65
        output = (number + shift_order[x]) % 26
        letter = alphabet[output]
        result.append(letter)
    return "".join(result)

def _betel_shift_beta(alphabet, keyword):
    result = []
    textlen = len(keyword)
    shift_order = [0, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    for x in range(11):
        number = ord(keyword[x]) - 65
        output = (number - shift_order[x]) % 26
        letter = alphabet[output]
        result.append(letter)
    return "".join(result)

def _betel_shift_gamma(alphabet, keyword):
    result = []
    textlen = len(keyword)
    shift_order = [2, 10, 2, 10, 1, 0, 0, 0, 0, 0, 1]
    for x in range(5):
        number = ord(keyword[x]) - 65
        output = (number - shift_order[x]) % 26
        letter = alphabet[output]
        result.append(letter)
    return "".join(result)

def _betel_shift_omega(alphabet, keyword):
    result = []
    textlen = len(keyword)
    shift_order = [0, 10, 0, 10, 0, 0, 0, 0, 0, 0, 0]
    for x in range(11):
        number = ord(keyword[x]) - 65
        output = (number - shift_order[x]) % 26
        letter = alphabet[output]
        result.append(letter)
    return "".join(result)

def _moon_shift_alpha(alphabet, keyword):
    result = []
    textlen = len(keyword)
    shift_order = [9, 3, 0, 3, 0, 0, 0, 0, 0 , 0, 0]
    for x in range(11):
        number = ord(keyword[x]) - 65
        output = (number + shift_order[x]) % 26
        letter = alphabet[output]
        result.append(letter)
    return "".join(result)

def _moon_shift_beta(alphabet, keyword):
    result = []
    textlen = len(keyword)
    shift_order = [0, 0, 1, 0, 11, 0, 0, 0, 0, 0, 0]
    for x in range(11):
        number = ord(keyword[x]) - 65
        output = (number - shift_order[x]) % 26
        letter = alphabet[output]
        result.append(letter)
    return "".join(result)

def _moon_shift_gamma(alphabet, keyword):
    result = []
    textlen = len(keyword)
    shift_order = [21, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0]
    for x in range(11):
        number = ord(keyword[x]) - 65
        output = (number - shift_order[x]) % 26
        letter = alphabet[output]
        result.append(letter)
    return "".join(result)

def _moon_shift_delta(alphabet, keyword):
    result = []
    textlen = len(keyword)
    shift_order = [0, 9, 0, 11, 0, 0, 0, 0, 0, 0, 0]
    for x in range(11):
        number = ord(keyword[x]) - 65
        output = (number + shift_order[x]) % 26
        letter = alphabet[output]
        result.append(letter)
    return "".join(result)

def _akhu_shift_alpha(alphabet, keyword):
    result = []
    textlen = len(keyword)
    shift_order = [10, 2, 4, 14, 0, 0, 0, 0, 0, 0, 0]
    for x in range(textlen):
        number = ord(keyword[x]) - 65
        output = (number + shift_order[x]) % 26
        letter = alphabet[output]
        result.append(letter)
    return "".join(result)

def _eye_shift_alpha(alphabet, keyword):
    result = []
    textlen = len(keyword)
    shift_order = [16, 6, 12, 0, 0, 0, 0, 0, 0, 0, 0]
    for x in range(textlen):
        number = ord(keyword[x]) - 65
        output = (number + shift_order[x]) % 26
        letter = alphabet[output]
        result.append(letter)
    return "".join(result)

def _eye_shift_beta(alphabet, keyword):
    result = []
    textlen = len(keyword)
    shift_order = [6, 12, 24, 0, 0, 0, 0, 0, 0, 0, 0]
    for x in range(textlen):
        number = ord(keyword[x]) - 65
        output = (number + shift_order[x]) % 26
        letter = alphabet[output]
        result.append(letter)
    return "".join(result)

def _solar_wind_shift(alphabet, keyword):
    result = []
    textlen = len(keyword)
    shift_order = [7, 16, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for x in range(textlen):
        number = ord(keyword[x]) - 65
        output = (number + shift_order[x]) % 26
        letter = alphabet[output]
        result.append(letter)
    return "".join(result)

def _wicca_n_shift(alphabet, keyword):
    result = []
    textlen = len(keyword)
    shift_order = [12, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for x in range(textlen):
        number = ord(keyword[x]) - 65
        output = (number + shift_order[x]) % 26
        letter = alphabet[output]
        result.append(letter)
    return "".join(result)

def _wicca_v_shift(alphabet, keyword):
    result = []
    textlen = len(keyword)
    shift_order = [21, 14, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for x in range(textlen):
        number = ord(keyword[x]) - 65
        output = (number + shift_order[x]) % 26
        letter = alphabet[output]
        result.append(letter)
    return "".join(result)

def _line_converter(line, prefix=None):
    n = []
    if prefix != None:
        n.append(prefix)
    for char in line:
        n.append(str(ord(char) - 65))
    return int("".join(n))

def _line_multiplier(a, b, m):
    return ((a * b) % m)

def _line_power(a, b, m):
    return pow(a, b, m)

def _line_square(a):
    return (a ** a)

def _line_square_mod(a, m):
    return ((a ** a) % m)

def _line_xor(a, m):
    return ((a ^ a))

def _line_add(a, m):
    return ((a + a) & 0xFFFFFFFFFFFFFFFF)

def _line_subtract(a, m):
    return ((a - a) & 0xFFFFFFFFFFFFFFFF)

def _number_to_string(n):
    return str(n)

def _hebew_transformation(alphabet, text, s=1):
    ''' Hebew Transformation '''
    double = _double_func_add(alphabet, text)
    RS = _right_shift_beta(alphabet, double)
    LS = _right_shift_beta(alphabet, RS)
    return double, "".join(RS), "".join(LS)

def _wind_transformation(alphabet, text, s=2):
    ''' Wind Transformation '''
    ''' Untested '''
    double = _double_func_add(alphabet, text)
    RS = _right_shift_beta(alphabet, double)
    LS = _left_shift_beta(alphabet, RS)
    return double, "".join(RS), "".join(LS)

def _radio_transformation(alphabet, text, s=2):
    ''' Venus Radio Transformation '''
    ''' Untested '''
    double = _double_func_add(alphabet, text)
    RS = _right_shift_alpha(alphabet, double, 5)
    LS = _left_shift_alpha(alphabet, RS, 2)
    return double, "".join(RS), "".join(LS)

def _asia_transformation(alphabet, text, s=2):
    ''' Asia Transformation '''
    ''' Untested '''
    double = _double_func_add(alphabet, text)
    RS = _right_shift_alpha(alphabet, double, 5)
    LS = _left_shift_alpha(alphabet, RS, 2)
    return double, "".join(RS), "".join(LS)

def _au_transformation(alphabet, text, s=2):
    ''' Au Transformation '''
    ''' Untested '''
    double = _double_func_add(alphabet, text)
    RS = _right_shift_alpha(alphabet, double, 5)
    LS = _left_shift_alpha(alphabet, RS, 2)
    return double, "".join(RS), "".join(LS)

def _betel_transformation(alphabet, text, s=2):
    ''' Betel Transformation '''
    double = _double_func_add(alphabet, text)
    RS = _right_shift_alpha(alphabet, double, 5)
    LS = _left_shift_alpha(alphabet, RS, 2)
    return double, "".join(RS), "".join(LS)

def _artrax_transformation(alphabet, text, s=2):
    ''' Artax Transformation '''
    ''' Untested '''
    double = _double_func_add(alphabet, text)
    RS = _right_shift_alpha(alphabet, double, 3)
    LS = _left_shift_alpha(alphabet, RS, 2)
    return double, "".join(RS), "".join(LS)

def _wajdet_transformation(alphabet, text, s=2):
    ''' Wajdet Transformation '''
    ''' Untested '''
    double = _double_func_add(alphabet, text)
    triple = _double_func_add(alphabet, double)
    LS = _left_shift_alpha(alphabet, triple, 5)
    RS = _right_shift_alpha(alphabet, LS, 2)
    return double, "".join(RS), "".join(LS)

def _psy_transformation(alphabet, text, s=2):
    ''' Psy Transformation '''
    ''' Untested '''
    double = _double_func_sub_sub(alphabet, text)
    triple = _double_func_sub_sub(alphabet, double)
    RS = _right_shift_alpha(alphabet, triple, 5)
    LS = _left_shift_alpha(alphabet, RS, 2)
    return double, triple, "".join(RS), "".join(LS)

def _betel_heqet_venus_transformation(alphabet, text, s=2):
    ''' Betel Heqet Venus Transformation '''
    double = _double_func_add(alphabet, text)
    triple = _double_func_add(alphabet, double)
    bsA = _betel_shift_alpha(alphabet, double)
    bsB = _betel_shift_beta(alphabet, bsA)
    bsG = _betel_shift_gamma(alphabet, bsB)
    return double, triple, bsB, bsG

def _U_transformation(alphabet, text, s=2):
    ''' U Transformation '''
    double = _double_func_add(alphabet, text)
    triple = _double_func_add(alphabet, double)
    bsA = _betel_shift_alpha(alphabet, double)
    bsB = _betel_shift_beta(alphabet, bsA)
    return double, triple, bsB, bsA

def _moon_transformation(alphabet, text, s=2):
    ''' Moon Transformation '''
    double = _double_func_add(alphabet, text)
    msA = _moon_shift_alpha(alphabet, double)
    msB = _moon_shift_beta(alphabet, msA)
    msG = _moon_shift_gamma(alphabet, msB)
    msD = _moon_shift_delta(alphabet, msG)
    return msA, msB, msD

def _solar_transformation(alphabet, text, s=2):
    ''' Solar Transformation '''
    solarA = _solar_wind_shift(alphabet, text[:2])
    return solarA

def _wicca_transformations(alphabet, text, s=2):
    ''' Wicca Transformations '''
    wiccaN = _wicca_n_shift(alphabet, text[:2])
    wiccaV = _wicca_v_shift(alphabet, text[:2])
    return wiccaN, wiccaV

def _eye_transformations(alphabet, text, s=2):
    eyeA = _eye_shift_alpha(alphabet, text[:3])
    eyeB = _eye_shift_beta(alphabet, text[:3])
    return eyeA, eyeB
    
def _floor_makerB(base, itera=1000, jump=39):
    levels = []
    for x in range(itera):
        i = pow(base, itera, jump)
        levels.append(i)
    return levels

def _floor_makerBA(base, itera=1000, jump=39):
    levels = []
    for x in range(itera):
        i = pow(base, itera, jump)
        levels.append(i)
    return levels

def _floor_makerBB(base, itera=1000, jump=39):
    levels = []
    for x in range(itera):
        i = pow(jump, base, itera)
        levels.append(i)
    return levels

def _floor_makerBC(base, itera=1000, jump=39):
    levels = []
    for x in range(itera):
        i = pow(jump, base, itera)
        levels.append(i)
    return levels

def _wall_makerB(jump=4, itera=1000, base=0):
    if base == 0:
        base += 2
    sides = []
    for x in range(1, itera):
        i = pow(jump, x, base)
        sides.append(i)
    return sides

def _wall_makerBA(jump=39, itera=1000, base=0):
    if base == 0:
        base += 4
    sides = []
    for x in range(1, itera):
        i = pow(base, jump, x)
        sides.append(i)
    return sides

def _wall_makerBB(base, itera=1000, jump=39):
    if base == 0:
        base += 8
    sides = []
    for x in range(1, itera):
        i = pow(base, x, jump)
        sides.append(i)
    return sides

def _wall_makerBC(base, itera=1000, jump=39):
    if base == 0:
        base += 12
    sides = []
    for x in range(1, itera):
        i = pow(base, x, jump)
        sides.append(i)
    return sides

def _run():
    _text_filename = input("Enter filename: ")
    _output_filename = input("Enter output filename: ")
    _modulus = input("Enter modulus number: ")
    _keyword = input("Enter keyword: ")
    n = int(_modulus)
    m = 4
    f = open(_output_filename, "w")
    
    record = Record()
    record.modulus = n
    record.mask = m
    
    record = _file_reader(_text_filename, record)
    alphabet, alphabet_list = _alphabet_generator(n)
    msg0, msg1, msg2, L0, L0_m, L0_p, L1, L1_m, L1_p, L2, L2_m, L2_p, modulus, floor0B, floor0BA, floor0BB, floor0BC,  floor01B, floor01BA, floor01BB, floor01BC,  floor02B, floor02BA, floor02BB, floor02BC, wall00B, wall00BA, wall00BB, wall00BC, wall01B, wall01BA, wall01BB, wall01BC, wall02B, wall02BA, wall02BB, wall02BC = _code_generator(record.text, alphabet, record.keys, m)
    f.write("Egyptian Star Code Generator Report\n")
    f.write("Organized by Uvajda (KryptoMagick)\n")
    f.write("----------------------------------\n\n")
    f.write("phase0: m0: "+str(msg0)+"\n "+"phase0: m1: "+str(msg1)+"\n "+"phase0: m2: "+str(msg2)+"\n")

    f.write("Line0 as an integer: "+str(L0)+"\n")
    f.write("Line1 as an integer: "+str(L1)+"\n")
    f.write("Line2 as an integer: "+str(L2)+"\n")

    f.write("Line0 multiplied: "+str(L0_m)+"\n")
    f.write("Line1 multiplied: "+str(L1_m)+"\n")
    f.write("Line2 multiplied by itself: "+str(L2_m)+"\n")
    
    f.write("Line0 raised to itself: "+str(L0_p)+" modulo line modulus: "+str(modulus)+"\n")
    f.write("Line1 raised to itself: "+str(L1_p)+" modulo line modulus: "+str(modulus)+"\n")
    f.write("Line2 raised to itself: "+str(L2_p)+" modulo line modulus: "+str(modulus)+"\n")
    
    f.write("Line modulus: "+str(modulus)+"\n")

    f.write("Floor0B: "+str(floor0B)+"\n")
    f.write("Floor0BA: "+str(floor0BA)+"\n")
    f.write("Floor0BB: "+str(floor0BB)+"\n")
    f.write("Floor0BC: "+str(floor0BC)+"\n")

    f.write("Floor01B: "+str(floor01B)+"\n")
    f.write("Floor01BA: "+str(floor01BA)+"\n")
    f.write("Floor01BB: "+str(floor01BB)+"\n")
    f.write("Floor01BC: "+str(floor01BC)+"\n")

    f.write("Floor02B: "+str(floor02B)+"\n")
    f.write("Floor02BA: "+str(floor02BA)+"\n")
    f.write("Floor02BB: "+str(floor02BB)+"\n")
    f.write("Floor02BC: "+str(floor02BC)+"\n")

    f.write("Wall00B: "+str(wall00B)+"\n")
    f.write("Wall00BA: "+str(wall00BA)+"\n")
    f.write("Wall00BB: "+str(wall00BB)+"\n")
    f.write("Wall00BC: "+str(wall00BC)+"\n")

    f.write("Floor01B: "+str(floor01B)+"\n")
    f.write("Floor01BA: "+str(floor01BA)+"\n")
    f.write("Floor01BB: "+str(floor01BB)+"\n")
    f.write("Floor01BC: "+str(floor01BC)+"\n")

    f.write("Wall01B: "+str(wall01B)+"\n")
    f.write("Wall01BA: "+str(wall01BA)+"\n")
    f.write("Wall01BB: "+str(wall01BB)+"\n")
    f.write("Wall01BC: "+str(wall01BC)+"\n")

    f.write("Floor02B: "+str(floor02B)+"\n")
    f.write("Floor02BA: "+str(floor02BA)+"\n")
    f.write("Floor02BB: "+str(floor02BB)+"\n")
    f.write("Floor02BC: "+str(floor02BC)+"\n")

    f.write("Wall02B: "+str(wall02B)+"\n")
    f.write("Wall02BA: "+str(wall02BA)+"\n")
    f.write("Wall02BB: "+str(wall02BB)+"\n")
    f.write("Wall02BC: "+str(wall02BC)+"\n")

    msg0, msg1, msg2, L0, L0_m, L0_p, L1, L1_m, L1_p, L2, L2_m, L2_p, modulus, floor1B, floor1BA, floor1BB, floor1BC, floor11B, floor11BA, floor11BB, floor11BC, floor12B, floor12BA, floor12BB, floor12BC,  wall10B, wall10BA, wall10BB, wall10BC, wall11B, wall11BA, wall11BB, wall11BC, wall12B, wall12BA, wall12BB, wall12BC  = _code_generator(msg0, alphabet, msg0, m)
    f.write("phase1: m0: "+str(msg0)+"\n "+"phase0: m1: "+str(msg1)+"\n "+"phase0: m2: "+str(msg2)+"\n")

    f.write("Line0 as an integer: "+str(L0)+"\n")
    f.write("Line1 as an integer: "+str(L1)+"\n")
    f.write("Line2 as an integer: "+str(L2)+"\n")

    f.write("Line0 multiplied: "+str(L0_m)+"\n")
    f.write("Line1 multiplied: "+str(L1_m)+"\n")
    f.write("Line2 multiplied: "+str(L2_m)+"\n")
    
    f.write("Line0 raised to itself "+str(L0_p)+" modulo line modulus: "+str(modulus)+"\n")
    f.write("Line1 raised to itself "+str(L1_p)+" modulo line modulus: "+str(modulus)+"\n")
    f.write("Line2 raised to itself "+str(L2_p)+" modulo line modulus: "+str(modulus)+"\n")

    f.write("Line modulus"+str(modulus)+"\n")

    f.write("Floor1B: "+str(floor1B)+"\n")
    f.write("Floor1BA: "+str(floor1BA)+"\n")
    f.write("Floor1BB: "+str(floor1BB)+"\n")
    f.write("Floor1BC: "+str(floor1BC)+"\n")

    f.write("Wall10B: "+str(wall10B)+"\n")
    f.write("Wall10BA: "+str(wall10BA)+"\n")
    f.write("Wall10BB: "+str(wall10BB)+"\n")
    f.write("Wall10BC: "+str(wall10BC)+"\n")

    f.write("Floor11B: "+str(floor11B)+"\n")
    f.write("Floor11BA: "+str(floor11BA)+"\n")
    f.write("Floor11BB: "+str(floor11BB)+"\n")
    f.write("Floor11BC: "+str(floor11BC)+"\n")

    f.write("Wall11B: "+str(wall11B)+"\n")
    f.write("Wall11BA: "+str(wall11BA)+"\n")
    f.write("Wall11BB: "+str(wall11BB)+"\n")
    f.write("Wall11BC: "+str(wall11BC)+"\n")

    f.write("Floor12B: "+str(floor12B)+"\n")
    f.write("Floor12BA: "+str(floor12BA)+"\n")
    f.write("Floor12BB: "+str(floor12BB)+"\n")
    f.write("Floor12BC: "+str(floor12BC)+"\n")

    f.write("Wall12B: "+str(wall12B)+"\n")
    f.write("Wall12BA: "+str(wall12BA)+"\n")
    f.write("Wall12BB: "+str(wall12BB)+"\n")
    f.write("Wall12BC: "+str(wall12BC)+"\n")

    msg0, msg1, msg2, L0, L0_m, L0_p, L1, L1_m, L1_p, L2, L2_m, L2_p, modulus, floor2B, floor2BA, floor2BB, floor2BC, floor21B, floor21BA, floor21BB, floor21BC, floor22B, floor22BA, floor22BB, floor22BC, wall20B, wall20BA, wall20BB, wall20BC, wall21B, wall21BA, wall21BB, wall21BC, wall22B, wall22BA, wall22BB, wall22BC = _code_generator(msg0, alphabet, msg0, m)
    
    f.write("Line0 as an integer: "+str(L0)+"\n")
    f.write("Line1 as an integer: "+str(L1)+"\n")
    f.write("Line2 as an integer: "+str(L2)+"\n")

    f.write("Line0 multiplied: "+str(L0_m)+"\n")
    f.write("Line1 multiplied: "+str(L1_m)+"\n")
    f.write("Line2 multiplied: "+str(L2_m)+"\n")
    
    f.write("Line0 raised to the power of the line modulus: "+str(L0_p)+"\n")
    f.write("Line1 raised to the power of the line modulus: "+str(L1_p)+"\n")
    f.write("Line2 raised to the power of the line modulus: "+str(L2_p)+"\n")

    f.write("phase2: m0: "+str(msg0)+"phase0: m1: "+str(msg1)+"phase0: m2: "+str(msg2)+"\n")
    
    f.write("Line0 as an integer: "+str(L0)+"\n")
    f.write("Line1 as an integer: "+str(L1)+"\n")
    f.write("Line2 as an integer: "+str(L2)+"\n")

    f.write("Line0 multiplied by itself: "+str(L0_m)+"\n")
    f.write("Line1 multiplied by itself: "+str(L1_m)+"\n")
    f.write("Line2 multiplied by itself: "+str(L2_m)+"\n")
    
    f.write("Line0 raised to itself: "+str(L0_p)+" modulo line modulus: "+str(modulus)+"\n")
    f.write("Line1 raised to itself: "+str(L1_p)+" modulo line modulus: "+str(modulus)+"\n")
    f.write("Line2 raised to itself: "+str(L2_p)+" modulo line modulus: "+str(modulus)+"\n")
    
    f.write("Line modulus: "+str(modulus)+"\n")

    f.write("Floor2B: "+str(floor2B)+"\n")
    f.write("Floor2BA: "+str(floor2BA)+"\n")
    f.write("Floor2BB: "+str(floor2BB)+"\n")
    f.write("Floor2BC: "+str(floor2BC)+"\n")

    f.write("Wall20B: "+str(wall20B)+"\n")
    f.write("Wall20BA: "+str(wall20BA)+"\n")
    f.write("Wall20BB: "+str(wall20BB)+"\n")
    f.write("Wall20BC: "+str(wall20BC)+"\n")

    f.write("Floor21B: "+str(floor21B)+"\n")
    f.write("Floor21BA: "+str(floor21BA)+"\n")
    f.write("Floor21BB: "+str(floor21BB)+"\n")
    f.write("Floor21BC: "+str(floor21BC)+"\n")

    f.write("Wall21B: "+str(wall21B)+"\n")
    f.write("Wall21BA: "+str(wall21BA)+"\n")
    f.write("Wall21BB: "+str(wall21BB)+"\n")
    f.write("Wall21BC: "+str(wall21BC)+"\n")

    f.write("Floor22B: "+str(floor22B)+"\n")
    f.write("Floor22BA: "+str(floor22BA)+"\n")
    f.write("Floor22BB: "+str(floor22BB)+"\n")
    f.write("Floor22BC: "+str(floor22BC)+"\n")

    f.write("Wall22B: "+str(wall22B)+"\n")
    f.write("Wall22BA: "+str(wall22BA)+"\n")
    f.write("Wall22BB: "+str(wall22BB)+"\n")
    f.write("Wall22BC: "+str(wall22BC)+"\n")

    path0 = _path_shift(list(alphabet_list), msg0)
    f.write("path0: :"+path0+"\n")
    path1 = _path_shift(list(alphabet_list), msg1)
    f.write("path1: :"+path1+"\n")
    path2 = _path_shift(list(alphabet_list), msg2)
    f.write("path2: :"+path2+"\n")
    double_msg0 = _double_func_add(list(alphabet_list), msg0)
    f.write("double + :"+double_msg0+"\n")
    double_msg1 = _double_func_sub(list(alphabet_list), msg1)
    f.write("double - :"+double_msg1+"\n")
    wiccaN, wiccaV = _wicca_transformations(list(alphabet_list), _keyword)
    f.write("Wicca Transformations: "+wiccaN+" "+wiccaV+"\n")
    moonB, moonA, moonG = _moon_transformation(list(alphabet_list), _keyword)
    f.write("Moon Transformations: "+moonB+" "+moonA+" "+moonG+"\n")
    eyeA, eyeB = _eye_transformations(list(alphabet_list), _keyword)
    f.write("Eye Transformations: "+eyeA+" "+eyeB+"\n")
    solarA = _solar_transformation(list(alphabet_list), _keyword)
    f.write("Solar Transformation: "+solarA+"\n")
    hebewD, hebewB, hebewA = _hebew_transformation(list(alphabet_list), msg0)
    f.write("Hebew Delta: "+hebewD+"\n")
    f.write("Hebew Transformations: "+hebewB+hebewA+"\n")
    betelD, betelB, betelA = _betel_transformation(list(alphabet_list), msg0)
    f.write("Betel Delta: "+betelD+"\n")
    f.write("Betel Transformations: "+betelB+" "+betelA+"\n")
    betelHeqetVenusD, betelHeqetVenusT, betelHeqetVenusB, betelHeqetVenusA = _betel_heqet_venus_transformation(list(alphabet_list), _keyword)
    f.write("Betel Heqet Venus Delta: "+betelHeqetVenusD+"\n")
    f.write("Betel Heqet Venus T: "+betelHeqetVenusT+"\n")
    f.write("Betel Heqet Venus Transformations: "+betelHeqetVenusB+" "+betelHeqetVenusA+"\n")

_run()
