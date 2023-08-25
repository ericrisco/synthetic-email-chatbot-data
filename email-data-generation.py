import pandas as pd
import random
import uuid
from datetime import datetime, timedelta

messages_translations = {
    "es": [
        "Es absolutamente ridículo lo patético que es este servicio de internet. Pago una fortuna cada mes y ¿para qué?",
        "El servicio es excelente, no he tenido problemas desde que lo contraté.",
        "Mi factura llegó con un monto incorrecto. ¿Pueden ayudarme?",
        "La señal de internet es muy inestable en mi área.",
        "Quiero cancelar mi suscripción, no estoy satisfecho con el servicio.",
        "¿Dónde puedo revisar mis facturas anteriores?",
        "He intentado ponerme en contacto varias veces y no obtengo respuesta.",
        "El paquete que contraté no coincide con el servicio que recibo.",
        "¿Por qué mi velocidad de internet es tan baja?",
        "Tengo problemas con el pago en línea. ¿Pueden asistirme?"
    ],
    "en": [
        "It's absolutely ridiculous how pathetic this internet service is. I pay a fortune every month and for what?",
        "The service is excellent, I haven't had any issues since I subscribed.",
        "My bill came with an incorrect amount. Can you help me?",
        "The internet signal is very unstable in my area.",
        "I want to cancel my subscription, I'm not satisfied with the service.",
        "Where can I check my previous bills?",
        "I've tried to get in touch multiple times and get no response.",
        "The package I signed up for doesn't match the service I receive.",
        "Why is my internet speed so slow?",
        "I'm having issues with online payment. Can you assist?"
    ],
    "fr": [
        "C'est absolument ridicule à quel point ce service internet est pathétique. Je paie une fortune chaque mois et pour quoi?",
        "Le service est excellent, je n'ai eu aucun problème depuis que je l'ai souscrit.",
        "Ma facture est arrivée avec un montant incorrect. Pouvez-vous m'aider?",
        "Le signal internet est très instable dans ma région.",
        "Je veux annuler mon abonnement, je ne suis pas satisfait du service.",
        "Où puis-je consulter mes factures précédentes?",
        "J'ai essayé de me mettre en contact à plusieurs reprises et je n'obtiens pas de réponse.",
        "Le forfait pour lequel je me suis inscrit ne correspond pas au service que je reçois.",
        "Pourquoi ma vitesse internet est-elle si basse?",
        "J'ai des problèmes avec le paiement en ligne. Pouvez-vous aider?"
    ],
    "de": [
        "Es ist absolut lächerlich, wie erbärmlich dieser Internetdienst ist. Ich bezahle jeden Monat ein Vermögen und wofür?",
        "Der Service ist ausgezeichnet, ich hatte seit meiner Anmeldung keine Probleme.",
        "Meine Rechnung kam mit einem falschen Betrag. Können Sie mir helfen?",
        "Das Internetsignal in meiner Gegend ist sehr instabil.",
        "Ich möchte mein Abonnement kündigen, ich bin mit dem Service nicht zufrieden.",
        "Wo kann ich meine früheren Rechnungen einsehen?",
        "Ich habe mehrmals versucht, Kontakt aufzunehmen und erhalte keine Antwort.",
        "Das Paket, für das ich mich angemeldet habe, entspricht nicht dem Service, den ich erhalte.",
        "Warum ist meine Internetgeschwindigkeit so langsam?",
        "Ich habe Probleme mit der Online-Zahlung. Können Sie helfen?"
    ]
}

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


import uuid

def random_id():
    return f"<{str(uuid.uuid4())}@me.com>"

import random

def random_from():
    domains = ['gmail.com', 'yahoo.com', 'outlook.com', 'icloud.com', 'hotmail.com']
    name = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=random.randint(5,10)))
    return f"{name}@{random.choice(domains)}"

def random_message_and_language():
    lang = random.choice(list(messages_translations.keys()))
    message = random.choice(messages_translations[lang])
    return message, lang

def random_response_by_language(lang):
    return random.choice(messages_multilang[lang])

def random_moment():
    end_date = datetime.now()
    start_date = end_date - timedelta(days=365)
    random_date = start_date + timedelta(seconds=random.randint(0, int((end_date - start_date).total_seconds())))
    return random_date.strftime('%m/%d/%Y %I:%M %p')

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

def random_negative_percentual(sentiment):
    if sentiment == "positive":
        return random.uniform(0, 0.3)
    elif sentiment == "negative":
        return random.uniform(0.5, 1)
    else:
        return random.uniform(0.3, 0.5)

def random_topic():
    topics = ["ACCOUNT", "CANCELLATION_FEE", "CONTACT", "DELIVERY", "FEEDBACK", 
              "INVOICES", "ORDER", "PAYMENT", "REFUNDS", "SHIPPING"]
    return random.choice(topics)

records = []
for _ in range(10000):
    message, lang = random_message_and_language()
    sentiment = random_sentiment(message, lang)
    negative_percentual = random_negative_percentual(sentiment)
    response = random_response_by_language(lang) if negative_percentual >= 0.5 else None
    
    record = {
        "Id": random_id(),
        "From": random_from(),
        "Message": message,
        "Moment": random_moment(),
        "Response": response,
        "Sentiment": sentiment,
        "NegativePercentual": negative_percentual,
        "Topic": random_topic(),
        "Language": lang
    }
    records.append(record)


df = pd.DataFrame(records)
file_path = "C:/MasterIA/emails.xlsx"
df.to_excel(file_path, index=False)
