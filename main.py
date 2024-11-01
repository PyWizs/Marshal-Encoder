#Created By PyWiz
#Github: https://github.com/PyWizs/Marshal-Encoder


import os,marshal,time,random
try: from colorama import init
except: os.system('pip install colorama'); from colorama import *

init()

r = '\033[1;31m'
g = '\033[0;37m'
y = '\033[1;33m'
w = '\033[1;37m'
gr = '\033[0;32m'

def banner(): print(f"""
{w}──{r}▒▒▒▒▒▒{w}─
─{r}▒─{w}▄{r}▒─{w}▄{r}▒{w}─
{w}─{r}▒▒▒▒▒▒▒{w}─
{w}─{r}▒▒▒▒▒▒▒{w}─
{w}─{r}▒{w}─{r}▒{w}─{r}▒{w}─{r}▒{w}─
""")
    
def clear():
    if(os.name == 'posix'):
        os.system('clear')
    else:
        os.system('cls')
clear()
banner()
file_path = input(f"{g}[{r}!{g}] {w}Enter Python3 File Path {g}( {r}Example {g}: {r}src/main.py {g}) :{w} ")
clear()

if '.py' not in file_path: banner(); print(f"{g}[{r}-{g}] {w}Please Enter Python File{r}!"); exit()
else:
    try: file = open(file_path,'r', encoding="utf8").read()
    except IOError: banner(); print(f"{g}[{r}-{g}] {w}No Such File Or Directory"); exit()

try: compiled_file = compile(file,'','exec'); encoded_code = marshal.dumps(compiled_file)
except TypeError: banner(); print(f"{g}[{r}-{g}] {w}File Already Compiled{r}!!!"); exit()

name = file_path.replace(".py","")
open(f"{name}_Encoded.py","w", encoding="utf8").write(f"""
# ─────▄───▄
# ─▄█▄─█▀█▀█─▄█▄
# ▀▀████▄█▄████▀▀
# ─────▀█▀█▀
# ♦ PyWiz
# • Github: https://github.com/PyWizs/Marshal-Encoder

import marshal
exec(marshal.loads({repr(encoded_code)}))
""")

print(f"""
{w}───{y}▄████▄
{w}──{y}███▄█▀
{w}─{y}▐████{w}──{y}█{w}─{y}█
{w}──{y}█████▄
{w}───{y}▀████▀

{g}[{gr}+{g}] {w}Encoded File Saved: {r}{name}_Encoded.py
""")
