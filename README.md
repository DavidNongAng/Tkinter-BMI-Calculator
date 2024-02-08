This repository is a BMI calculator app. This is not my project, I am recreating it as a learning experience.

Original: https://www.youtube.com/watch?v=mop6g-c5HEY&t=45995s

New things I learned:

- Tracing: Tkinter provides a way to trace changes to a variable. It would either trace Write 'w' or Read 'r' a variable and run a function when it does.

Ex: self.height_int.trace('w', self.update_bmi)
When the height on the app is updated (writing), it will run the function to update the BMI.
