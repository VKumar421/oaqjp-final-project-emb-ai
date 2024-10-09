import requests
import json
def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header= {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj= { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = myobj, headers=header)  
    formatted_response = json.loads(response.text)

    if response.status_code == 400:
        anger = None
        disgust = None
        fear = None
        joy = None
        sadness = None
        dominant_emotion = None
        return {'anger': anger, 'disgust': disgust, 'fear': fear, 'joy': joy, 
        'sadness': sadness, 'dominant_emotion': dominant_emotion}  

    dominant_emotion = ''
    dominant_emotion_value = 0
    anger = formatted_response['emotionPredictions'][0]['emotion']['anger']
    if dominant_emotion_value < anger:
        dominant_emotion = 'Anger'
        dominant_emotion_value = anger

    disgust = formatted_response['emotionPredictions'][0]['emotion']['disgust']
    if dominant_emotion_value < disgust:
        dominant_emotion = 'Disgust'
        dominant_emotion_value = disgust

    fear = formatted_response['emotionPredictions'][0]['emotion']['fear']
    if dominant_emotion_value < fear:
        dominant_emotion = 'Fear'
        dominant_emotion_value = fear

    joy = formatted_response['emotionPredictions'][0]['emotion']['joy']
    if dominant_emotion_value < joy:
        dominant_emotion = 'Joy'
        dominant_emotion_value = joy

    sadness = formatted_response['emotionPredictions'][0]['emotion']['sadness']
    if dominant_emotion_value < sadness:
        dominant_emotion = 'Sadness'
        dominant_emotion_value = sadness
    
    return {'anger': anger, 'disgust': disgust, 'fear': fear, 'joy': joy, 
    'sadness': sadness, 'dominant_emotion': dominant_emotion}  


