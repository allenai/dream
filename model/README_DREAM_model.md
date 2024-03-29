# Downloading and running the DREAM model

This is documentation on our suggestions as to how to run the model from our paper DREAM: Improving Situational QA by First Elaborating the Situation, NAACL 2022 (Arxiv link: https://arxiv.org/abs/2112.08656, ACL Anthology link: https://aclanthology.org/2022.naacl-main.82/)


## Download the model
You can directly click on the files on https://beaker.org/ds/01FMN19KY0SZQQHAG1JECDFVH4/details to download. Alternatively, you can also use the Beaker (https://github.com/beaker/docs) command line as follows:
```
$ beaker dataset fetch 01FMN19KY0SZQQHAG1JECDFVH4 -o dream_model_download
```
(You may replace "dream_model_download" with a folder name of your preference. This is where the model will be downloaded to.)

We also make the model available on HuggingFace: https://huggingface.co/allenai/DREAM. Feel free to skip the above download steps if you wish to load it from the Model Hub using code (see below, the alternative way of "Running the model").


## Install conda (if you don't have it)
```
$ wget https://repo.anaconda.com/archive/Anaconda3-2019.10-Linux-x86_64.sh
$ chmod +x Anaconda*.sh
$ sh Anaconda*.sh
$ export PATH=/home/$USER/anaconda3/bin/:$PATH
```

## Create a conda environment
You'll need to install PyTorch and Transformers to use the model. The following code snippet installs the requirements inside a conda environment. The requirements.txt file can be found in this same folder as this README.
```
$ conda create -n dream python=3.7
$ conda activate dream
$ python3.7 -m pip install -r requirements.txt
```


## Running the model
Using the transformers library, you can load the downloaded model as such in python (if you downloaded the model locally):

```
>>> from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
>>> model = AutoModelForSeq2SeqLM.from_pretrained("/home/yulingg/dream_model_download") # can take a couple minutes, be patient!
>>> tokenizer = AutoTokenizer.from_pretrained("t5-11b")
```

Alternatively, you can also load it from the HuggingFace Model Hub:
```
>>> from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
>>> model = AutoModelForSeq2SeqLM.from_pretrained("allenai/DREAM") # NOTE: COMPARED TO ABOVE, THE ONLY DIFFERENCE IS IN THIS LINE
>>> tokenizer = AutoTokenizer.from_pretrained("t5-11b")
```



Ex.1 (Rule of thumb dimension)
```
>>> input_string = "$answer$ ; $question$ = [SITUATION] hitting someones car in the drive thru on purpose. [QUERY] rot"
>>> input_ids = tokenizer.encode(input_string, return_tensors="pt")
>>> output = model.generate(input_ids, max_length=200)
>>> tokenizer.batch_decode(output, skip_special_tokens=True)
["$answer$ = It's wrong to damage other people's property."]
```

Ex.2 (Consequence dimension)
```
>>> input_string = "$answer$ ; $question$ = [SITUATION] hitting someones car in the drive thru on purpose. [QUERY] consequence"
>>> input_ids = tokenizer.encode(input_string, return_tensors="pt")
>>> output = model.generate(input_ids, max_length=200)
>>> tokenizer.batch_decode(output, skip_special_tokens=True)
['$answer$ = [immoral_consequence] You get a ticket and the owner of the car takes you to court.']
```

As discussed in our paper, DREAM supports the following possible dimensions for each input situation S:
```
1. M : motivation of character(s) before S.
2. E: emotion of character(s) after S.
3. ROT : general Rule of Thumb (ROT) about whether action described in S is socially acceptable or not (also known as social norm).
4. Con: likely consequence of action in S.
```
To get DREAM's output for these dimensions, use the corresponding terms below after the "[QUERY] " tag in your input string:
```
motivation
emotion
rot
consequence
```


The code above has been tested with transformers==4.24.0 and torch==1.13.0.