import wolframalpha
Client = wolframalpha.Client("HRK7Q3-U78RHLUQJ3")

import wikipedia

import PySimpleGUI as sg

import pyttsx3
engine = pyttsx3.init()
#engine.say("hello anjali you are really smart and you will definitely appoint in infosys")

#engine.runAndWait()    


sg.theme('DarkPurple')	# Add a touch of color
# All the stuff inside your window.
layout = [[sg.Text('Enter A command'),sg.InputText()],[sg.Button('Ok'),sg.Button('Cancel')]]

# Create the Window
window = sg.Window('PyDa',layout)

    
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event in [None,'Cancel']:	# if user closes window or clicks cancel
        break
    try:
        res=Client.query(values[0])
        wiki_res = wikipedia.summary(values[0],sentences=2)
        wolfram_res=next(res.results).text
        engine.say(wolfram_res)
        engine.say(wiki_res)
        sg.PopupNonBlocking('wolfram Result: '+wolfram_res,'wikipedia Result: '+wiki_res)   #Add results of wolfram & wikipedia    

    except wikipedia.exceptions.DisambiguationError: 
        res=Client.query(values[0])
        wolfram_res=next(res.results).text
        engine.say(wolfram_res)
        sg.PopupNonBlocking('wolfram Result: '+wolfram_res)   #Add results of wolfram & wikipedia         

    except wikipedia.exceptions.PageError:
        res=Client.query(values[0])
        wolfram_res=next(res.results).text
        engine.say(wolfram_res)
        sg.PopupNonBlocking('wolfram Result: '+wolfram_res)   #Add results of wolfram & wikipedia

    except:
        wiki_res = wikipedia.summary(values[0],sentences=2)
        engine.say(wiki_res)
        sg.PopupNonBlocking('wikipedia Result: '+wiki_res)   #Add results of wolfram & wikipedia
       
    engine.runAndWait()
    
    
    print(values[0])

            
window.close()









