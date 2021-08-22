from tkinter import Event, font
import PySimpleGUI as sg
import random
from PySimpleGUI.PySimpleGUI import Input, Output
import time

class App_forca:
    """
    Jogo da forca
    Desafia o usuário a adivinhar uma palavra secreta, chutando uma letra de cada vez

    returns:
    FUN
    No params needed
    """
    
    def __init__(self):

        palavras = ['Amarelo','Amiga','Amor','Aviao','Balao','Bebe','Bolo','Branco','Cama','Caneca','Celular','Clube','Copo','Doce','Elefante','Escola','Estojo','Faca','Foto','Garfo','Geleia','Girafa','Janela','Limonada','Meia','Noite','Oculos','onibus','Parque','Passarinho','Peixe','Pijama','Rato','Umbigo','Afobado','Amendoim','Banheiro','Caatinga','Cachorro','Campeonato','Capricornio','Catapora','Crepusculo','Empregado','Esparadrapo','Forca','Galaxia','Historia','Magenta','Manjericao','Menta','Moeda','Palavra','Pedreiro','Pneumonia','Pulmao','Rotatoria','Serenata','Transeunte','Trilogia','Xicara','loucura','skate','edificio','Acender','Afilhado','Ardiloso','Aspero','Asterisco','Basquete','Caminho','Champanhe','Chiclete','Chuveiro','Coelho','Contexto','Convivencia','Desalmado','Eloquente','Esfirra','Esquerdo','Exceção','Fugaz','Gororoba','Heterossexual','Horrorizado','Impacto','Independencia','Modernidade','Oftalmologista','Otorrinolaringologista','Paralelepipedo','Pororoca','Prognosticio','Quarentena','Quimera','Reportagem','Sino','Taciturno','Tenue','Visceral']
        
        sg.change_look_and_feel('DarkBlue')
        self.vidas = 6
        self.palavra_sorteada = random.choice(palavras).upper()
        self.erros = []
        self.apresentacao = """Bem Vindo!

Você tem 6(seis) vidas para descobrir a PALAVRA SECRETA
Digite seu palpite(uma letra por vez)
A cada erro, você perdera uma vida
Se acabarem as vidas, o jogo acaba e você perde
Se você acertar todas as letras antes de ficar sem vidas, você vence.
BOA SORTE!!!"""
        # lauout
        self.layout = [
            [sg.Image('hangman.png', size=(200,200),pad=(5,5))],
            [sg.Text(self.apresentacao.upper(),font='Fixedsys  10' ,size=(70,8), key='boas_vindas')],
            [sg.Text(f'A PALAVRA SECRETA POSSUI {len(self.palavra_sorteada)} LETRAS', font='Fixedsys  10' ,size=(40,0))],
            [sg.Text('DIGITE SEU PALPITE',font='Fixedsys  10' ,size=(20,0)),sg.Input(size=(2,0),do_not_clear=False, key='palpite')],
            [sg.Button('JOGAR',bind_return_key=True)],
            [Output(size=(70,10),font='Comic 15')]
        ]
         
    def status(self,palavra_sorteada, acertos,vidas):
        display = []
        for letra in palavra_sorteada:
            if letra in acertos:
                display.append(letra)
            else:
                display.append('*')
        resposta = str(display).replace('[','').replace(']','').replace("'",'').replace(',','').replace(' ','')
        print("""Vidas: {}
{}   
PALAVRA: {}
{}
ERROS: {}
{}
    """.format(vidas,('-'*50), str(display).replace('[','').replace(']','').replace("'",'').replace(',','').upper(),('-'*50),str(self.erros).replace('[','').replace(']','').replace("'",'').replace(',',' -').upper(),('-'*50)))
        return resposta
    
    def play(self):
        """
        Roda o jogo

        no params needed
        """
        play_check_op = ('S','N')        
        acertos = []
        window = sg.Window('JOGO DA FORCA').layout(self.layout)
        
        
        
        while True:
            if self.vidas > 0:
                resposta = self.status(self.palavra_sorteada, acertos,self.vidas)
                if resposta.upper() != self.palavra_sorteada:
                    self.button, self.values = window.read()
                    
                    palpite = self.values['palpite']
                    if palpite.isalpha() and len(palpite)==1:
                        if palpite.upper() not in acertos and palpite.upper() not in self.erros:
                            if palpite.upper() in self.palavra_sorteada:
                                acertos.append(palpite.upper())
                            else:
                                self.erros.append(palpite.upper())
                                self.vidas -= 1
                        else:
                            print('\n'+f'Letra {palpite.upper()} já utilizada...digite um novo palpite'+'\n')
                    else:
                        print('\n'+'Digite apenas letras, uma por vez. '+'\n' )
                else:
                    print('\n'+ "Parabens você venceu!!!"+'\n')
                    print('Gostaría de jogar novamente? S/N ')
                    self.button, self.values = window.read()
                    play_check = self.values['palpite']
                    if play_check.upper() in play_check_op:
                        if play_check.upper() != 'N':
                            window.close(); del window
                            self.__init__()
                            self.play()
                        else:
                            print('Bye-bye!')
                        time.sleep(3)
                        window.close(); del window
                        break
                    else:
                        print("DIGITE APENAS 'S' OU 'N' ")
                        time.sleep(3)
            else:
                print('\n' + f'Você perdeu! Mais sorte na próxima vez. A palavra secreta era {self.palavra_sorteada.upper()}' + '\n')
                print('Gostaría de jogar novamente S/N ')
                self.button, self.values = window.read()
                play_check = self.values['palpite']
                if play_check.upper() in play_check_op:
                    if play_check.upper() != 'N':
                        window.close(); del window 
                        self.__init__()
                        self.play()
                    else:
                        print('Bye-bye!')
                        time.sleep(3)
                        window.close(); del window
                        break
                else:
                        print("DIGITE APENAS 'S' OU 'N' ")
                        time.sleep(3)    
        window.close(); del window


if __name__=='__main__':
    App_forca().play()
    