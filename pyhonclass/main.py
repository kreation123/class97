intro = input('enter you name :    ')
print(intro)
characterCouunt = 0
worldCount= 1
for character in intro :
    characterCouunt = characterCouunt +1
    if(character == ' '):
        worldCount = worldCount + 1
print(characterCouunt)
print(worldCount)