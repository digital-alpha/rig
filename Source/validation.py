import spacy
import json
import logging
import random
import re
import datefinder
import pandas as pd
import nltk

class Validate:
    # self.text is the document text
    # self.entities is the list of entities that are annotated along with the index of occurance
    def __init__(self, data):
        self.text = data[0]
        self.entities = data[1]['entities']
    
    def predicted_entities(self):
        predicted_list = []
        predicted_entities={}
        doc = nlp(self.text)
        if doc.ents:
            for ent in doc.ents:
                predicted_list.append(ent.label_)
            predicted_set = set(predicted_list)
            predicted_labels = list(predicted_set)
            for ent in doc.ents:
                if ent.label_ in predicted_entities.keys():
                    values=[predicted_entities[ent.label_]].append(ent.text)
                    predicted_entities[ent.label_]=values
                else:
                    predicted_entities[ent.label_]=[ent.text]
            #print(sorted(predicted_labels))
            return ([sorted(predicted_labels),predicted_entities])
    
    def true_entities(self):
        true_list = []
        true_entities={}
        if len(self.entities) != 0:
            for ix in range(len(self.entities)):
                true_list.append(self.entities[ix][2])
                if self.entities[ix][2] in true_entities.keys():
                    values=[true_entities[self.entities[ix][2]]].append(self.text[self.entities[ix][0]:self.entities[ix][1]])
                    true_entities[self.entities[ix][2]]=values
                else:
                    true_entities[self.entities[ix][2]]=[self.text[self.entities[ix][0]:self.entities[ix][1]]]
                
            true_set = set(true_list)
            true_labels = list(true_set)
            #print(sorted(true_labels))
            return([sorted(true_labels),true_entities])
        
    def calculate_accuracy(self):
        predictions = self.predicted_entities()
        true_labels = self.true_entities()
        count = 0
        for ix in range(len(predictions[0])):
            if(len(true_labels[0])>ix):
                if predictions[0][ix] in true_labels[0]:
                    count+=1
        accuracy = (count/len(true_labels[0]))*100  
        return accuracy
    
    def entity_accuracy(self):
        entitiy_dict={}
        predictions = self.predicted_entities()
        true_labels = self.true_entities()
        for ix in range(len(predictions[0])):
            if(len(true_labels[0])>ix):
                if predictions[0][ix] in true_labels[0]:
                    entitiy_dict[predictions[0][ix]]=[predictions[1][predictions[0][ix]],true_labels[1][predictions[0][ix]]]
        return(entitiy_dict)


# In[7]:


def check_validity(m): # here m is the dictionary output of the 
    count=0
    sample=['Role','Employee Name','Date of Agreement','End Date','Bonus','Notice Period','Other Compensation','Non Monetary Benefits','Health Insurance','401k','At will','Stock','Company Name','Address of Employee','Address of Company','Base Salary','Start Date','Supervisor Information','Vacation']
    for values in sample:    
        val=m[values]

        if val!=None:
            if len(val)==2:
                lar=len(val[0]) if len(val[0])>len(val[1]) else len(val[1])
                diff=((lar-nltk.edit_distance(val[0],val[1]))/lar)*100
                if diff!=100:
                    if val[1]== "None" and val[0]!="None":
                        print("Similarity in the two attributes of {}:{}".format(values,100))
                        #print(val[0]-val[1])
                        count+=1
                    if val[0] in val[1]:
                        count+=1

                        print("Similarity in the two attributes of {}:{}".format(values,100))
                        #print(val[0]-val[1])
                    else:
                        print("Similarity in the two attributes of {}:{}".format(values,diff))

                else:
                        count+=1
                        print("Similarity in the two attributes of {}:{}".format(values,diff))
            else:
                if len(val)==1:
                    print("Similarity in the two attributes of {}:{}".format(values,100))


# In[39]:


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


# In[49]:


# Validation dataset
#data = convert_dataturks_to_spacy("New_Dataset_Employee.json")


# In[ ]:


# to calculate the average of the validation test
#sum1=0
#count=0
#for i in range(len(data)):
#    v = Validate(data[i])
#    sum1+=v.calculate_accuracy()
#    count+=1
#    print(v.calculate_accuracy())
#print("final Average:{}".format(sum1/count))


# In[23]:


# to check validity of a document
#doc=nlp(data[5][0])
#v = Validate(data[5])
#obj1= Entities()
#m = obj1.results(doc,v.entity_accuracy())
#check_validity(m)


# In[39]: