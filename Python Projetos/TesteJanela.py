import PySimpleGUI as sg                        # Part 1 - The import

# Define the window's contents
layout = [  [sg.Text("Qual seu Nome?")],     # Part 2 - The Layout
            [sg.Input()],
            [sg.Button('Ok')] ]

# Create the window
window = sg.Window('Digite Seu Nome', layout)      # Part 3 - Window Defintion

# Display and interact with the Window
event, values = window.read()                   # Part 4 - Event loop or Window.read call

# Do something with the information gathered
print('Ola', values[0], "! Obrigado")

# Finish up by removing from the screen
window.close()                                  # Part 5 - Close the Window