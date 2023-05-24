import openai
import PySimpleGUI as sg

#Creates the ability to open and read files

def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()

openai.api_key = open_file("API_Key.txt")

#This creates the chat bots function pulling from the openai package

def gpt3_completion(prompt, engine='text-davinci-003', temp=0.7, top_p=1.0, tokens=400, freq_pen=0.0, pres_pen=0.0,
stop=["Teenager:", "Child:"]):
    prompt = prompt.encode(encoding='ASCII', errors='ignore').decode()
    response = openai.Completion.create(
        engine=engine,
        prompt=prompt,
        temperature=temp,
        max_tokens=tokens,
        top_p=top_p,
        frequency_penalty=freq_pen,
        presence_penalty=pres_pen,
        stop=stop)
    text = response['choices'][0]['text'].strip()
    return text

#This creates the layout of the chatbots GUI window

layout = [[sg.Text('Welcome To the Chatbot')],
            [sg.Text('Type Your Message Here:'), sg.InputText(key='-IN-')],
            [sg.Button('Submit'), sg.Button('Close Window')],
            [sg.Multiline(size=(80, 50), key='textbox')]]

sg.theme("reddit")
window = sg.Window("ChatBot", layout,).finalize()

on = True

#This is the main loop of the program that allows for a continuous conversation

if __name__ == '__main__':
    converstaion = list()
    while on == True:
        event, values = window.read()
        if event in (None, 'Close Window'):
            break
        window.read()
        input = window['-IN-'].get()
        user_input = input
        print(user_input)
        if user_input == "Stop":
            on = False
        converstaion.append("Child: %s" % user_input)
        text_block = "\n".join(converstaion)
        prompt = open_file('prompt_chat.txt').replace('<<BLOCK>>', text_block)
        prompt = prompt + "\nTeenager:"
        response = gpt3_completion(prompt)
        window['textbox'].print("Child: ", input)
        window['textbox'].print("Teenager: ", response)
        converstaion.append("Teenager: %s" % response)
