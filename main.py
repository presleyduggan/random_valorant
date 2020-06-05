from flask import Flask
import random as random

app = Flask(__name__)
@app.route('/')
def givegun():
    guns = {
        1: "Bucky",
        2: "Marshall",
        3: "Judge",
        4: "Odin",
        5: "Shorty",
        6: "Ares",
        7: "Sheriff",
        8: "Frenzy",
        9: "3 Marshalls, 2 Shorties",
        10: "2 Sheriffs, 3 Ares",
        11: "OP (marshall if poor)",
        12: "Stinger",
        13: "Guardian",
        14: "3 Phantoms, 2 Vandals",
        15: "1 Vandal, 4 Shorties",
        16: "Ghost",
        17: "Stack/Rush A with Classic",
        18: "Judge -> run down mid",
        19: "Jack is IGL",
        20: "Apohl is IGL"
    }

    pistol = {
        1: "Armor",
        2: "Ghost",
        3: "Shorty",
        4: "Stack A w/ Shorty",
        5: "Stack B w/ Armor",
        6: "Frenzy",
        7: "Sheriff",
        8: "3 Sheriff, 2 Shorty",
        9: "No buy",
        10: "Ask all chat"
    }
    num = random.randint(1,20)
    pistol_num = random.randint(1,10)
    round_text = guns[num]
    pistol_text = pistol[pistol_num]
    blank = '<br/>'
    title = "VALORANT RANDOM GUN PICKER"
    line2 = "This Round: "
    return title + blank + blank+ line2+ round_text + blank + blank + "If Pistol Round: " + pistol_text
	

if __name__ == '__main__':
	app.run(host='127.0.0.1', port=8080, debug=True)