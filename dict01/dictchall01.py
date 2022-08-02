#!/usr/bin/env python3

##create a dictionary
char_name= input(" Which character do you want to know about? (Startlord, Mystique, Hulk)").title()
char_stat= input(" What statisti  do you want to know about? (real name, powers, archenemy)").lower()

marvelchars= {
"Starlord":
{"real name": "peter quill",
  "powers": "dance moves",
  "archenemy": "Thanos"},

"Mystique":
  {"real name": "raven darkholme",
  "powers": "shape shifter",
  "archenemy": "Professor X"},

"Hulk":
  {"real name": "bruce banner",
  "powers": "super strength",
  "archenemy": "adrenaline"}
             }

print(f"{char_name}'s {char_stat} is: {marvelchars get(char_name).get(char_stat).title()}")
