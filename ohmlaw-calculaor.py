value1 = input("Enter the 1st value: ")
try:
    value1 = int(value1)
except ValueError:
    try:
        value1 = float(value1)
    except ValueError:
        print("Invalid value")
identity1 = input("Enter the 1st value identity: ")
value2 = input("Enter the 2nd value: ")
try:
    value2 = int(value2)
except ValueError:
    try:
        value2 = float(value2)
    except ValueError:
        print("Invalid value")
identity2 = input("Enter the 2nd value identity: ")
operator = input("Enter the operator: ")

if operator == "R" and identity1 == "V" and identity2 == "A":
    print(value1 / value2, "ohm")
elif operator == "V" and identity1 == "ohm" and identity2 == "A":
    print(value1 * value2, "V")
elif operator == "V" and identity1 == "A" and identity2 == "W":
    print(value1 / value2, "V")
elif operator == "I" and identity1 == "V" and identity2 == "ohm":
    print(value1 / value2, "A")
elif operator == "I" and identity1 == "V" and identity2 == "W":
    print(value1 / value2, "A")
elif operator == "P" and identity1 == "V" and identity2 == "A":
    print(value1 * value2, "W")
elif operator == "P" and identity1 == "V" and identity2 == "ohm":
    print(value1 * value1 / value2, "W")
elif operator == "P" and identity1 == "A" and identity2 == "ohm":
    print(value1 * value1 * value2, "W")
elif operator == "R" and identity1 == "ohm" and identity2 == "ohm":
    print(value1 + value2, "ohm")
    print("Amperage is same Amperage of one component")
    print("It is a series circuit")
elif operator == "R" and identity1 == "kohm" and identity2 == "kohm":
    print(value1 + value2, "kohm")
    print("Amperage is same Amperage of one component")
    print("It is a series circuit")
elif operator == "R" and identity1 == "Mohm" and identity2 == "Mohm":
    print(value1 + value2, "Mohm")
    print("Amperage is same Amperage of one component")
    print("It is a series circuit")
elif operator == "V" and identity1 == "V" and identity2 == "V":
    print(value1 + value2, "V")
    print("Amperage is same Amperage of one component")
    print("It is a series circuit")
elif operator == "C" and identity1 == "uF" and identity2 == "uF":
    print(value1 + value2, "uF")
    print("Amperage is same Amperage of one component")
    print("It is a series circuit")
elif operator == "C" and identity1 == "nF" and identity2 == "nF":
    print(value1 + value2, "nF")
    print("Amperage is same Amperage of one component")
    print("It is a series circuit")
elif operator == "C" and identity1 == "pF" and identity2 == "pF":
    print(value1 + value2, "pF")
    print("Amperage is same Amperage of one component")
    print("It is a series circuit")
elif operator == "C" and identity1 == "F" and identity2 == "F":
    print(value1 + value2, "F")
    print("Amperage is same Amperage of one component")
    print("It is a series circuit")
elif operator == "I" and identity1 == "A" and identity2 == "A":
    print(value1 + value2, "A")
    print("It is a parellel circuit")
    print(
        "Voltage and Resistance is same Voltage and Resistance of one component"
    )

else:
    print("Invalid operator")
