# The DREAM-series
This repository provides access to the data, code and model in our DREAM-series of works. This is a line of research where we make use of scene elaboration for building a "mental model" of situation given in input text. The relevant papers in the DREAM-series are: 

* DREAM: Improving Situational QA by First Elaborating the Situation, NAACL 2022 (Arxiv link: https://arxiv.org/abs/2112.08656, ACL Anthology link: https://aclanthology.org/2022.naacl-main.82/)
(Refer to section "DREAM" below.)

* Just-DREAM-about-it: Figurative Language Understanding with DREAM-FLUTE, FigLang workshop @ EMNLP 2022 (Arxiv link: TBD) (Joint first position in figurative language understanding shared task.)
(Refer to section "DREAM-FLUTE" below.)

By elaborating along key conceptual dimensions informed by cognitive science, story understanding and planning literature, our approach has shown to improve task performance on various tasks such as ETHICS, CODAH, Social IQA, and Figurate Language Understanding (FLUTE). Our approach is easily adaptable to other language models, and task-agnostic in format (e.g. QA or NLI) and domain (e.g. ethical decisions or figurative language understanding).


# DREAM

This repository provides access to the data and model used in our paper DREAM: Improving Situational QA by First Elaborating the Situation, NAACL 2022 (Arxiv link: https://arxiv.org/abs/2112.08656, ACL Anthology link: https://aclanthology.org/2022.naacl-main.82/)

## Dataset Creation:
The script to compile Scene Elaboration (SE) dataset from existing commonsense resources is provided in two formats. 

(1) For the script in Jupyter Notebook format (.ipynb), follow the instructions in the Markdown to download the source data and run each cell in the notebook.
You should end up with the same 3 subdirectories in your "external_data" folder as in the instructions below.


(2) For the python script (.py), when running the script, first create a folder in the same directory named "external_data/", and download the source data:

```
Instructions to download the Social Chemistry dataset:
1. Visit the website for the Social Chemistry project https://maxwellforbes.com/social-chemistry/ 
2. Scroll down to the "QUICK INFO" part, find the third column "DATA", "Social-Chem-101 Dataset 4.5M+ annotations 28 MB .zip" to "DOWNLOAD" the source data
3. Unzip the downloaded file and place it in "external_data" folder we created

Instructions to download the Story Commonsense dataset :
1. Visit the website for the Story Commonsense project https://uwnlp.github.io/storycommonsense/
2. At the top of the page, where the "Quick links" are, click "[download the data]"
3. Unzip the downloaded file and place it in "external_data" folder we created

Instructions to download the Moral Stories dataset :
1. The Moral Stories dataset is available at https://tinyurl.com/moral-stories-data
2. "Download" the compressed file from the link above 
3. Expand the downloaded file and place it in "external_data" folder we created
```

After downloading these, in your "external_data" folder, you should have the following 3 subdirectories:
```
moral_stories_datasets
social-chem-101
storycommonsense_data
```

Run the script as (we have used python v3.7 during development)
```
python data/compile_scene_elaboration_dataset.py
```

This script will compile Scene Elaboration dataset in the following folder: 
```
external_data_tidied_combined_used_to_train_DREAM
```

## DREAM Model:
Our T5-11B model is available in HuggingFace PyTorch format at:
https://beaker.org/ds/01FMN19KY0SZQQHAG1JECDFVH4

We also make the model available on HuggingFace:
https://huggingface.co/allenai/DREAM

For additional instructions about using the DREAM model and sample commands, please refer to https://github.com/allenai/dream/blob/main/model/README_DREAM_model.md.

# DREAM-FLUTE
We provide access to the code and models used in our paper Just-DREAM-about-it: Figurative Language Understanding with DREAM-FLUTE, FigLang workshop @ EMNLP 2022 (Arxiv link: TBD)

## Data Processing:
For details on how we make use of the training data provided in the FigLang2022 shared task, please refer to https://github.com/allenai/dream/blob/main/FigLang2022SharedTask/Process_Data_Train_Dev_split.ipynb.

## Models:
We made all models described in our paper available on the HuggingFace Model Hub. For links to the models, additional instructions about using the models and sample commands, please refer to https://github.com/allenai/dream/blob/main/FigLang2022SharedTask/README_DREAM_FLUTE_model.md.


# Citations
```
@inproceedings{gu-etal-2022-dream,
    title = "{DREAM}: Improving Situational {QA} by First Elaborating the Situation",
    author = "Gu, Yuling  and
      Dalvi, Bhavana  and
      Clark, Peter",
    booktitle = "Proceedings of the 2022 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies",
    month = jul,
    year = "2022",
    address = "Seattle, United States",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2022.naacl-main.82",
    doi = "10.18653/v1/2022.naacl-main.82",
    pages = "1115--1127",
}

Citation for DREAM-FLUTE coming soon! 
```

