from pyfiglet import Figlet


title = Figlet(font='doom').renderText('HANGMAN GAME')
stage = """

//================]
||                |
||                |
||                |
||
||
||
||
||
||
||
||
||
############+========####
##                     ##
##                     ##
"""


def run() -> None:
    print(title, stage, sep='\n')


if __name__ == '__main__':
    run()