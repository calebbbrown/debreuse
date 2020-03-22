from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)

recentsearches=[
    {
    "id": 1,
    "name": "Augustus",
    "portrait": "/static/pic1.jpg",
    "death":"Livia",
    "reignstart": -27,
    "reignend": 14,
    "summary": "Augustus, son of Gaius Julius Caesar, became the first princeps of Rome after defeating Marcus Antonius and Cleopatra. His role morphed from one of de facto primacy based upon his own personal wealth and the loyalty of the armies under Marcus Agrippa into a formal dynastic monarchial system. Augustus slowly and carefully built a political machine, the basic tenets of which would define Rome for over 400 years. Regrettably, Augustus was not as skilled at managing his personal affairs as he was in regards to public affairs, and he struggled to guide his willful and treacherous family all his life. His most impressive accomplishment of all may have been the peaceful transfer of his power upon his death to his unlikely heir Tiberius.",
    "rating": 9,
    "children":["julia", "postumus"]
    },
    {
    "id": 2,
    "name": "Tiberius",
     "portrait": "/static/pic2.jpg",
     "death":"Natural",
     "reignstart": 14,
     "reignend": 37,
     "summary": "Tiberius' greatest accomplishment was maintaining a peaceful transition of pseudohereditary power, thus establishing the pattern that the monarchy would take for hundreds of years. Tiberius is remembered as a hard, cold emperor who stocked up the treasury like a miser at the expense of his citizens. Whether this was sound long-term fiscal policy can be debated, but in any case, it made him less than popular. Before his reign began, he established a reputation as a legendary general and conqueror for Rome, but his imperial reign was defined by a paranoid and reclusive existence at his Capri estate",
     "rating": 5,
     "children":["Drusus","Germanicus","Caligula"]
    },
    {
    "id": 3,
    "name": "Caligula",
     "portrait": "/static/pic3.jpg",
     "death":"Natural",
     "reignstart": 37,
     "reignend": 41,
     "summary": "The so-called Mad Emperor, Caligula is the first in a long line of men who took the throne before they were old enough to be responsible with it. It has been speculated that a bout of brain fever altered Caligula such that he because much more erratic and cruel after the illness. His reign is remembered for such exploits as his war against Neptune, naming his beloved horse a Consul, and taking liberties with the wives of senators. As must be expected, Caligula, who was never called by that semi-insulting nickname in his time, was assassinated before his reign reached 5 years.",
     "rating": 2,
     "children":["julia drusilla"]
    },
   {
   "id": 4,
   "name": "Claudius",
    "portrait": "/static/pic4.jpg",
    "death":"Natural",
    "reignstart": 41,
    "reignend": 54,
    "summary": "One of the most unlikely emperors, Claudius avoided the suspicion and execution that befell his more powerful relatives during Tiberius' fraught reign, and after Caligula's death, found himself instantly and surprisingly the epicenter of political power (surprisingly, that is, if you believe he had no hand in Caligula's downfall). Claudius was known for a physical disability, now speculated to have been cerebral palsy or epilepsy, which left him the object of much mockery. Nevertheless, upon gaining the throne, Claudius proved a wise ruler who personally took part in administrative and legal affairs, and notably his reign saw the first stages of the conquest of Britain by the great general Agricola",
    "rating": 8,
    "children": ["Claudia","Brittanicus", "Nero"]
   },
   {
   "id": 5,
   "name": "Nero",
    "portrait": "/static/pic5.JPG",
    "death":"Natural",
    "reignstart": 54,
    "reignend": 68,
    "summary": "The lasting modern image of Nero is that of the hillside fiddler basking in the flames of Rome. However, it is to be noted that Nero, a populist who raised taxes on the wealthy to fund a massive public works campaign, was despised by the learned of his time, so the written accounts we have of his life must be read with some skepticism. Controlled by a domineering mother for the beginning stages of his rule, Nero eventually ignored Agrippina's diktats and forged his own rule, which, though unpopular among the court, was mostly celebrated by his citizens. However, Nero could not get away with thumbing his nose at the elite forever, and he was eventually assasinated.",
    "rating": 4,
    "children":[]
   },
   {
   "id": 6,
   "name": "Galba",
    "portrait": "/static/pic6.jpg",
    "death":"Natural",
    "reignstart": 68,
    "reignend": 69,
    "summary": "Galba happened to be in the right place at the right time upon Nero's assasination, as head of the Praetorian guard, a powerful military force in Rome. However, he was not popular among the people, nor the senators, so his reign was short lived and uneventful. He is best known for being first in the so called Year of Four Emperors. The second emperor, the powerful senator Otho, had Galba killed in short order.",
    "rating": 2,
    "children":[]
   },
   {
   "id": 7,
   "name": "Otho",
    "portrait": "/static/pic7.jpg",
    "death":"Natural",
    "reignstart": 69,
    "reignend": 69,
    "summary": "Second in the Year of Four Emperors, Otho was a powerful Roman elite who seemed to have a decent path to long term power upon the elimination of Galba. However, during the reign of Galba, the general Vitellius of the German provinces had staged a revolt, and this problem became Otho's problem upon his ascention. Unfortunately for Otho, Vitellius had him outgunned, and he was decisively defeated at Bedriacum, bringing an end to his short reign",
    "rating": 1,
    "children":[]
   },
   {
   "id": 8,
   "name": "Vitellius",
    "portrait": "/static/pic8.jpg",
    "death":"Natural",
    "reignstart": 69,
    "reignend": 69,
    "summary": "Upon overthrowing Otho, Vitellius and his weakened legions immediately learned the meaning of the word 'irony' as the eastern general Vespasion did to Vitellius what Vitellius had done to Otho. Another battle was staged at Bedriacum, where Vespasian's legions, hardened by continual struggles with the Persians over the years, defeated the bruised armies of Vitellius, ending his very short reign",
    "rating": 1,
    "children":[]
   },
   {
   "id": 9,
   "name": "Vespasian",
    "portrait": "/static/pic9.jpg",
    "death":"Natural",
    "reignstart": 69,
    "reignend": 79,
    "summary": "Vespasian's biggest accomplishment is putting Rome back on a path of stability after an exceptionally unstable period of civil war. Apart from that underrated feat, Vespasian did not do much conquering beyond continued expansion of Roman dominion in Britain. He is remembered today for the Colliseum, which he began and left to his son Trajan to complete upon his death.",
    "rating": 8,
    "children":[]
   },
   {
   "id": 10,
   "name": "Titus",
    "portrait": "/static/pic10.jpg",
    "death":"Natural",
    "reignstart": 79,
    "reignend": 81,
    "summary": "Titus had a short but peaceful reign, and was remembered fondly by contemporaries as well as modern scholars. He completed public works such as the Colliseum, and provided funds and infrastucture to the oft-neglected provinces. Whether his untimely death was truly fever can always be disputed, but with no hard evidence to support assasination, it seems that Titus simply ran out of luck. " ,
    "rating": 5,
    "children":[]
   }
];

Emperors=[{
"id": 1,
"name": "Augustus",
"portrait": "/static/pic1.jpg",
"death":"Natural",
"reignstart": -27,
"reignend": 14,
"summary": "Augustus, son of Gaius Julius Caesar, became the first princeps of Rome after defeating Marcus Antonius and Cleopatra. His role morphed from one of de facto primacy based upon his own personal wealth and the loyalty of the armies under Marcus Agrippa into a formal dynastic monarchial system. Augustus slowly and carefully built a political machine, the basic tenets of which would define Rome for over 400 years. Regrettably, Augustus was not as skilled at managing his personal affairs as he was in regards to public affairs, and he struggled to guide his willful and treacherous family all his life. His most impressive accomplishment of all may have been the peaceful transfer of his power upon his death to his unlikely heir Tiberius.",
"rating": 9,
"children":["julia", "postumus"]
},
{
"id": 2,
"name": "Tiberius",
 "portrait": "/static/pic2.jpg",
 "death":"Natural",
 "reignstart": 14,
 "reignend": 37,
 "summary": "Tiberius' greatest accomplishment was maintaining a peaceful transition of pseudohereditary power, thus establishing the pattern that the monarchy would take for hundreds of years. Tiberius is remembered as a hard, cold emperor who stocked up the treasury like a miser at the expense of his citizens. Whether this was sound long-term fiscal policy can be debated, but in any case, it made him less than popular. Before his reign began, he established a reputation as a legendary general and conqueror for Rome, but his imperial reign was defined by a paranoid and reclusive existence at his Capri estate",
 "rating": 5,
 "children":["Drusus","Germanicus","Caligula"]
},
{
"id": 3,
"name": "Caligula",
"portrait": "/static/pic3.jpg",
 "death":"Natural",
 "reignstart": 37,
 "reignend": 41,
 "summary": "The so-called Mad Emperor, Caligula is the first in a long line of men who took the throne before they were old enough to be responsible with it. It has been speculated that a bout of brain fever altered Caligula such that he because much more erratic and cruel after the illness. His reign is remembered for such exploits as his war against Neptune, naming his beloved horse a Consul, and taking liberties with the wives of senators. As must be expected, Caligula, who was never called by that semi-insulting nickname in his time, was assassinated before his reign reached 5 years.",
 "rating": 2,
 "children":["julia drusilla"]
},
{
"id": 4,
"name": "Claudius",
"portrait": "/static/pic4.jpg",
"death":"Natural",
"reignstart": 41,
"reignend": 54,
"summary": "One of the most unlikely emperors, Claudius avoided the suspicion and execution that befell his more powerful relatives during Tiberius' fraught reign, and after Caligula's death, found himself instantly and surprisingly the epicenter of political power (surprisingly, that is, if you believe he had no hand in Caligula's downfall). Claudius was known for a physical disability, now speculated to have been cerebral palsy or epilepsy, which left him the object of much mockery. Nevertheless, upon gaining the throne, Claudius proved a wise ruler who personally took part in administrative and legal affairs, and notably his reign saw the first stages of the conquest of Britain by the great general Agricola",
"rating": 8,
"children": ["Claudia","Brittanicus", "Nero"]
},
{
"id": 5,
"name": "Nero",
"portrait": "/static/pic5.jpg",
"death":"Natural",
"reignstart": 54,
"reignend": 68,
"summary": "The lasting modern image of Nero is that of the hillside fiddler basking in the flames of Rome. However, it is to be noted that Nero, a populist who raised taxes on the wealthy to fund a massive public works campaign, was despised by the learned of his time, so the written accounts we have of his life must be read with some skepticism. Controlled by a domineering mother for the beginning stages of his rule, Nero eventually ignored Agrippina's diktats and forged his own rule, which, though unpopular among the court, was mostly celebrated by his citizens. However, Nero could not get away with thumbing his nose at the elite forever, and he was eventually assasinated.",
"rating": 4,
"children":[]
},
{
"id": 6,
"name": "Galba",
"portrait": "/static/pic6.jpg",
"death":"Natural",
"reignstart": 68,
"reignend": 69,
"summary": "Galba happened to be in the right place at the right time upon Nero's assasination, as head of the Praetorian guard, a powerful military force in Rome. However, he was not popular among the people, nor the senators, so his reign was short lived and uneventful. He is best known for being first in the so called Year of Four Emperors. The second emperor, the powerful senator Otho, had Galba killed in short order.",
"rating": 2,
"children":[]
},
{
"id": 7,
"name": "Otho",
"portrait": "/static/pic7.jpg",
"death":"Natural",
"reignstart": 69,
"reignend": 69,
"summary": "Second in the Year of Four Emperors, Otho was a powerful Roman elite who seemed to have a decent path to long term power upon the elimination of Galba. However, during the reign of Galba, the general Vitellius of the German provinces had staged a revolt, and this problem became Otho's problem upon his ascention. Unfortunately for Otho, Vitellius had him outgunned, and he was decisively defeated at Bedriacum, bringing an end to his short reign",
"rating": 1,
"children":[]
},
{
"id": 8,
"name": "Vitellius",
"portrait": "/static/pic8.jpg",
"death":"Natural",
"reignstart": 69,
"reignend": 69,
"summary": "Upon overthrowing Otho, Vitellius and his weakened legions immediately learned the meaning of the word 'irony' as the eastern general Vespasion did to Vitellius what Vitellius had done to Otho. Another battle was staged at Bedriacum, where Vespasian's legions, hardened by continual struggles with the Persians over the years, defeated the bruised armies of Vitellius, ending his very short reign",
"rating": 1,
"children":[]
},
{
"id": 9,
"name": "Vespasian",
"portrait": "/static/pic9.jpg",
"death":"Natural",
"reignstart": 69,
"reignend": 79,
"summary": "Vespasian's biggest accomplishment is putting Rome back on a path of stability after an exceptionally unstable period of civil war. Apart from that underrated feat, Vespasian did not do much conquering beyond continued expansion of Roman dominion in Britain. He is remembered today for the Colliseum, which he began and left to his son Trajan to complete upon his death.",
"rating": 8,
"children":[]
},
{
"id": 10,
"name": "Titus",
"portrait": "/static/pic10.jpg",
"death":"Natural",
"reignstart": 79,
"reignend": 81,
"summary": "Titus had a short but peaceful reign, and was remembered fondly by contemporaries as well as modern scholars. He completed public works such as the Colliseum, and provided funds and infrastucture to the oft-neglected provinces. Whether his untimely death was truly fever can always be disputed, but with no hard evidence to support assasination, it seems that Titus simply ran out of luck. " ,
"rating": 5,
"children":[]
},
{
"id": 11,
"name": "Domition",
"portrait": "/static/pic11.jpg",
"death":"Natural",
"reignstart": 81,
"reignend": 96,
"summary": "One of the most divisive emperors, Domitian was hated in his time, especially by the senate, for his dictatorial style. However, upon more modern reflection, it appears that Domitian was a prudent and capable ruler, if somewhat ruthless and power-hungry.",
"rating": 7,
"children":[]
},
{
"id": 12,
"name": "Nerva",
"portrait": "/static/pic12.jpg",
"death":"Natural",
"reignstart": 96,
"reignend": 98,
"summary": "The main appeal of Nerva after the fall of Domitian was that he was an old man who would not be around for very long. His enduring legacy is that he did not blow it on the question of succession, prudently choosing the best man for the job in Trajan",
"rating": 6,
"children":[]
},
{
"id": 13,
"name": "Trajan",
"portrait": "/static/pic13.jpg",
"death":"Natural",
"reignstart": 98,
"reignend": 117,
"summary": "Perhaps Rome's greatest general since Julius Caesar, Trajan expanded Rome's borders to the greatest extent they would ever reach. Some would say that Trajan overextended the Empire, and indeed his son Hadrian willingly abandoned much of Trajan's eastern conquests, believing them impractical to rule. Transitory as his gains may have been, Trajan's rule represents the peak of Roman power, and a resurgent Persia would ensure that Roman troops never conquered further than Mesopotamia again",
"rating": 9,
"children":["Hadrian"]
},
{
"id": 14,
"name": "Hadrian",
"portrait": "/static/pic14.jpg",
"death":"Natural",
"reignstart": 117,
"reignend": 138,
"summary": "An oddball emperor, Hadrian took a unique approach to the throne, championing a national policy of peace in contrast to his predecessor Trajan, and consolidating power rather than expanding borders.",
"rating": 9,
"children":[]
},
{
"id": 15,
"name": "Antoninus",
"portrait": "/static/pic15.jpg",
"death":"Natural",
"reignstart": 138,
"reignend": 161,
"summary": "The luckiest emperor in Roman History, Antonius Pius barely had to have his hands on the wheel in order to preside over the most peaceful and plentiful period in Roman history.",
"rating": 8,
"children":[]
},
{
"id": 16,
"name": "Verus",
"portrait": "/static/pic16.jpg",
"death":"Natural",
"reignstart": 161,
"reignend": 169,
"summary": "The more debauched counterpart to his co-emperor Marcus Aurelus' stoic ideal, Verus was a more fun-loving emperor who still, for the most part, saw success as a general.",
"rating": 5,
"children":[]
},
{
"id": 17,
"name": "Marcus",
"portrait": "/static/pic17.jpg",
"death":"Natural",
"reignstart": 161,
"reignend": 180,
"summary": "The Philosopher King of Plato's dreams, Marcus Aurelius would have rather written than battled, but as a true stoic, did his duty during the Marcomanic wars and set a foundation for generations of peace on the western front.",
"rating": 10,
"children":["Commodus"]
},
{
"id": 18,
"name": "Commodus",
"portrait": "/static/pic18.jpg",
"death":"Natural",
"reignstart": 177,
"reignend": 192,
"summary": "You may know his as the villain from 'Gladiator'. Commodus was an egomaniac whose interest in affairs of state took a backseat to his interest in games.",
"rating": 3,
"children":[]
},
{
"id": 19,
"name": "Pertinax",
"portrait": "/static/pic19.jpg",
"death":"Natural",
"reignstart": 193,
"reignend": 193,
"summary": "After the coup which toppled Commodus, Pertinax was installed as a responsible senior official. However, Pertinax made the rookie mistake of not keeping his armies happy, which ended predictably in his downfall.",
"rating": 2,
"children":[]
},
{
"id": 20,
"name": "Didius",
"portrait": "/static/pic20.jpg",
"death":"Natural",
"reignstart": 193,
"reignend": 193,
"summary": "Didius is risibly remembered as the man who bought the throne at the Praetorian auction, and in doing so, signed his own death warrant.",
"rating": 1,
"children":[]
},
{
"id": 21,
"name": "Septimius",
"portrait": "/static/pic21.jpg",
"death":"Natural",
"reignstart": 193,
"reignend": 211,
"summary": "An austere but capable general, Severus established his own troubled dynasty, and brought back a measure of stability to the empire. His closest analog is Vespasian.",
"rating": 7,
"children":[]
},
{
"id": 22,
"name": "Caracalla",
"portrait": "/static/pic22.jpg",
"death":"Natural",
"reignstart": 209,
"reignend": 217,
"summary": "A brutal man, Caracalla courted the favor of the masses by extending citizenship to all men in the empire in a landmark declaration. However, this apparent generosity (although really just a ploy to increase tax revenue) did not rehabilitate his image as one of the worst emperors.",
"rating": 2,
"children":[]
},
{
"id": 23,
"name": "Getta",
"portrait": "/static/pic23.jpg",
"death":"Natural",
"reignstart": 209,
"reignend": 211,
"summary": "The unfortunate son of Severus, Getta's fierce and bitter rivalry with his co-emperor and brother Caracalla ended with his death by Caracalla's hands.",
"rating": 3,
"children":[]
},
{
"id": 24,
"name": "Macrinus",
"portrait": "/static/pic24.jpg",
"death":"Natural",
"reignstart": 217,
"reignend": 218,
"summary": "An unlikely emperor, Macrinus allegedly killed emperor Caracalla because of a prophecy which indicated that he, Macrinus, would be the next emperor. Rather than taking this prophecy as inspiration, Macrinus was simply scared that he would be executed if Caracalla heard tell of it, and preemptively struck in self-defense. This odd story is the only notable thing about Macrinus' reign, as he never made it to Rome, and was overthrown by a military coup within months",
"rating": 2,
"children":[]
},
{
"id": 25,
"name": "Elagabalus",
"portrait": "/static/pic25.jpg",
"death":"Natural",
"reignstart": 218,
"reignend": 222,
"summary": "The title of Weirdest Emperor is a hotly contested one, but Elagabalus certainly has a case. Just fourteen years old, Elegabalus' main policy initiative was to eliminate polytheism and establish the cult of the sun god Sol Invictus as the offical Roman religion. This might not seem much crazier than orienting the official religion around some Jewish prophet, but the change did not go over well.",
"rating": 2,
"children":[]
},
{
"id": 26,
"name": "Alexander",
"portrait": "/static/pic26.jpg",
"death":"Natural",
"reignstart": 222,
"reignend": 235,
"summary": "Another boy emperor, the kindest thing that can be said is that he was an earnest emperor who did his best to learn and to rule. However, his indecisiveness and general weakness as a general would eventually cost him the throne",
"rating": 4,
"children":[]
},
{
"id": 27,
"name": "Maximinus",
"portrait": "/static/pic27.jpg",
"death":"Natural",
"reignstart": 235,
"reignend": 238,
"summary": "The imposing Thracian military man had few friends except in the army upon seizing the throne, but really, the support of the army is typically plenty.",
"rating": 4,
},
{
"id": 28,
"name": "Gordian1",
"portrait": "/static/pic28.jpg",
"death":"Natural",
"reignstart": 238,
"reignend": 238,
"summary": "An old man, Gordian was essentially forced by his disaffected Carthaginian constituents into leading them in revolt, although he insisted upon his son sharing his power.",
"rating": 1,
"children":[]
},
{
"id": 29,
"name": "Gordian2",
"portrait": "/static/pic29.jpg",
"death":"Natural",
"reignstart": 238,
"reignend": 238,
"summary": "Thrust into power upon the ascent of his father, Gordian helped lead the North African revolt against Maximinus Thrax, but was very unsuccessful. He is noted for having the shortest reign of any emperor at only 21 days.",
"rating": 1,
"children":[]

},
{
"id": 30,
"name": "Pupienus",
"portrait": "/static/pic30.jpg",
"death":"Natural",
"reignstart": 238,
"reignend": 238,
"summary": "One of two men, along with Balbinus, to be pressured by the senate into heading up a Senatorial rebellion againt Maximinus Thrax.",
"rating": 1,
"children":[]
},
];

currsearched=[];

currviewed=[];

theterm=[];

created=[];




@app.route('/')
def home():
    return render_template('hw7home.html',recentsearches=recentsearches,currsearched=currsearched, currviewed=currviewed)

@app.route('/create')
def yello(name=None):
    return render_template('hw7create.html', created=created)


@app.route('/search/<id>')
def search(id):
    return render_template('hw7search.html', currsearched=currsearched, theterm=theterm, Emperors=Emperors, currviewed=currviewed)

@app.route('/view/<id>')
def view(id):
    return render_template('hw7view.html', currviewed=currviewed)



@app.route('/update_recent', methods=['GET', 'POST'])
def update_recent():
    global recentsearches
    global Emperors

    json_update = request.get_json()
    name= json_update["name"]
    found=0
    for x in recentsearches:
        if x["name"]==name:
            found=1

    if found==0:
        for y in Emperors:
            if y["name"]==name:
                recentsearches.pop()
                recentsearches.insert(0,y)

    return jsonify(recentsearches=recentsearches)


@app.route('/save_descrip_edit', methods=['GET', 'POST'])
def save_descrip_edit():
    global currviewed
    global recentsearches
    global Emperors

    json_edit = request.get_json()
    death= json_edit["death"]
    name= json_edit["name"]

    for x in recentsearches:
        if x["name"]==name:
            x["death"]=death

    for y in Emperors:
        if y["name"]==name:
            y["death"]=death


    currviewed[0]["death"]=death

    return jsonify(currviewed=currviewed)

@app.route('/save_rating_edit', methods=['GET', 'POST'])
def save_rating_edit():
    global currviewed
    global recentsearches
    global Emperors

    json_edit = request.get_json()
    name= json_edit["name"]
    rating= json_edit["rating"]


    for x in recentsearches:
        if x["name"]==name:
            x["rating"]=rating

    for y in Emperors:
        if y["name"]==name:
            y["rating"]=rating


    currviewed[0]["rating"]=rating

    return jsonify(currviewed=currviewed)

@app.route('/save_edit_child', methods=['GET', 'POST'])
def save_edit_child():
    global currviewed
    global recentsearches
    global Emperors
    json_edit = request.get_json()
    childpos= int(json_edit["childpos"])
    name= json_edit["name"]
    rename=name

    for x in recentsearches:
        if x["name"]==name:
            new="z"+x["children"][childpos]
            x["children"][childpos]=new
            currviewed[0]=x

    for y in Emperors:
        if y["name"]==name:
            new="z"+y["children"][childpos]
            y["children"][childpos]=new
            currviewed[0]=y


    return jsonify(currviewed=currviewed)

@app.route('/undo_edit_child', methods=['GET', 'POST'])
def undo_edit_child():
    global currviewed
    global recentsearches
    global Emperors
    json_edit = request.get_json()
    childpos= int(json_edit["childpos"])
    name= json_edit["name"]
    rename=name

    for x in recentsearches:
        if x["name"]==name:
            new=x["children"][childpos][1:]
            x["children"][childpos]=new
            currviewed[0]=x

    for y in Emperors:
        if y["name"]==name:
            new=y["children"][childpos][1:]
            y["children"][childpos]=new
            currviewed[0]=y    

    return jsonify(currviewed=currviewed)


@app.route('/viewview', methods=['GET', 'POST'])
def viewview():
    global Emperors
    global currviewed
    currviewed=[]
    json_view = request.get_json()
    viewid= json_view["viewid"]
    for emp in Emperors:
        if emp["id"]==viewid:
            currviewed.append(emp)

    return jsonify(currviewed = currviewed)

@app.route('/search/viewsearch', methods=['GET', 'POST'])
def viewsearch():
    global Emperors
    global currviewed
    currviewed=[]
    json_view = request.get_json()
    viewid= json_view["viewid"]
    for emp in Emperors:
        if emp["id"]==viewid:
            currviewed.append(emp)

    return jsonify(currviewed = currviewed)


@app.route('/searchdata', methods=['GET', 'POST'])
def searchdata():
    global currsearched
    global emperors
    global theterm
    currsearched=[];
    theterm=[];
    json_search = request.get_json()
    searchedname= json_search["searchedname"].lower()
    place=0

    theterm.append({"term":str(searchedname)})
    for emp in Emperors:
        if emp["name"].lower().find(searchedname.lower())>=0:
            currsearched.append({"name":str(emp["name"]),"place":emp["name"].find(searchedname),"death":str(emp["death"]),"which":"aname"})

        elif emp["death"].lower().find(searchedname.lower())>=0:
            currsearched.append({"name":str(emp["name"]),"place":emp["death"].find(searchedname),"death":str(emp["death"]),"which":"death"})



    return jsonify(currsearched=currsearched)

@app.route('/search/searchsearchdata', methods=['GET', 'POST'])
def searchsearchdata():
        global currsearched
        global Emperors
        global theterm
        currsearched=[];
        theterm=[];
        json_search = request.get_json()
        searchedname= json_search["searchedname"].lower()
        found=0

        theterm.append({"term":str(searchedname)})
        for emp in Emperors:
            if emp["name"].lower().find(searchedname)>=0:
                currsearched.append({"name":str(emp["name"]),"place":emp["name"].find(searchedname),"death":str(emp["death"]),"which":"aname"})
                found=1
            elif emp["death"].lower().find(searchedname)>=0:
                currsearched.append({"name":str(emp["name"]),"place":emp["death"].find(searchedname),"death":str(emp["death"]),"which":"death"})
                found=1


        if found==0:
            currsearched[0]={"name":"no","place":"nope"}

        return jsonify(currsearched=currsearched)

@app.route('/view/viewsearchdata', methods=['GET', 'POST'])
def viewsearchdata():
        global currsearched
        global Emperors
        global theterm
        currsearched=[];
        theterm=[];
        json_search = request.get_json()
        searchedname= json_search["searchedname"].lower()
        found=0

        theterm.append({"term":str(searchedname)})
        for emp in Emperors:
            if emp["name"].lower().find(searchedname)>=0:
                currsearched.append({"name":str(emp["name"]),"place":emp["name"].find(searchedname),"death":str(emp["death"]),"which":"aname"})
                found=1
            elif emp["death"].lower().find(searchedname)>=0:
                currsearched.append({"name":str(emp["name"]),"place":emp["death"].find(searchedname),"death":str(emp["death"]),"which":"death"})
                found=1


        if found==0:
            currsearched[0]={"name":"no","place":"nope"}

        return jsonify(currsearched=currsearched)


@app.route('/createsearchdata', methods=['GET', 'POST'])
def createsearchdata():
        global currsearched
        global Emperors
        global theterm
        currsearched=[];
        theterm=[];
        json_search = request.get_json()
        searchedname= json_search["searchedname"].lower()
        found=0

        theterm.append({"term":str(searchedname)})
        for emp in Emperors:
            if emp["name"].lower().find(searchedname)>=0:
                currsearched.append({"name":str(emp["name"]),"place":emp["name"].find(searchedname),"death":str(emp["death"]),"which":"aname"})
                found=1
            elif emp["death"].lower().find(searchedname)>=0:
                currsearched.append({"name":str(emp["name"]),"place":emp["death"].find(searchedname),"death":str(emp["death"]),"which":"death"})
                found=1


        if found==0:
            currsearched[0]={"name":"no","place":"nope"}

        return jsonify(currsearched=currsearched)





@app.route('/save_create', methods=['GET', 'POST'])
def save_create():
    global Emperors
    global created
    global currviewed
    created=[]
    currviewed=[]
    json_create = request.get_json()
    name= json_create["name"]
    death= json_create["death"]
    reigns= json_create["reigns"]
    reigne= json_create["reigne"]
    descrip= json_create["descrip"]
    rating= json_create["rating"]
    id= json_create["id"]
    portrait=json_create["portrait"]
    children=json_create["children"]


    # add new entry to array with
    # a new id and the name the user sent in JSON
    new_create_entry = {
        "id":  id,
        "name": name,
        "death":death,
        "portrait":portrait,
        "reignstart":reigns,
        "reignend":reigne,
        "summary":descrip,
        "rating":rating,
        "children":children


    }
    Emperors.append(new_create_entry)
    created.append(new_create_entry)
    currviewed.append(new_create_entry)

    #send back the WHOLE array of data, so the client can redisplay it
    return jsonify(created = created)



















if __name__ == '__main__':
	app.run(debug=True)
