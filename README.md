# What is a Button?
A button is a small, flat, round odject that is pressed to activate a function in electronics.

## Tutorial 1: Test your button (in Python)

1 ) Materials:

- 2x Female/Male Jumpers
- 1x Small Piece of Wire (or a Male Jumper)
- 1x Button
- Breadboard
- Raspberry Pi
- Micro SD Card

2 ) Building the Circuit:

**Step 1:** <br>
Connect one of the female/male jumper to GND pin

**Step 2:** <br>
Connect another female/male jumper to GPIO 2 pin

**Step 3:** <br>
Connect the GPIO 2 jumper to column 10 of the breadboard (Right Side)

**Step 4:** <br>
Connect the GND jumper to the negative row of the breadboard (Right Side)

**Step 5:** <br>
Connect a piece of wire (or male jumper) between the negative row and the 12 column of the breadboard (Right Side)

**Step 6:** <br>
Put the button between 10 and 12 column of the breadboard (Right Side)

3 ) Set Up the Code:

You need to import the Button module:
<pre>
from gpiozero import Button
</pre>

Create a variable named "button" and attched the "Button(2)" value to it:
<pre>
button = Button(2)
</pre>

The 'button.wait_for_press()' method makes that the next line is going to run after pressing the button-keep on mind that this method is often use on a **while loop**
<pre>
button.wait_for_press()
</pre>

4 ) My Program Examples:

A. button_press.py <br>
This Python script is looping forever, cheking if the button was pressed. When it's pressed or it's being pressed; it will diplay a message and will sleep for 0.5 seconds.

## Tutorial 2: Control a LED with the button
***Note:*** You're going to need the same **materials** and **steps** for this tutorial.
