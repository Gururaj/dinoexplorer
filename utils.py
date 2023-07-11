def getJsonList(dinos):
    dinoList = []
    for dino in dinos:
        dinoList.append(dino.getJson())
    return dinoList
