from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from pymongo import MongoClient
from datetime import datetime

cluster = MongoClient("mongodb+srv://gildas:Blacky1997@cluster0.rouo0mj.mongodb.net/?retryWrites=true&w=majority")
db = cluster["icc"]
users = db["users"]

app = Flask(__name__)


@app.route("/", methods=["get", "post"])
def reply():
    text = request.form.get("Body")
    number = request.form.get("From")
    number = number.replace("whatsapp:", "")
    res = MessagingResponse()
    user = users.find_one({"number": number})
    if bool(user) == False:
        msg = res.message("Bonjour Majesté,vous etes la bonne personne au bon endroit au bon moment et sur la bonne plateforme.\nVeuillez Choisir parmi les options suivantes :\n 1️⃣ Programme de la semaine\n 2️⃣ Les différents temples et les adresses\n 3️⃣ Qui sommes nous ? \n 4️⃣ Admin section")
        msg.media("https://i.pinimg.com/564x/66/e6/2e/66e62eb37a99ace7b28d254d9ed66670.jpg")
        users.insert_one({"number": number, "status": "main", "messages": []})
        return str(res)
    elif user["status"] == "main":
        try:
            option = int(text)
        except:
            res.message("Majesté, veuillez entrer une réponse valide !!! 😊")
            return str(res)
        if option == 1:
            res.message("Le programme de la semaine est le suivant : ")
            res.message("Chaque dimanche: \n 1 er culte à 7h30 \n 2 ème culte à 10h30 \n 3 ème culte à 13h30 ")
            return str(res)
        elif option == 2:
            res.message("Les différents temples où vous pouvez adorer le Seigneur avec nous !!!")
            res.message("*Impact Centre Chrétien - Campus de Cotonou*")
            res.message("*adresse :* Route des pêches - Axe fidjrossè fin pavés Tôgbin - rue pavée de la station JNP à droite - 1 ère rue à gauche")
            res.message("*Impact Centre Chrétien - Campus de Calavi*")
            res.message("*adresse :* Godomey Togoudo - Prendre la bretelle du trafuc local à droite en venant du pont de Houédonou pour le carrefour IITA. Immeuble Edou Service")
            return str(res)
        elif option == 3:
            msg1 = res.message("*Nous sommes une église où l'amour de Dieu transforme des gens ordinaires en champions*")
            msg1.media("https://images.subsplash.com/image.jpg?id=c3851557-30a7-424f-af7f-0eee44a7f029&w=1920&h=692")
            res.message("*Notre Vision*")
            res.message("Construire des hommes et des femmes qui inspirent et influencent positivement leur environnement pour la gloire de Dieu et pour l’avancement de l’humanité.")
            res.message("*Impact Centre Chrétien c'est :*")
            res.message("*Un centre de refuge* Où l’amour, l’acceptation, le réconfort, l’espérance, l’encouragement restaurent et transforment les personnes désespérées, frustrées, rejetées, oppressées, abusées ")
            res.message("*Un centre de formation* Où nos différentes plateformes préparent chaque personne à entrer et opérer dans un ministère de manière efficace et productive.")
            res.message("*Un centre d'adoration* Où la puissance de la Parole transforme chaque personne en véritable adorateur, en esprit et en vérité. (Jean 4 : 23)")
            return str(res)
        elif option == 4:
            res.message("Admin section en cours de construction !!!!")
            return str(res)
        else:
            res.message("Majesté, veuillez entrer une réponse valide !!! 😊")
            return str(res)

if __name__ == "__main__":
    app.run()
