#! python3
# formFiller.py - Automatically fills in the form.

import pyautogui, time

formData = [{'name': 'Alice', 'fear': 'eavesdroppers', 'source': 'wand',
            'robocop': 4, 'comments': 'Tell Bob I said hi.'},
            {'name': 'Bob', 'fear': 'bees', 'source': 'amulet', 'robocop': 4,
            'comments': 'n/a'},
            {'name': 'Carol', 'fear': 'puppets', 'source': 'crystal ball',
            'robocop': 1, 'comments': 'Please take the puppets out of the break room.'},
            {'name': 'Alex Murphy', 'fear': 'ED-209', 'source': 'money',
            'robocop': 5, 'comments': 'Protect the innocent. Serve the public trust. Uphold the law.'},
           ]


for person in formData:
    
    # Give the user a chance to kill the script.
    print('>>> 5-SECOND PAUSE TO LET USER PRESS CTRL-C <<<')
    time.sleep(5)
    
    # Wait until the form page has loaded.
    print('Entering %s info...' % (person['name']))
    pyautogui.write(['\t', '\t'])
    
    # Fill out the Name Field.
    pyautogui.write(person['name'] + '\t')
    
    # Fill out the Greatest Fear(s) field.
    pyautogui.write(person['fear'] + '\t')
    
    # Fill out the Source of Wizard Powers field.
    if person['source'] == 'wand':
        pyautogui(['down', '\t'], 0.5)
    elif person['source'] == 'amulet':
        pyautogui(['down', 'down', '\t'], 0.5)
    elif person['source'] == 'crystal ball':
        pyautogui(['down', 'down', 'down', '\t'], 0.5)
    elif person['source'] == 'money':
        pyautogui(['down', 'down', 'down', 'down' '\t'], 0.5)

    # Fill out the RoboCop field.
    if person['robocop'] == 1:
        pyautogui([' ', '\t'], 0.5)
    elif person['robocop'] == 2:
        pyautogui(['right', '\t'], 0.5)
    elif person['robocop'] == 3:
        pyautogui(['right', 'right', '\t'], 0.5)
    elif person['robocop'] == 4:
        pyautogui(['right', 'right', 'right', '\t'], 0.5)
    elif person['robocop'] == 5:
        pyautogui(['right', 'right', 'right', 'right' '\t'], 0.5)

    # Fill out the Additional Comments field.
    pyautogui.write(person['comments'] + '\t')

    # Click Submit button by pressing Enter.
    time.sleep(0.5) # Wait for button to activate.
    pyautogui.press('enter')

    # Wait until form page has loaded.
    print('Submitted form.')
    time.sleep(5)

    # Click the Submit another response link.
    pyautogui.click(submitAnotherLink[0], submitAnotherLink[1])