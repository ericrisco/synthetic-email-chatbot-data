import pandas as pd
import random
import uuid
from datetime import datetime, timedelta

def random_id():
    return str(uuid.uuid4())

def random_message():
    chatbot_messages = {
        "es": {
            "call drop": "Mi llamada se cortó de repente.",
            "can’t receive texts": "No puedo recibir mensajes de texto.",
            "can’t send texts": "Mis mensajes no se envían.",
            "data not working": "Mis datos no están funcionando.",
            "internet slow": "El internet está muy lento.",
            "no 4G": "No tengo señal 4G aquí.",
            "no signal": "He perdido la señal por completo.",
            "password reset": "Necesito restablecer mi contraseña.",
            "phone lost": "Perdí mi teléfono. ¿Qué puedo hacer?",
            "phone unlock": "¿Cómo puedo desbloquear mi teléfono?",
            "SIM card activation": "¿Cómo activo mi tarjeta SIM?",
            "wifi problem": "Mi wifi no conecta."
        },
        "en": {
            "call drop": "My call just dropped.",
            "can’t receive texts": "I can't receive any texts.",
            "can’t send texts": "My texts aren't sending.",
            "data not working": "My data isn't working.",
            "internet slow": "The internet is crawling.",
            "no 4G": "I don't seem to have 4G here.",
            "no signal": "I've lost signal entirely.",
            "password reset": "I need to reset my password.",
            "phone lost": "I've lost my phone. What should I do?",
            "phone unlock": "How can I unlock my phone?",
            "SIM card activation": "How do I activate my SIM card?",
            "wifi problem": "My wifi isn't connecting."
        },
        "fr": {
            "call drop": "Mon appel vient d'être interrompu.",
            "can’t receive texts": "Je ne reçois pas de textos.",
            "can’t send texts": "Mes textos ne s'envoient pas.",
            "data not working": "Mes données ne fonctionnent pas.",
            "internet slow": "L'internet est très lent.",
            "no 4G": "Je n'ai pas de 4G ici.",
            "no signal": "J'ai perdu le signal.",
            "password reset": "Je dois réinitialiser mon mot de passe.",
            "phone lost": "J'ai perdu mon téléphone. Que faire?",
            "phone unlock": "Comment puis-je déverrouiller mon téléphone?",
            "SIM card activation": "Comment activer ma carte SIM?",
            "wifi problem": "Mon wifi ne se connecte pas."
        },
        "de": {
            "call drop": "Mein Anruf wurde plötzlich abgebrochen.",
            "can’t receive texts": "Ich kann keine SMS empfangen.",
            "can’t send texts": "Meine SMS werden nicht gesendet.",
            "data not working": "Meine Daten funktionieren nicht.",
            "internet slow": "Das Internet ist sehr langsam.",
            "no 4G": "Ich habe hier kein 4G.",
            "no signal": "Ich habe das Signal komplett verloren.",
            "password reset": "Ich muss mein Passwort zurücksetzen.",
            "phone lost": "Ich habe mein Handy verloren. Was soll ich tun?",
            "phone unlock": "Wie kann ich mein Handy entsperren?",
            "SIM card activation": "Wie aktiviere ich meine SIM-Karte?",
            "wifi problem": "Mein WLAN verbindet nicht."
        }
    }
    lang = random.choice(list(chatbot_messages.keys()))
    category = random.choice(list(chatbot_messages[lang].keys()))
    message = chatbot_messages[lang][category]
    return message, lang, category

messages_multilang = {
    "en": [
        "Hello! We regret to hear about the issues. We are here to assist you.",
        "Thank you for your positive feedback. We're delighted you're enjoying our service.",
        "Your bill is being reviewed. We'll rectify any discrepancies shortly.",
        "We're actively working on enhancing the network coverage. Thanks for your patience.",
        "Your concerns are valid. We'll reach out to address them.",
        "Your past bills can be viewed on our online portal.",
        "Apologies for the delay. We're experiencing a high volume of inquiries."
    ],
    "es": [
        "¡Hola! Lamentamos escuchar sobre los problemas. Estamos aquí para ayudarte.",
        "Gracias por tus comentarios positivos. Nos alegra que disfrutes de nuestro servicio.",
        "Estamos revisando tu factura. Corregiremos cualquier discrepancia en breve.",
        "Estamos trabajando activamente para mejorar la cobertura de la red. Gracias por tu paciencia.",
        "Tus preocupaciones son válidas. Nos pondremos en contacto para abordarlas.",
        "Puedes ver tus facturas anteriores en nuestro portal en línea.",
        "Disculpas por el retraso. Estamos experimentando un alto volumen de consultas."
    ],
    "fr": [
        "Bonjour! Nous regrettons d'entendre parler des problèmes. Nous sommes ici pour vous aider.",
        "Merci pour vos commentaires positifs. Nous sommes ravis que vous appréciiez notre service.",
        "Votre facture est en cours de révision. Nous rectifierons toute anomalie sous peu.",
        "Nous travaillons activement à améliorer la couverture du réseau. Merci de votre patience.",
        "Vos préoccupations sont valides. Nous vous contacterons pour les aborder.",
        "Vous pouvez consulter vos factures précédentes sur notre portail en ligne.",
        "Nos excuses pour le retard. Nous connaissons un volume élevé de demandes."
    ],
    "de": [
        "Hallo! Es tut uns leid von den Problemen zu hören. Wir sind hier, um Ihnen zu helfen.",
        "Vielen Dank für Ihr positives Feedback. Wir freuen uns, dass Sie unseren Service genießen.",
        "Ihre Rechnung wird überprüft. Wir werden Unstimmigkeiten in Kürze beheben.",
        "Wir arbeiten aktiv daran, die Netzabdeckung zu verbessern. Vielen Dank für Ihre Geduld.",
        "Ihre Bedenken sind berechtigt. Wir werden uns mit Ihnen in Verbindung setzen, um sie zu klären.",
        "Sie können Ihre früheren Rechnungen auf unserem Online-Portal einsehen.",
        "Entschuldigung für die Verzögerung. Wir haben ein hohes Anfragevolumen."
    ]
}

def random_sentiment(message, lang):
    sentiment_keywords = {
        "en": {
            "positive": ["excellent", "great", "happy", "satisfied", "enjoying"],
            "negative": ["problem", "ridiculous", "pathetic", "unstable", "cancel", "lost", "slow", "issue"]
        },
        "es": {
            "positive": ["excelente", "genial", "feliz", "satisfecho", "disfrutando"],
            "negative": ["problema", "ridículo", "patético", "inestable", "cancelar", "perdí", "lento", "problema"]
        },
        "fr": {
            "positive": ["excellent", "super", "heureux", "satisfait", "appréciant"],
            "negative": ["problème", "ridicule", "pathétique", "instable", "annuler", "perdu", "lent", "problème"]
        },
        "de": {
            "positive": ["ausgezeichnet", "großartig", "glücklich", "zufrieden", "genießen"],
            "negative": ["problem", "lächerlich", "erbärmlich", "instabil", "abbrechen", "verloren", "langsam", "problem"]
        }
    }
    
    for word in sentiment_keywords[lang]["positive"]:
        if word in message:
            return "positive"
    
    for word in sentiment_keywords[lang]["negative"]:
        if word in message:
            return "negative"
    
    return "mixed"

def random_moment():
    end_date = datetime.now()
    start_date = end_date - timedelta(days=365)
    random_date = start_date + timedelta(seconds=random.randint(0, int((end_date - start_date).total_seconds())))
    return random_date.strftime('%m/%d/%Y %I:%M %p')

def random_negative_percentual(sentiment):
    if sentiment == "positive":
        return random.uniform(0, 0.3)
    elif sentiment == "negative":
        return random.uniform(0.5, 1)
    else:
        return random.uniform(0.3, 0.5)

def random_response_by_language(lang):
    return random.choice(messages_multilang[lang])

records = []
for _ in range(10000):
    message, lang, category = random_message()
    sentiment = random_sentiment(message, lang)
    negative_percentual = random_negative_percentual(sentiment)
    response = random_response_by_language(lang) if negative_percentual >= 0.5 else None
    
    record = {
        "Id": random_id(),
        "Message": message,
        "Moment": random_moment(),
        "Response": response,
        "Sentiment": sentiment,
        "NegativePercentual": negative_percentual,
        "Topic": category,
        "Langguage": lang
    }
    records.append(record)

df = pd.DataFrame(records)
file_path = "C:/MasterIA/chatbot.xlsx"
df.to_excel(file_path, index=False)