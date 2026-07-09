#!/usr/bin/python3
""" Copyright© 2023-2026 OpenSoftware-World
OpenSoftware-World Calculator Tüm Hakları GPL(Genel Kamu Lisansı) altında korunmaktadır.
OpenSoftware-World Calculator All Rights Reserved under the GPL(General Public License).
Bu Yazılımın Bir Kopyası GitHub da yayınlanmaktadır Görüntülemek için: https://github.com/OpenSoftware-World/OpenSoftware-World-Calculator
A Copy of This Software is published on GitHub To view: https://github.com/OpenSoftware-World/OpenSoftware-World-Calculator """

import os, platform
from Lib.Basic_Maths.Basic_Maths import *
from Lib.PyAppDevKit.pyappdevkit import *
from Lang.lang import *

while True:
    print("*********************************************************************")
    if lang == "tr" or lang == "TR":
        print("*** {0}     ***". format(welcome_msg))
        print("""*** {0}                                                   ***
***                                                               ***
*** {1}                          ***""". format(process_list,process_list_msg))
    elif lang == "en" or lang == "EN":
        print("*** {0}         ***". format(welcome_msg))
        print("""*** {0}                                                      ***
***                                                               ***
*** {1}                       ***""". format(process_list,process_list_msg))
    else:
        print("Invalid Language!")
    print("""***                                                               ***
*** 1. calc                                                       ***
*** 2. about                                                      ***                     
*** 3. exit                                                       ***                      
*** 4. help                                                       ***
*** 5. git-address                                                ***                              
*** 6. ver                                                        ***          
*** 7. licence                                                    ***                                  
*** 8. Thank                                                      ***                                    
*********************************************************************""")
    command=str(input("calc> "))
    if platform.system() == "Linux" or platform.system() == "Darwin":
        os.system("clear")
    elif platform.system() == "Windows":
        os.system("cls")
    else:
        pass
    selected_process=str(slctd_prcs)

    if command == "1" or command == "calc":
        print("""*** {0}     ***
         {1}={2}""". format(command_calc_txt,slctd_prcs_msg,selected_process))
        print("""
        1.   {0}
        2.   {1}
        3.   {2}
        4.   {3}
        5.   {4}
        6.   {5}""". format(add,ext,mul,div,per,mod))
        process=str(input("{0}". format(usr_input)))
        selected_process=process
        os.system("clear")
        print("""calc> {0}: 
         {1}={2}""". format(command_calc_txt,slctd_prcs_msg,selected_process))
        n1=float(input(usr_input_n1))
        n2=float(input(usr_input_n2))
        if platform.system() == "Linux" or platform.system() == "Darwin":
            os.system("clear")
        elif platform.system() == "Windows":
            os.system("cls")
        else:
            pass

        if process == "1" or process == "addition" or process == "Addition" or process == "toplama" or process == "Toplama" or process == "add":
            Addition(n1,n2,"",save_cfg=OFF,file_name="",save_err_msg="")
        elif process == "2" or process == "extraction" or process == "Extraction" or process == "çıkarma" or process == "Çıkarma" or process == "ext":
            Extraction(n1,n2,"",save_cfg=OFF,file_name="",save_err_msg="")
        elif process == "3" or process == "multiplication" or process == "Multiplication" or process == "çarpma" or process == "Çarpma" or process == "mul":
            Multiplication(n1,n2,"",save_cfg=OFF,file_name="",save_err_msg="")
        elif process == "4" or process == "division" or process == "Division" or process == "bölme" or process == "Bölme" or process == "div":
            Division(n1,n2,"",div_err,save_cfg=OFF,file_name="",save_err_msg="")
        elif process == "5" or process == "percentage" or process == "Percentage" or process == "yüzde hesaplama" or process == "Yüzde Hesaplama" or process == "per":
            Percentage(n1,n2,"",save_cfg=OFF,file_name="",save_err_msg="")
        elif process == "6" or process == "mod" or process == "Mod" or process == "mod alma" or process == "Mod Alma" or process == "mod":
            Mod(n1,n2,"",save_cfg=OFF,file_name="",save_err_msg="")
        else:
            error_msg(error_dialog,"","")
    elif command == "2" or command == "about" or command == "About" or command == "hakkında" or command == "Hakkında" or command == "info" or command == "Info":
            print("OpenSoftware-World-Calculator CLI(Command Line Interface) LICENCE=GPL2")
    elif command == "3" or command == "exit" or command == "Exit" or command == "çıkış" or command == "Çıkış" or command == "quit" or command == "Quit":
        all_exit(dialog_switch=OFF,lang=lang,ExitSelectDialog="",userTimeDialog="",exitDialog="",errormsgDialog="",unit="")
    elif command == "4" or command == "help" or command == "Help" or command == "yardım" or command == "Yardım":
        print("OpenSoftware-World-Calculator 2.3")
        print("\n Command: calc , about , help , exit , git-address , web-site , ver , licence , Thank")
        print("\nhttps://opensoftware-world.com/Documents/OpenSoftware-World-Calculator/2.3/OpenSoftware-World_calculator_doc.html")
    elif command == "5" or command == "git-address" or command == "Git-Address" or command == "git adresi" or command == "Git Adresi":
        print("GitHub Link: https://github.com/OpenSoftware-World/OpenSoftware-World-Calculator")
    elif command == "6" or command == "web-site" or command == "Web-Site" or command == "web sitesi" or command == "Web Sitesi":
        print("https://opensoftware-world.com")
    elif command == "7" or command == "ver" or command == "Ver" or command == "version" or command == "Version":
        print(ver_msg)
    elif command == "8" or command == "licence" or command == "Licence" or command == "lisans" or command == "Lisans":
        print(licence_msg)
    elif command == "9" or command == "thank" or command == "Thank" or command == "teşekkür" or command == "Teşekkür":
        print(thank)
    else:
        error_msg(error_dialog,"","")