import hangman
import reversegam
import tictactoeModificado
import PySimpleGUI as gui
import time
import json



def guardar_usuario(usr):

	try:
		with open ("historialUsuarios.json",'r+', encoding='UTF-8') as a:
			usuarios = a.read()
			json.dump(usr, a, indent= 3 )

	except FileNotFoundError:
		with open("historialUsuarios.json", 'w', encoding='UTF-8') as a:
			json.dump(usr,a ,indent=3)

def main(args):
	
	sigo_jugando = True
	while sigo_jugando:
		


		layout = [[gui.Text('Menu de Juegos')],
				  [gui.Text('usuario:'), gui.InputText(size=(10, 50), key='usuario')],
				  [gui.Button(button_text='Ahoracado', key='ahorcado')],
				  [gui.Button(button_text='TA-TE-Ti', key='tateti')],
					[gui.Button(button_text='otello', key='otello')],
					[gui.Button(button_text='Salir', key='salir')]
		]

		window = gui.Window('Juegos', layout)
		window.Finalize()
		event, value = window.read()

		if value  != None :
			#usr = {value['usuario']:[event, time.time()]}
			usr = {'usr' :value['usuario'], 'juego':event, 'fecha': time.ctime(time.time())}

		if event == 'ahorcado':
			window.close()

			guardar_usuario(usr)
			hangman.main()
			sigo_jugando = False
		elif event == 'tateti':
			window.close()
			guardar_usuario(usr)
			tictactoeModificado.main()

			sigo_jugando = False

		elif event == 'otello':
			window.close()
			guardar_usuario(usr)
			reversegam.main()
			sigo_jugando = False

		elif event == 'salir' :
			sigo_jugando = False
			window.close()
	window.close()

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
