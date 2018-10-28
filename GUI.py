try:
	import tkinter
except:
	import tkinter as Tkinter
import time


# Configurations
WIDTH=330		# Set Width Of Widget
HEIGHT=300		# Set Height
LOOP_TURN=100	# Update Loop Turns
LOOP_WAIT=0.2	# Time For Waiting On Every Loop Turn

class GUI(tkinter.Tk):
	def __init__(self, DATAVALUE):
		tkinter.Tk.__init__(self)
		self.DATAVALUE=DATAVALUE
		self.main_function_handler()

	# Creating Function for Handling Other Functions
	def main_function_handler(self):
		self.creating_function_for_appereance()
		self.coordinate_position()
		self.creating_canvas_board()
		self.creating_Gui_valiadilty()
		return

	# Creating Function For Showing Data
	def creating_canvas_board(self):
		canvas=tkinter.Canvas(self,bg='skyblue')
		canvas.create_text(50,10,text=''.join(self.DATAVALUE.pop('temperature')), font=('arial 100 bold'),anchor='nw', fill='gray5') # Temperature
		canvas.create_text(130,150,text=''.join(self.DATAVALUE.pop('next summary').upper()), font=('arial 10 bold'),fill='Blue') # Next Summary
		for i,j in enumerate(self.DATAVALUE.items()):
			num=i
			(label,value)=j
			canvas.create_text(50,180+(20*i),text='{}'.format(label.upper()), font=('arial 10 italic'),anchor='nw', fill='gray10')
			canvas.create_text(150,180+(20*i),text='{}'.format(value), font=('arial 10 italic'),anchor='nw', fill='gray20')
		canvas.pack(expand='yes',fill='both')
		return

	# Close Function
	def close_widget(self):
		self.destroy()
		return

	# Function For Handling GUI Apperance Style
	def creating_function_for_appereance(self):
		self.focus_force()
		self['bg']='gray'
		self.overrideredirect(True)
		return

	# Function Fon Handling GUI Position
	def coordinate_position(self):
		self.geometry("%dx%d+%d+%d" % (WIDTH,HEIGHT,\
			self.winfo_screenwidth()/1.5-(WIDTH/1.5),\
			self.winfo_screenheight()/1-(HEIGHT),\
			))

	# Function For Handling GUI Loop Timing
	def creating_Gui_valiadilty(self):
		x=1.0
		for i in range(LOOP_TURN):
			time.sleep(LOOP_WAIT)
			self.update_idletasks()
			self.update()
			self.attributes('-alpha',x)
			x=x-0.01
		self.destroy()
		return


# Main Trigger
if __name__ == '__main__':
	# This Data Is only For Testing GUI
	DATAVALUE={'next summary': '                Clear throughout the\xa0day.      ', 'temperature': '21\u02da', 'Humidity:': '25%', 'Rain': '0mm', 'Visibility:': '10+km', 'Wind:': '5kph\u2191', 'UV Index:': '8', 'Pressure:': '1016hPa', 'summary': 'Clear.', 'Dew Pt:': '0\u02da'}
	# Starting GUI Function
	GUI(DATAVALUE)
