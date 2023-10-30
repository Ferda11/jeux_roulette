from random import randrange
import pickle

def chaine_majuscule(nom):
    for i in nom:
        if i.isupper():
            return True
    return False


# function sa se pouw fe tretman sou non user a
def connexion():
    nom=input("Antre non ou san espas ni let majiskil: ")
    while True:
            if " " in nom or chaine_majuscule(nom):
                nom = input('nom pa dwe gn espace oubyen let majiskil :')
                continue
                 
            return nom

    
    
    
    
        
# telechaje 
def load_database():
    try:
        with open('DB','rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        return []      

# anregitre yon base de done  
def save(database):
    with open('DB','wb') as file:
            return pickle.dump(database,file)
         
# anregistre user ak skol
def register(user,sko=0):
    database = load_database()
    for i in database:
        if i['nom'] == user:
            print('utilisateur sa egziste deja skol se:',i['sko'])
            break
    else:  
        user_info ={
            'nom':user,
            'sko':sko}
        
        database.append(user_info) 
    save(database)
    

# function sa se pouw update sko menm pat testel
def update_sko(user,chans):
        database = load_database()
        for i in database:
            if i['nom'] == user:
                i['sko'] += (chans-1) *30           
        save(database)               
        return 

    
def get_user(user):
        database = load_database()
        for i in database:
            if i['nom'] == user:
                return i


reponse=" "
user = connexion()
register(user)
while ( not reponse.lower()=="k"):
    nonb_odi=randrange(0,1)
    chans=5
    while(chans>0):

        try:
            nonb_itilizate=int(input("antre yon nonb nan enteval 0-100 ou gen "+str(chans)+" chans :"))
            if 0 <= nonb_itilizate <=100 :
                if(nonb_itilizate < nonb_odi):
                    print(f"ou pedi paske ou chwazi {str(nonb_itilizate)} ki piti ke  nonb ki jenere a")
                elif(nonb_itilizate > nonb_odi):
                    print(f"ou pedi paske ou chwazi {str(nonb_itilizate)}  ki gro ke  nonb ki jenere a")

                else:
                    print(f"ou genyen paske ou chwazi {str(nonb_itilizate)} ki egal ak {str(nonb_odi)} nonb ki jenere a")
                    update_sko(user,chans)
                    
                    
                    break
                chans-=1
                
            else:
                print("nonb ou chwazi a dwe jwenn li ant 0 a 100")
        except ValueError:
            print("antre yon nonb valid")
    sko=(chans-1)*30
   
    if(chans==0):
        print("ou pa gen chans ki rete anko .")
        print("Nonb ki te kache a se :"+str(nonb_odi))
        print("sko ou nan pati sa se :"+str(sko))
        
    user = get_user(user)
    newsko = user['sko']
    print(f"Nouvo sko ou se{newsko}")
    reponse=input("eske ou vle rejwe? wi/non. prese nenpot touch siw vle kontinye epi k siw pap kontinye :")
    #user = get_user(user)
   # newsko = user['sko']
    
    if(reponse.lower() =="k"):
        print("mesi paskew te chwazi jwe!!!!")
        break
                    
