
import PyPDF2
import textract
import re
from abc import ABC, abstractmethod
import os
#import spacy 
#nlp = spacy.load('sample_work_model_300_drop_0.05')
#from Entity import Entities,display_attributes


class converter(ABC):

	def get_document_format(self):
		pass

	def set_conversion_algo(self):
		pass

	def convert_to_text(document):
		pass
	
	def post_process(self,text):
		pass
	
	def pre_process(self):
		pass

	# def save_converted_file(self,document_path,text):
	# 	path=os.path.splitext(document_path)[0] + ".txt"
	# 	file=open(path,"w+")
		
	# 	file.write(text)
	# 	print("hello from save")		
	# 	file.close()
	def get_document_type(self):
		pass

class pdf_converter(converter):

	def convert_to_text(self,document_path):
		
		document=open(document_path,'rb')
		pdfReader = PyPDF2.PdfFileReader(document)
		num_pages = pdfReader.numPages
		print(num_pages)
		count = 0
		text = ""
		path=os.path.splitext(document_path)[0].split('/')[-1] + ".txt"
		file=open(path,"w+")
		
		print("here Normal")
		
		while count < num_pages:
			pageObj = pdfReader.getPage(count)
			count +=1
			c=pageObj.extractText()
			text += c
			file.write(c)
			#print(text)
		
		#print("hello from save")		
		file.close()


class image_converter(converter):

	def post_process(self,text):
		text= re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f\x7f-\xff]', '', text.decode("utf-8"))
		#text = re.sub(r'\n', '', text)
		return(text)

	def convert_to_text(self,document_path): ## testeract
		print("tesseract")
		text = textract.process(document_path, method='tesseract', language='eng') 
		text= self.post_process(text)
		path=os.path.splitext(document_path)[0].split('/')[-1] + ".txt"
		file=open(path,'w+')
		file.write(text)
		file.close()
		 
		 

	


## benchmarking it would help

## Dependency layer
class Interface():
	def get_instance(self,format):
		if format=='PDF':
			return(pdf_converter())
		else:
			return(image_converter())

	def get_text(self,instance,document_path):
		text=instance.convert_to_text(document_path)

		#instance.save_converted_file(document_path,text)


# pdfFileObj=open('pdf_fortest/P4.pdf','rb')
#with open('pdf_fortest/P4.pdf','rb') as f:
# 	document=f.read()



# pdfFileObj1=open('pdf_fortest/P3.pdf','rb')


# i=Interface()

 

# #################################### Benchmarking ###################################

# def test(doc):
# 	obj = Entities()
# 	mapping = obj.results(doc)
# 	df = obj.results_to_df(mapping)
# 	entities=df.to_dict('dict')
	    
# 	tup=[]
# 	for j in entities.values():
#  		tup.append(j[0])

# 	print(tup)

#i=image_converter()
# #doc=nlp(document)
#i.convert_to_text(document)

# #print("Original document")
# #test(doc)
# print("processed and Obtained")
# test(doc1)



# import pytesseract
# import cv2
# import re
 
# def ocr(img_path):
#     img = cv2.imread(img_path)
#     text = pytesseract.image_to_string(img,lang='eng',config='--psm 6')
#     #out_file = re.sub(".png",".txt",img_path.split("\\")[-1])
#     #out_path = out_dir + out_file
#     #fd = open(out_path,"w")
#     #fd.write("%s" %text)
#     #return out_file



#     print(text)

 
#p=pdf_converter()

#print(p.convert_to_text('media/docs/feature_doc.pdf'))
#pdfFileObj1=open('Source/pdf_fortest/P3.pdf','rb')
#print(p.convert_to_text('Source/pdf_fortest/P3.pdf'))