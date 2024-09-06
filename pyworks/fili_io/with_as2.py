team = ["서울","인천","부산","광주","대전","대구"]
with open("./sourse/city.txt","w") as f:
    for i in team:
        f.write(i + " ")
with open("./sourse/city.txt","r") as f:
    print(f.read())