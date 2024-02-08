This repository is a BMI calculator app. 

Original: https://www.youtube.com/watch?v=mop6g-c5HEY&t=45995s

New things I learned:

1. Tracing: Tkinter provides a way to trace changes to a variable. It would either trace Write 'w' or Read 'r' a variable and run a function when it does.

Ex: self.height_int.trace('w', self.update_bmi)

When the height on the app is updated (writing), it will run the function to update the BMI.

Note: When you use this trace, the function needs to have *args in its parameters.

Ex: 

- def change_units(self, *args):
    self.height_input.update_text(self.height_int.get())
    self.weight_input.update_weight()

2. divmod(x,y): python built-in function used to get the quotient (x), and the remainder(y)

Ex): pounds, ounces = divmod(raw_ounces, 16)

this function is dividing raw_ounces by 16 and stores the quotient in the pounds and remainder in ounces.

3. bind() function in Tkinter: this function is used to handle specific events in a customized way that isnt directly related to normal widgets.
Ex). self.bind('<Button>', self.change_units)

- This functions as a button where if pressed it will change the displayed widget by calling to the custom function change_units.

Note: It is important to pass in event as a parameter in the function called to.

