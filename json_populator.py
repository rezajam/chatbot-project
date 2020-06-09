import json
import pycountry


countryName = []

for ctry in pycountry.countries:
    # print(ctry.name)
    countryName.append(ctry.name)


# print(countryName)


# testing the dictionary listing from countryNames above.
mainDict = {}
synonymsList = []
valuesTest = []
for cn in countryName:
    mainDict = {}
    mainDict["type"] = "synonyms"
    mainDict["value"] = cn
    mainDict["synonyms"] = synonymsList
    valuesTest.append(mainDict)

# print(mainDict)
# print(valuesTest)


with open('skill-CHAT2.json') as f:
    data = json.load(f)
# "entity": "country"

# for entity in data["entities"]:
#     if (entity['entity'] == 'country'):
#         print(entity['values'].clear())

# This is the fetcher for quality check later
for entity in data["entities"]:
    if (entity['entity'] == 'country'):
        # print(entity['values'])
        # for cname in (entity['values']):
        #     print(cname["value"])
        for cn in countryName:
            mainDict = {}
            mainDict["type"] = "synonyms"
            mainDict["value"] = cn
            mainDict["synonyms"] = synonymsList
            entity['values'].append(mainDict)
        # print("=====Entity['values']=====")
        # print(entity['values'])


print("======JSON PRINT=======")
print(data)
