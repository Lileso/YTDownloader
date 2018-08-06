import pafy

url = input("Please Enter URL:\n")
video = pafy.new(url)
best = video.getbest()

dl_location = best.url

#best.download(quiet=False)

import urllib.request, shutil

with urllib.request.urlopen(dl_location) as response, open("video_ltt.mp4", 'wb') as out_file:
    shutil.copyfileobj(response, out_file)

print("Done!")