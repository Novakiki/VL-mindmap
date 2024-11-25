### SETUP

1. Set up Cursor Rules (below)
2. Specify project structure (below)    
3. Add .cursorrules file (below)
4. Open composer, ask it to proceed with steps 1 and 2
5. Test and fine tune


--------------------------------
--------------------------------


## Cursor Rules

Use termcolor for printing at every step to inform the user of the program's status.

When using with open, always specify encoding="utf-8".

Define major variables in ALL CAPS at the top of the script. Avoid taking user input for these unless explicitly required.

If the script includes models like gpt-4.0, gpt-4.0-mini, o1-mini, or o1-preview, do not modify these as they exist.

Always use try-except blocks with descriptive and informative error messages where necessary. Provide clear and helpful error printing.

Implement each project with a separation of concerns in mind.

For API keys, use system variables set with set -x in the fish shell, and access them in Python using os.getenv() instead of .env files.

Create and update requirements.txt without specifying version numbers unless absolutely necessary.

## project_structure.txt

.
├── main.py
├── static/
│   ├── css/
│   │   └── styles.css
│   └── js/
│       └── main.js
├── templates/
│   └── index.html
└── requirements.txt 

## .cursorrules

APP RULES:

fastapi webapp using daisyui, taiwind and anime js
colorful with beautiful aniamted gradients
main.py should be in root folder. it will run the app with main:app 127 with reload port 8001

STEP 1:
beautiful and animated title "Virtual Limit Mindmapper
absolutely stunning simple text input box very simple but incredibly elegant and beautiful.

STEP 2:
from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a helpful assistant. JSON word has to be in system prompt for json mode"},
        {
            "role": "user",
            "content": "Write a haiku about recursion in programming."
        },
        response_format={ "type": "json_object" }
    ]
)

print(completion.choices[0].message)

enter key will send the topic to backend
diplay a waiting animation while the call is being made to the backend
Lets use this call to return a detailed mindmap. 
lets display this to the user in a beatuiful visual.
make sure the mindmap is beautiful and animated.
make sure the user can pan and zoom in and out of the mindmap area.
make sure the mindmap area fits in to its element correctly.
lets scroll down to the mindmap when it is ready


