#     Registrations CSV Generator
#     Copyright (C) 2022  Timofei Vikhrianov
#
#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
#
#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
#
#     You should have received a copy of the GNU General Public License
#     along with this program.  If not, see <https://www.gnu.org/licenses/>.

import json
import csv
import sys
import urllib.request


def get_comp_info(comp_id):
    """Returns the competition info as a dictionary"""
    comp_info_json = urllib.request.urlopen("https://funcubing.org/api/competitions/" + comp_id).read()
    comp_info = json.loads(comp_info_json.decode("utf-8"))
    return comp_info


def get_events(comp_id):
    """Returns the competition events list"""
    comp_events_json = urllib.request.urlopen("https://funcubing.org/api/competitions/" + comp_id + "/events").read()
    comp_events = json.loads(comp_events_json.decode("utf-8"))
    events_list = list()
    for event in comp_events:
        events_list.append(event["event"])
    index = 1
    while index < len(events_list):
        if events_list[index] in events_list[: index]:
            events_list.pop(index)
        else:
            index += 1
    return events_list


def get_registrations(comp_id):
    """Returns registrations as a dictionary"""
    registrations_json = urllib.request.urlopen("https://funcubing.org/"
                                                "api/competitions/" + comp_id + "/registrations").read()
    registrations = json.loads(registrations_json.decode("utf-8"))
    return registrations


def get_competitors(registrations):
    """Returns competitors with WCA ID as a dictionary"""
    competitors = list()
    for registration in registrations:
        competitor_json = urllib.request.urlopen(
            "https://funcubing.org/api/competitors/" + registration["fc_id"]).read()
        competitor = json.loads(competitor_json.decode("utf-8"))
        competitors.append(competitor[0])
    return competitors


# Print license notice
print("Registrations CSV Generator  Copyright (C) 2022  Timofei Vikhrianov"
      "\nThis program comes with ABSOLUTELY NO WARRANTY; for details see https://www.gnu.org/licenses/gpl-3.0.html"
      "\nThis is free software, and you are welcome to redistribute it under certain conditions; "
      "see https://www.gnu.org/licenses/gpl-3.0.html for details.\n")

print("This program generates registration.csv file for your FunCubing competition. You should have an Internet "
      "connection.")
print("Please enter your competition ID: ")
comp_id = input()  # Read competition ID
try:
    comp_info = get_comp_info(comp_id)
except Exception:
    print("Error! Press ENTER to exit and try again")
    input()
    sys.exit()

print("Please wait...")

# Check "Is competition exist?"
if "error" in comp_info:
    print("Competition not found! Press ENTER to close this program and try again.")
    input()
    sys.exit()

# Check "Is competition ranked?"
if not comp_info["is_ranked"]:
    print("This competition is not ranked! This program supports ranked competitions only.")
    print("See https://cubingrf.org/calendar/speedcubing-federation-competitions/ for details.")
    print("Press ENTER to close this program.")
    input()
    sys.exit()

try:
    comp_events = get_events(comp_id)  # Get competition events list
    registrations = get_registrations(comp_id)  # Get competitors list
    registrations.sort(key=lambda registration: registration['id'])  # Sort competitors by ID
    competitors = get_competitors(registrations)
except Exception:
    print("Competition not found! Press ENTER to close this program and try again.")
    input()
    sys.exit()
# Competitors events lists ascending ID
events_list = list()
for registration in registrations:
    competitor_events = list()
    for event in comp_events:
        if event in registration["event_ids"]:
            competitor_events.append("1")
        else:
            competitor_events.append("0")
    events_list.append(competitor_events)

# Write CSV file
registrations_csv = open("registrations.csv", "w", newline='', encoding='utf-8')
writer = csv.writer(registrations_csv)
first_row = ["Status", "Name", "Country", "WCA ID", "Birth Date", "Gender"] + comp_events + ["Email"]
writer.writerow(first_row)  # Write headline
index = 0
for competitor in competitors:
    row = ["a", competitor["name"], "Russia", (competitor["wca_id"] if competitor["wca_id"] else ""), "1954-12-04",
           "o"] + events_list[index] + ["ex" + str(index) + "@ex.com"]
    writer.writerow(row)
    index += 1

print("Done! Your registration.csv saved in program directory. "
      "You can change gender and birth date manually if needed.")
print("Press ENTER to exit.")
input()
