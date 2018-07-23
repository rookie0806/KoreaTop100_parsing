import csv
    
def make_DB():
    DB = [] 
    
    with open('recent.csv', newline='') as csvfile:
        grade = 200
        reader = csv.DictReader(csvfile)
        for row in reader:
            musicid = row['Music_id']
            musictitle = row['Music_title']
            musicartist = row['Music_artist']
            DB.append([musicid,musictitle,musicartist,grade,0])
            #grade = grade - 1
    
    
    with open('top.csv', newline='') as csvfile:
        grade = 200
        reader = csv.DictReader(csvfile)
        for row in reader:
            flag = 0
            musicid = row['Music_id']
            musictitle = row['Music_title']
            musicartist = row['Music_artist']
            #grade = grade - 1
            for E in DB : 
                if musicid in E:
                    E[4] = grade
                    flag = 1
                    break
            if(flag==0):
                DB.append([musicid,musictitle,musicartist,0,grade])

    return DB

def save() :
    DB = make_DB()
    with open('my_list2.csv', 'w', newline='') as csvfile:
        fieldnames = ['Music_id','Music_title', 'Music_artist','Grade']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for i in range(0,len(DB)):
            grade = (int(DB[i][3]) * 0.65 + int(DB[i][4]) * 0.35)  / 2
            writer.writerow({'Music_id': DB[i][0], 'Music_title': DB[i][1], 'Music_artist' : DB[i][2], 'Grade' : grade})

if __name__ == "__main__":
    save()
