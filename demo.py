from flask import Flask, render_template, redirect, request


app = Flask(__name__)

dummy_driver= [
        {   "user": "driver",
            "id": "HE23FZ",
            "name" : "Khaled Fraudeur",
            "phone_number" : "0556540312",
            "vehicule" : "Hyundai Atos",
            "rating" : "4.1",
            "wilaya" : "algiers",
            "model" : "Samsung A10",
            "phone_OS" : "ANDROID",
            "os_version" : "18",
            "app_version" : "2.27.1",
            "status" : "Online",
            "device_lang": "fr",
            "app_lang": "fr",
            "device_id": "qade4054h5k93",
            "last_used": "2025-09-04T13:25"
           
        }, 
        {   "user": "driver",
            "id": "KG43ES",
            "name" : "Hamoud Boulam",
            "phone_number" : "0776540312",
            "vehicule" : "kia picanto",
            "rating" : "4.2",
            "wilaya" : "algiers",
            "model" : "iphone 12",
            "phone_OS" : "ANDROID",
            "os_version" : "18",
            "app_version" : "2.28.1",
            "status" : "Online",
            "device_lang": "fr",
            "app_lang": "fr",
            "device_id": "1fdbfl42h5kf0",
            "last_used": "2025-08-25T22:13"
            
        },
        {   "user":"driver",
            "id": "BNM31Q",
            "name" : "Mourad Zawash",
            "phone_number" : "0666541632",
            "vehicule" : "Renault Clio 4",
            "rating" : "4.8",
            "wilaya" : "Blida",
            "model" : "Redmi Note 8",#model
            "phone_OS" : "ANDROID",#for platform too
            "os_version" : "18",#os version
            "app_version" : "2.28.1",#app version
            "status" : "Offline",
            "device_lang": "fr",
            "app_lang": "eng",
            "device_id": "sfd24lkjh5kf7",
            "last_used": "2025-09-01T12:05"
        }

        ]


trips = [{
    "trip_id": "XG4T2SSZH4FR",
    "date" : "04/09/2025",
    "time" : "12:04",
    "status": "FINISHED",
    "wilaya": "Algiers",    
    "depart" : "Baba Hassen",
    "destination": "Zeralda",
    "price" : "1530DA",
    "payment_method" : "espece",
    "driver" : "Khaled Fraudeur",
    "driver_id" : "HE23FZ",
    "rider": "Client 1",
    "rider_num": "0555444333",
    "service": "classique",
    "service_type": "aller simple"
},{
    "trip_id": "XG4T2S4S1QFR",
    "date" : "03/09/2025",
    "time" : "19:40",
    "status": "FINISHED",
    "wilaya": "Algiers",
    "depart" : "Bachdjerah",
    "destination": "Dely Brahim",
    "price" : "1300DA",
    "payment_method" : "espece",
    "driver" : "Khaled Fraudeur",
    "driver_id" : "HE23FZ",
    "rider": "Client Client",
    "rider_num": "0770111333",
    "service": "classique",
    "service_type": "aller simple"
},{
    "trip_id": "CP454FWJMSSM",
    "date" : "02/09/2025",
    "time" : "02:54",
    "status": "DRIVER_COMING_CANCELED",
    "wilaya": "Algiers",
    "depart" : "Hussein Dey",
    "destination": "Birtouta",
    "price" : "1782da",
    "payment_method" : "espece",
    "driver" : "Khaled Fraudeur",
    "driver_id" : "HE23FZ",
    "rider": "Client 1",
    "rider_num": "0660888999",
    "service": "classique",
    "service_type": "aller simple"
}
]


@app.route("/index", methods = ["GET", "POST"])
def demo():
    if request.method == "GET":
        return render_template("index.html", dummy_driver = dummy_driver)
    

@app.route("/bug/<driver_id>", methods=["GET", "POST"])
def bug(driver_id):
    if request.method == "GET":
        for driver in dummy_driver:
            if driver["id"] == driver_id:
                return render_template("bug.html", dummy = driver)
            

@app.route("/trip", methods=["POST", "GET"])
def trip():
    if request.method == "GET":
        return render_template("trip.html", trips=trips)

@app.route("/issue/<ride_id>", methods=["GET"])
def issue(ride_id):
    if request.method == "GET":
        for ride in trips:
            if ride_id == ride["trip_id"]:
                return render_template("issue.html", ride=ride)
                    
                

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
