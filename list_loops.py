songs = ["ROCKSTAR", "Do It", "For The Night"]
print(songs[1])
print(songs[-1])
songs[-1]="Pikasonic Forever"
print(songs)
songs.extend(["Pikasonic Inside", "Porter Robinson Shelter"])
del songs[1]
print (songs)

animals = ["Cat","Dog","Mice"]
animals.append("Slime. Yes slime.")
print (animals[2])
del animals[0]
for animal in animals:
    print (animal)