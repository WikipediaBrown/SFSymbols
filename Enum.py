
numbers = {
  "case": "caseImage",
  "repeat": "repeatImage",
  "return": "returnImage",
  "0": "zero",
  "1": "one",
  "2": "two",
  "3": "three",
  "4": "four",
  "5": "five",
  "6": "six",
  "7": "seven",
  "8": "eight",
  "9": "nine"
}

file = open("Sources/SFSymbols/Enum.swift", "w")

file.write("//\n")
file.write("//  SFSymbols.swift\n")
file.write("//  Missions\n")
file.write("//\n")
file.write("//  Created by nonplus on 12/18/21.\n")
file.write("//\n")
file.write("\n")
file.write("public enum SFSymbols: String, CaseIterable {\n")
file.write("\n")

with open('SFSymbols.txt') as topo_file:
    for line in topo_file:
        parts = line.split('.')
        camelCaseName = ""
        
        for part in parts:
            if part == parts[0]:
            
                if part.rstrip() in numbers:
                    camelCaseName += numbers[part.rstrip()]
                    continue
                elif part[0] in numbers:
                    camelCaseName += numbers[part[0]] + part[1:]
                    continue
                camelCaseName += part
                continue
            camelCaseName += part.capitalize()
            
        result = "    case {} = \"{}\"\n".format(camelCaseName.rstrip(), line.rstrip())
        file.write(result)
file.write("}\n")
file.close()
