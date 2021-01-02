import tkinter
import tkinter.messagebox as mb
def main():
	top = tkinter.Tk()
	top.withdraw()
	while True:
		choice = getMenuChoice(menu)
		executeChoice(choice)
def playGame(game):
	result = ""
	while not result:
		printGame(game)
		choice = input("Cell[1-9 or q to quit]:")
		if choice.lower()[0] == 'q':
			save = mb.askyesno("Save game","Save game before quitting?")
			if save:
				tic_tac_toe_logic.saveGave(game)
			quit()
		else:
			try:
				cell = int(choice)-1
				if not (0 <= cell <= 8):
					raise ValueError
			except ValueError:
				print("Choose a number or 'q' to quit")
				continue
			try:
				result = tic_tac_toe_logic.userMove(game,cell)
			except ValueError:
				mb.showerror("Invalid cell","Choose an empty cell")
				continue
			if not result:
				result = tic_tac_toe_logic.computerMove(game)
			if not result:
				continue
			elif result == 'D':
				printGame(game)
				mb.showinfo("Result","It's a draw")
			else:
				printGame(game)
				mb.showinfo("Result","Winner is {}".format(result))


	









	
	
