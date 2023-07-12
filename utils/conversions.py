def getJsonList(dinos):
    dinoList = []
    for dino in dinos:
        dinoList.append(dino.__dict__)
    return dinoList
