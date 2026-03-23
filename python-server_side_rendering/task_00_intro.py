def generate_invitations(template, attendees):

    if not isinstance(template, str):
        print("Error: template must be a string")
        return

    if not template:
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    if not all(isinstance(attendee, dict) for attendee in attendees):
        print("Error: attendees must be a list of dictionaries")
        return

    for i, attendee in enumerate(attendees, start=1):
        attendee_name = attendee.get("name") or "N/A"
        attendee_title = attendee.get("event_title") or "N/A"
        attendee_date = attendee.get("event_date") or "N/A"
        attendee_location = attendee.get("event_location") or "N/A"

        result = template.replace("{name}", attendee_name)
        result = result.replace("{event_title}", attendee_title)
        result = result.replace("{event_date}", attendee_date)
        result = result.replace("{event_location}", attendee_location)

        with open(f"output_{i}.txt", "w") as f:
            f.write(result)
