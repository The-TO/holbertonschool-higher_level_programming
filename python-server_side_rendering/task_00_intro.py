#!/usr/bin/python3
"""Genere un fichier d'invitation personnalisé depuis le template"""


def generate_invitations(template, attendees):
    """créer un fichier output_X.txt par participant, remplissant le modèle"""
    if not isinstance(template, str):
        print(f"Error: template must be a string, got {type(template).__name__}")
        return
    if not isinstance(attendees, list) or \
            not all(isinstance(a, dict) for a in attendees):
        print(f"Error: attendees must be a {type(attendees).__name__} and contains dictionaries")
        return
    if not template:
        print("Template is empty, no output files generated.")
        return
    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    placeholder = ["name", "event_title", "event_date", "event_location"]

    for i, attendee in enumerate(attendees, start=1):
        content = template
        for key in placeholder:
            value = attendee.get(key)
            if value is None:
                value = "N/A"
            content = content.replace("{" + key + "}", str(value))

        try:
            with open("output_{}.txt".format(i), "w") as f:
                f.write(content)
        except OSError as e:
            print(f"Error writing output_{i}.txt: {e}")
