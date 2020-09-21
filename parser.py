import requests
import json
import os.path

json_dir = "/Users/JessicaChen/Desktop/labelbox-masks.json"
save_dir = "/Users/JessicaChen/Desktop/PC ML Project/labelbox_images"

with open(json_dir) as a:
    data = json.load(a)
    for index, i in enumerate(data):

        # save original images
        og = i['Labeled Data']
        fileName = "scan{:04d}.png".format(index)
        completeName = os.path.join(save_dir, fileName)
        res = requests.get(og)
        with open(completeName, "wb") as output:
            output.write(res.content)

        # save individual instances
        instance = i['Label']['objects']
        for j in instance:
            og2 = (j['instanceURI'])
            fileName2 = "scan{:04d}-{}.png".format(index, j['value'])
            completeName2 = os.path.join(save_dir, fileName2)
            res2 = requests.get(og2)
            with open(completeName2, "wb") as output2:
                output2.write(res2.content)

