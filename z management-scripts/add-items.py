"""

This creates the HTML script for adding items to the SkyCity 
inventory page. The input is a comma delimited text input,
and the output is the appropriate HTML into the add-items-output.txt

"""


items = input("input items (coma delimited): ").split(",")

rolling_str = ""

for item in items:
    
    if item == "":
        continue
    rolling_str += f"<tr><td>{item}</td><td>HIGH</td></tr>\n"


with open("add-items-output.txt", "w") as f:
    f.write(rolling_str)

print(rolling_str)