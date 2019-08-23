import spacy
import json
import logging
import random

def convert_dataturks_to_spacy(dataturks_JSON_FilePath):
    try:
        training_data = []
        lines=[]
        with open(dataturks_JSON_FilePath, 'r',encoding="UTF-8") as f:
            lines = f.readlines()

        for line in lines:

            data = json.loads(line)
            text = data['content']
            entities = []
            
            if(type(data['annotation']) != type(None)):
            
                for annotation in data['annotation']:
                    
                    point = annotation['points'][0]
                    labels = annotation['label']
                    
                    if not isinstance(labels, list):
                        labels = [labels]

                    for label in labels:
                        
                        entities.append((point['start'], point['end'] + 1 ,label))


                training_data.append((text, {"entities" : entities}))

        return training_data
    except Exception as e:
        logging.exception("Unable to process " + dataturks_JSON_FilePath + "\n" + "error = " + str(e))
        return None


#data = convert_dataturks_to_spacy("Sample_work_310.json")

def train_spacy(train_data):
    TRAIN_DATA = train_data
    nlp = spacy.blank('en')  
    if 'ner' not in nlp.pipe_names:
        ner = nlp.create_pipe('ner')
        nlp.add_pipe(ner, last=True)

   
    for text, annotations in TRAIN_DATA:
        for ent in annotations.get('entities'):
            ner.add_label(ent[2])

    
    other_pipes = [pipe for pipe in nlp.pipe_names if pipe != 'ner']
    with nlp.disable_pipes(*other_pipes):  
        optimizer = nlp.begin_training()
        for itn in range(50): # epoch number
            print("Starting iteration " + str(itn))
            random.shuffle(TRAIN_DATA)
            losses = {}
            for text, annotations in TRAIN_DATA:
                
                nlp.update(
                    [text],  
                    [annotations],  
                    drop=0.05,  
                    sgd=optimizer,  
                    losses=losses)
            print(losses)
    nlp.to_disk('sample_work_model_125_drop_0.05')

#train_spacy(train_data)
#nlp = spacy.load('sample_work_model_300_drop_0.05')

# Testing 

def convert_dataturks_to_spacy_test(dataturks_JSON_FilePath):
    try:
        training_data = []
        lines=[]
        with open(dataturks_JSON_FilePath, 'r',encoding="UTF-8") as f:
            lines = f.readlines()

        for line in lines:

            data = json.loads(line)
            text = data['content']
            entities = []
            
            if(type(data['annotation']) == type(None)):
                training_data.append((text))

        return training_data
    except Exception as e:
        logging.exception("Unable to process " + dataturks_JSON_FilePath + "\n" + "error = " + str(e))
        return None


# In[4]:


#test = convert_dataturks_to_spacy_test("Sample_work_all.json")
#len(test)
