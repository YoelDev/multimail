# -*- coding: utf-8 -*-
# Version Tool -> 0.0.1
# Written by: * Yoel Manrique - yoeldev
# Venezuela
# https://github.com/yoeldev

import sys, smtplib, os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase

BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, END = '\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[1;35m', '\033[1;32m', '\033[0m'

sprint = "_".center(44, "_")
sprinte = "+".center(44,"+")

def header():
    sys.stdout.write(YELLOW + '''
 /$$      /$$ /$$   /$$ /$$    /$$$$$$$$ /$$$$$$ /$$      /$$  /$$$$$$  /$$$$$$ /$$      '''+ GREEN +'''['''+ RED+'''PARA USO UNICAMENTE DE APRENDIZAJE'''+ GREEN +''']'''+ YELLOW +'''
| $$$    /$$$| $$  | $$| $$   |__  $$__/|_  $$_/| $$$    /$$$ /$$__  $$|_  $$_/| $$      ''' + GREEN +'''           [''' + YELLOW+ '''VEN'''+ BLUE+'''EZU'''+ RED+'''ELA''' + GREEN+''']             '''+ YELLOW+'''
| $$$$  /$$$$| $$  | $$| $$      | $$     | $$  | $$$$  /$$$$| $$  \ $$  | $$  | $$      '''+ GREEN+'''   [-->'''+RED+'''MULTIMAIL'''+MAGENTA+'''['''+RED+'''V0.0.1'''+MAGENTA+''']'''+ GREEN+'''<--]'''+ YELLOW +'''
| $$ $$/$$ $$| $$  | $$| $$      | $$     | $$  | $$ $$/$$ $$| $$$$$$$$  | $$  | $$      '''+ MAGENTA +''' https://github.com/YoelDev/multimail '''+ YELLOW +'''
| $$  $$$| $$| $$  | $$| $$      | $$     | $$  | $$  $$$| $$| $$__  $$  | $$  | $$      
| $$\  $ | $$| $$  | $$| $$      | $$     | $$  | $$\  $ | $$| $$  | $$  | $$  | $$      '''+ GREEN +''' Importante leer archivo readme para saber'''+ YELLOW +'''
| $$ \/  | $$|  $$$$$$/| $$$$$$$$| $$    /$$$$$$| $$ \/  | $$| $$  | $$ /$$$$$$| $$$$$$$$    '''+ GREEN +''' como utilizar la herramienta'''+ YELLOW +'''
|__/     |__/ \______/ |________/|__/   |______/|__/     |__/|__/  |__/|______/|________/                
''' + RED + '''      [ Disclaimer Alert ]''' + YELLOW +  ''' 
''' + BLUE + '''->'''+ WHITE +'''No me hago responsable del uso''' + BLUE +'''<-''' + YELLOW + '''
''' + BLUE + '''------>''' + WHITE +'''que se le pueda dar''' + BLUE +'''<------ ''' + YELLOW + '''
''' + BLUE + ''' ----->'''+ WHITE +'''Uso etico no ilegal'''+ BLUE +'''<-----  ''' + YELLOW + '''
''' + MAGENTA + '''-----------------------------------''' + YELLOW +  ''' 
''' + RED + '''    [ El Aprendizaje es libre ]''' + YELLOW +  '''
''' + WHITE + ''' Usar unicamente para ''' + RED + ''' TRABAJO''' + WHITE + ''' o ''' + RED + '''EDUCACIÓN''' + WHITE + ''' !
''' + MAGENTA + sprint + "\n")
    input(YELLOW + 'Presiona ['+ RED +'Enter'+ YELLOW +'] para continuar...')


def input_text():
    os.system('clear')
    print(RED + "RECUERDE ASEGURARSE QUE EL CORREO EXISTE".center(44,"+"))
    mail = ""
    passw = 0
    check = ""
    mail = input(BLUE + "[Por favor ingrese su correo]: " + RED)
    passw = input(BLUE + "[Por favor ingrese la clave de su correo]: " + RED)
    print(YELLOW + sprint + "\n")
    print(BLUE + "¿Estas credenciales son correctas?")
    print("[" + GREEN + "User" + BLUE +"] " +GREEN+mail)
    print(BLUE +"[" + GREEN + "Password" + BLUE +"] " +GREEN+passw)
    print("\n"+BLUE + "[De ser correcta presione introduzca "+ RED+"Y"+BLUE +" de lo contrario "+ RED +"N"+BLUE+"] ")
    check = input().lower()
    if check == "y":
        enviar_correo(mail,passw)
    elif check == "n":
        return input_text()
    else:
        print(RED + "[Entrada erronea abortando]")
        return main() 
    print(RED + "[MAIL ENVIADO]".center(44,"+"))

def enviar_correo(mail,passw):
    amail = mail
    apassw =  passw
    select = input(BLUE + "[Por favor ingrese el metodo de envio a utilizar-> "+ RED+"S"+BLUE +" envio a un unico mail / "+ RED+"M"+BLUE +" envio a multiples mails]: " + RED.lower())
   
    if select == "s":
        vmail = input(BLUE + "[Por favor ingrese el correo a enviar el mail]: " + RED)
    elif select == "m":
        vmail = input(BLUE + "[Al ingresar los correos asegurese de separarlos unicamente con una coma sin espacios]: \n" + RED)

    else:
        
        return enviar_correo(mail,passw)

    masunto = input(BLUE + "[Por favor ingrese el asunto]: " + RED)
    mmensaje = input(BLUE + "[Por favor ingrese el mensaje]: " + RED)
    csend = input(BLUE + "[Por favor ingrese la cantidad de mensajes a enviar]: " + RED)
    csendm = int(csend)

    #Cabecera del mail
    msg = MIMEMultipart()
    mensaje = mmensaje
    msg['From'] = amail
    msg['To'] = vmail
    msg['Subject'] = masunto
    msg.attach(MIMEText(mensaje, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com: 587')
    server.starttls()
    server.login(amail, apassw)
    for e in range(csendm):
        server.sendmail(msg['From'], msg['To'].split(","), msg.as_string())
    server.quit()
    


def main():
    header()
    input_text()

if __name__ == "__main__":
    main()
