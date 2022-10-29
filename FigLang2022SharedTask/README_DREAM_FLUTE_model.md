# Downloading and running the DREAM-FLUTE models

This is documentation on our suggestions as to how to run the models from our paper Just-DREAM-about-it: Figurative Language Understanding with DREAM-FLUTE, FigLang workshop @ EMNLP 2022 (Arxiv link: TBD), where we acheved joint first position in the figurative language understanding shared task.

## Setup
The setup required to run the DREAM-FLUTE is the same as that for DREAM. Please refer the same instructions (https://github.com/allenai/dream/blob/main/model/README_DREAM_model.md) for installing the requirements inside a conda environment.

## Accessing the model
We also make all models available on HuggingFace: 

* https://huggingface.co/allenai/System1_FigLang2022
* https://huggingface.co/allenai/System2_FigLang2022
* https://huggingface.co/allenai/System3_DREAM_FLUTE_emotion_FigLang2022
* https://huggingface.co/allenai/System3_DREAM_FLUTE_motivation_FigLang2022
* https://huggingface.co/allenai/System3_DREAM_FLUTE_consequence_FigLang2022
* https://huggingface.co/allenai/System3_DREAM_FLUTE_social_norm_FigLang2022
* https://huggingface.co/allenai/System3_DREAM_FLUTE_all_dimensions_FigLang2022
* https://huggingface.co/allenai/System4_classify_FigLang2022
* https://huggingface.co/allenai/System4_explain_FigLang2022

## Load and use the models
For each model, we provide a quick example of how to load and use it.

### System 1: Using original data

```
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
model = AutoModelForSeq2SeqLM.from_pretrained("allenai/System1_FigLang2022")

tokenizer = AutoTokenizer.from_pretrained("t5-3b")
input_string = "Premise: My neighbor actually purchased a dream car of mine and I see it parked in his driveway everyday just taunting me. Hypothesis: My neighbor's new car is exactly my dream car, and I feel so happy every time I see it parked in his driveway. Is there a contradiction or entailment between the premise and hypothesis?"
input_ids = tokenizer.encode(input_string, return_tensors="pt")
output = model.generate(input_ids, max_length=200)
tokenizer.batch_decode(output, skip_special_tokens=True)

```

### System 2: Jointly predicting the type of figurative language

```
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
model = AutoModelForSeq2SeqLM.from_pretrained("allenai/System2_FigLang2022")

tokenizer = AutoTokenizer.from_pretrained("t5-3b")
input_string = "Premise: Yesterday two gangs were fighting just in front of my home. Hypothesis: Yesterday I saw two gangs fighting right in front of my house and it totally didn't make me scared at all. What is the type of figurative language involved? Is there a contradiction or entailment between the premise and hypothesis?"
input_ids = tokenizer.encode(input_string, return_tensors="pt")
output = model.generate(input_ids, max_length=200)
tokenizer.batch_decode(output, skip_special_tokens=True)

```

### Systems 3: DREAM-FLUTE - Providing DREAM’s different dimensions as input context

DREAM-FLUTE (emotion)
```
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
model = AutoModelForSeq2SeqLM.from_pretrained("allenai/System3_DREAM_FLUTE_emotion_FigLang2022")

tokenizer = AutoTokenizer.from_pretrained("t5-3b")
input_string = "Premise: we laid in the field of green grass and relaxed. [Premise - emotion] I (myself)'s emotion is happy. Hypothesis: we laid in fields of gold. [Hypothesis - emotion] I (myself)'s emotion is happy. Is there a contradiction or entailment between the premise and hypothesis?"
input_ids = tokenizer.encode(input_string, return_tensors="pt")
output = model.generate(input_ids, max_length=200)
tokenizer.batch_decode(output, skip_special_tokens=True)

```

DREAM-FLUTE (motivation)
```
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
model = AutoModelForSeq2SeqLM.from_pretrained("allenai/System3_DREAM_FLUTE_motivation_FigLang2022")

tokenizer = AutoTokenizer.from_pretrained("t5-3b")
input_string =  "Premise: After years of service and contribution to the company, he was finally promoted. [Premise - motivation] Company's motivation is to recognize his hard work. Hypothesis: The company released him after many years of service. [Hypothesis - motivation] Company's motivation is to get someone else to work. Is there a contradiction or entailment between the premise and hypothesis?"
input_ids = tokenizer.encode(input_string, return_tensors="pt")
output = model.generate(input_ids, max_length=200)
tokenizer.batch_decode(output, skip_special_tokens=True)
```

DREAM-FLUTE (consequence)
```
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
model = AutoModelForSeq2SeqLM.from_pretrained("allenai/System3_DREAM_FLUTE_consequence_FigLang2022")

tokenizer = AutoTokenizer.from_pretrained("t5-3b")
input_string = "Premise: My decision-making skills are not purely based on emotions and gut. [Premise - likely consequence] I make more balanced and informed decisions. Hypothesis: My personal feelings color my judgment in this case. [Hypothesis - likely consequence] I make a decision that is not in the best interests of the company. Is there a contradiction or entailment between the premise and hypothesis?"
input_ids = tokenizer.encode(input_string, return_tensors="pt")
output = model.generate(input_ids, max_length=200)
tokenizer.batch_decode(output, skip_special_tokens=True)
```

DREAM-FLUTE (social norm)
```
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
model = AutoModelForSeq2SeqLM.from_pretrained("allenai/System3_DREAM_FLUTE_social_norm_FigLang2022")

tokenizer = AutoTokenizer.from_pretrained("t5-3b")
input_string = "Premise: Sure ,he snorted just to make me feel even better about the already great situation. [Premise - social norm] It's good to make people feel better about a situation. Hypothesis: Sure, he snorted, just rub it in. [Hypothesis - social norm] It's rude to rub something in someone's face when they don't want to. Is there a contradiction or entailment between the premise and hypothesis?"
input_ids = tokenizer.encode(input_string, return_tensors="pt")
output = model.generate(input_ids, max_length=200)
tokenizer.batch_decode(output, skip_special_tokens=True)

```

DREAM-FLUTE (all 4 dimensions)
```
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
model = AutoModelForSeq2SeqLM.from_pretrained("allenai/System3_DREAM_FLUTE_all_dimensions_FigLang2022")

tokenizer = AutoTokenizer.from_pretrained("t5-3b")
input_string = "Premise: I was really looking forward to camping but now it is going to rain so I won't go. [Premise - social norm] It's okay to be disappointed when plans change. [Premise - emotion] I (myself)'s emotion is disappointed. [Premise - motivation] I (myself)'s motivation is to stay home. [Premise - likely consequence] I will miss out on a great experience and be bored and sad. Hypothesis: I am absolutely elated at the prospects of getting drenched in the rain and then sleep in a wet tent just to have the experience of camping. [Hypothesis - social norm] It's good to want to have new experiences. [Hypothesis - emotion] I (myself)'s emotion is excited. [Hypothesis - motivation] I (myself)'s motivation is to have fun. [Hypothesis - likely consequence] I am so excited that I forget to bring a raincoat and my tent gets soaked. Is there a contradiction or entailment between the premise and hypothesis?"
input_ids = tokenizer.encode(input_string, return_tensors="pt")
output = model.generate(input_ids, max_length=200)
tokenizer.batch_decode(output, skip_special_tokens=True)
```

### System 4: Two-step System - Classify then explain

Step1: Classify
```
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
model = AutoModelForSeq2SeqLM.from_pretrained("allenai/System4_classify_FigLang2022")

tokenizer = AutoTokenizer.from_pretrained("t5-3b")
input_string = "Premise: After releasing his rage he was like a ferocious wolf. Hypothesis: After letting off his rage he sat down like a lamb. Is there a contradiction or entailment between the premise and hypothesis? Answer : "
input_ids = tokenizer.encode(input_string, return_tensors="pt")
output = model.generate(input_ids, max_length=200)
tokenizer.batch_decode(output, skip_special_tokens=True)
```


Step2: Explain
```
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
model = AutoModelForSeq2SeqLM.from_pretrained("allenai/System4_explain_FigLang2022")

tokenizer = AutoTokenizer.from_pretrained("t5-3b")
input_string = "Premise: It is wrong to lie to children. Hypothesis: Telling lies to the young is like clippin the wings of a butterfly. Is there a contradiction or entailment between the premise and hypothesis? Answer : Entailment. Explanation : "
input_ids = tokenizer.encode(input_string, return_tensors="pt")
output = model.generate(input_ids, max_length=200)
tokenizer.batch_decode(output, skip_special_tokens=True)
```



