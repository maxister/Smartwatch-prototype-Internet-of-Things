import machine,time

MorseCode = {'A':'.-','B':'-...','C':'-.-.','D':'-..','E':'.','F':'..-.','G':'--.',
    'H':'....','I':'..','J':'.---','K':'-.-','L':'.-..','M':'--','N':'-.',
    'O':'---','P':'.--.','Q':'--.-','R':'.-.','S':'...','T':'-','U':'..-',
    'V':'...-','W':'.--','X':'-..-','Y':'-.--','Z':'--..',
    '0':'-----','1':'.----','2':'..---','3':'...--','4':'....-',
    '5':'.....','6':'-....','7':'--...','8':'---..','9':'----.',
    '.':'.-.-.-',
    ',':'--..--',
    '?':'..--..',
    '/':'--..-.',
    '@':'.--.-.',
}

def blink(led,t,unit):
    led.value(0)
    time.sleep(t)
    led.value(1)
    time.sleep(unit)
    return

def morse(msg,pin,tdot,m):
    led = machine.Pin(pin,machine.Pin.OUT)

    tdash = tdot * 3

    for i in range(m):
        for l in msg:
            c = MorseCode.get(l.upper())
            for e in c:
                if e == ".": blink(led, tdot, tdot)
                if e == "-": blink(led, tdash, tdot)
        time.sleep(tdot*6)
    renturn

morse('SOS',2,0.1,10)

