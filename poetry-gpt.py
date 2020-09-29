import gpt_2_simple as gpt2
import os
import requests
import tensorflow as tf

model_name = "124M"
if not os.path.isdir(os.path.join("models", model_name)):
	print(f"Downloading {model_name} model...")
	gpt2.download_gpt2(model_name=model_name)   # model is saved into current directory under /models/124M/


file_name = "poe.txt"
if not os.path.isfile(file_name):
	url = "http://www.gutenberg.org/cache/epub/10031/pg10031.txt"
	data = requests.get(url)
	
	with open(file_name, 'w') as f:
		f.write(data.text)
    
sess = gpt2.start_tf_sess()

gpt2.finetune(sess,
              file_name,
              model_name=model_name,
              steps=1000)   # steps is max number of training steps

gpt2.generate(sess)
