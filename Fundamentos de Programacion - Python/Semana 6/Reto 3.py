


def traductor_a_espanol(mensaje_a_traducir):
    diccionario_morse = {'/': ' ', '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.':
                            'E', '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---':
                             'J', '-.-': 'K', '.-..':'L', '--': 'M', '-.': 'N', '---': 'O',
                         '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
                         '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z'}
    lista_mensaje = mensaje_a_traducir.split()
    mensaje_traducido = ''
    for i in lista_mensaje:
        mensaje_traducido = mensaje_traducido + diccionario_morse.get(i)


    return mensaje_traducido


mensaje = traductor_a_espanol('.... . -- --- ... / . -. -.-. --- -. - .-. .- -.. --- / ..- -. .- / .--. .-.. .- -. - .- / -. ..- -. -.-. .- / .- -. - . ... / ...- .. ... - .-')
print(mensaje)


