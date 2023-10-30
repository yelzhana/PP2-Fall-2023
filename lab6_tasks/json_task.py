import json

with open("sample-data.json", "r") as file:
    data = json.load(file)

headers = ["DN", "Description", "Speed", "MTU"]

print(f"{headers[0]:<50} {headers[1]:<20} {headers[2]:<10} {headers[3]:<6}")
print("=" * 80)

output = []
for entry in data["imdata"]:
    attributes = entry["l1PhysIf"]["attributes"]
    dn = attributes["dn"]
    descr = attributes["descr"]
    speed = attributes["speed"]
    mtu = attributes["mtu"]
    output.append([dn, descr, speed, mtu])

print(f"{'DN':<50} {'Description':<20} {'Speed':<10} {'MTU':<6}")
print("-"*80)
for row in output:
    print(f"{row[0]:<50} {row[1]:<20} {row[2]:<10} {row[3]:<6}")