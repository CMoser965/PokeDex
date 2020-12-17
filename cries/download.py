import wget

url = 'https://veekun.com/dex/media/pokemon/cries/'
for x in range(1, 721):
    filename = wget.download(url + str(x) + '.ogg')
    print(str(x) + "downloaded")

print("finished.")
