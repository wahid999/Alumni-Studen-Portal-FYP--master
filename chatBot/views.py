from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import nltk
# nltk.download()

from nltk.stem.lancaster import LancasterStemmer
stemmer=LancasterStemmer()
import numpy
import tensorflow
import tflearn
import random
import json
import pickle
import os
from django.conf import settings
@csrf_exempt
def index(request):

    if request.method == 'POST':
        text = request.POST.get('text')
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        path = os.path.join(BASE_DIR, 'static/intents.json')
        with open(path) as file:
            data = json.load(file)
        try:
            with open("data1.pickle", "rb") as f:
                
                words,labels,training,output=pickle.load(f)
        except:
            words=[]
            labels=[]
            docs_x=[]  
            docs_y=[]
            for intent in data["intents"]:
                for pattern in intent["patterns"]:
                    wrd=nltk.word_tokenize(pattern)
                    words.extend(wrd)
                    docs_x.append(wrd)
                    docs_y.append(intent["tag"])
                if intent["tag"] not in labels:
                        labels.append(intent["tag"])
            words=[stemmer.stem(w.lower()) for w in words]
            words=sorted(list(set(words)))
            labels=sorted(labels)


            training=[]
            output=[]
            out_empty=[0 for _ in range(len(labels))]
            for x, doc in enumerate(docs_x):
                bag=[]
                wrds=[stemmer.stem(w) for w in doc if w not in "?"]
                for w in words:
                    if w in wrds:
                        bag.append(1)
                    else:
                        bag.append(0)
                output_row=out_empty[:]
                output_row[labels.index(docs_y[x])]=1
                training.append(bag)
                output.append(output_row)
            training=numpy.array(training)
            output=numpy.array(output) #converted into arrary
     
        with open("data1.pickle","wb") as f:
                pickle.dump((words, labels, training, output), f)

        tensorflow.reset_default_graph()
        net=tflearn.input_data(shape=[None,len(training[0])])
        net =tflearn.fully_connected(net,8)
        net =tflearn.fully_connected(net,8)
        net =tflearn.fully_connected(net,len(output[0]),activation="softmax")
        net =tflearn.regression(net)
        model = tflearn.DNN(net)

        try:
            model.load('model1.tflearn')

        except:
            model.fit(training,output,n_epoch=1000,batch_size=8,show_metric=True)#training model
            model.save("model1.tflearn")

        def bag_of_word(s,words):
            bags=[0 for _ in range(len(words))]
            s_words=nltk.word_tokenize(s)
            s_words=[stemmer.stem(word.lower()) for word in s_words]

            for se in s_words:
                for i,w in enumerate(words):
                    if w==se:
                        bags[i]=1
            return numpy.array(bags)

        def chat():
            # print("Wellcome to ChatBot ,How can i help you?")
            results= model.predict([bag_of_word(text,words)])[0]
            results_index = numpy.argmax(results)
            tag = labels[results_index]
            # print(results_index,results_index)
            if results[results_index]>0.6:   
                for tg in data["intents"]:
                    if tg['tag']==tag:
                        responses=tg['responses']
                        return random.choice(responses)
            else:
                    
                return "i didn't get what are you saying..! try again"

        ans = chat()
        print(ans)      
        data = {'text': ans}
        return JsonResponse(data,safe=False)
    return render(request,'index.html')