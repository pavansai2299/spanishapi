import spacy
from flask import Flask, request

app = Flask(__name__)

#nlp = spacy.load("en_core_web_md")
nlp = spacy.load("es_core_news_md")


@app.route('/getdetails', methods=['POST'])
def get_details():
    details = request.data.decode("utf-8")
    doc = nlp(details)
    #doc = nlp("Pavan Sai, Vamshi, Preethi are friends and I don't know about teja.")
    #data = dict()
    big_data = dict()
    i = 1
    for ent in doc.ents:
        # data["type"] = ent.label_
        # data["name"] = ent.text
        # print(data)
        big_data.setdefault(i, {})["type"] = ent.label_
        big_data.setdefault(i, {})["name"] = ent.text
        # big_data[i].append(data)
        #print(big_data)
        #print(ent.text, ent.label_)
        i += 1

    return big_data


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5010)
