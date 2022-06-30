print("Input a name of a log file.")
with open(input(), "r") as f:
    lines = f.readlines()

warnings = []
for line in lines:
    if "WARNING" in line:
        warnings.append(line)

items = []
while warnings:
    print(warnings[0] + "\n")
    print("Input a warning type.")
    warning_type = input()

    num_warning_type = len([warning for warning in warnings if warning_type in warning])
    warning_type_ex = next(warning for warning in warnings if warning_type in warning)
    warning_type_time = warning_type_ex.split()[1]
    warning_type_descr = " ".join(warning_type_ex.split()[2:])

    items.append(f"{num_warning_type} times incl. {warning_type_time} - {warning_type_descr}")

    temp = []
    for warning in warnings:
        if not warning_type in warning:
            temp.append(warning)
    warnings = temp

print("Input a name of a summary file.")
with open(input(), 'w') as f:
    for item in items:
        f.write("%s\n" % item)
