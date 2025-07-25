action = 'shoot'
score = 0

if action =='shoot':
    print("oh shoot kard!")
elif action =='pass':
    print('pass dad be doostesh')
elif action == "goal" :
    print("goaaaaaal")
    score +=1        #مدل خلاصه شده score = score + 1
else:
    print("che kardi?")

if score> 0 :
    print(f"oh barande shodi{score}")
else:
    print("bazi cherti bood")