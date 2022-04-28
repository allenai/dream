# DREAM

This is repository for our recent paper DREAM: Improving Situational QA by First Elaborating the Situation, NAACL 2022 (https://arxiv.org/abs/2112.08656)

## Dataset Creation:
The script to compile Scene Elaboration (SE) dataset from existing commonsense resources is provided in two formats. 

(1) For the script in Jupyter Notebook format (.ipynb), follow the instructions in the Markdown to download the source data and run each cell in the notebook.
You should end up with the same 3 subdirectories in your "external_data" folder as in the instructions below.


(2) For the python script (.py), when running the script, first create a folder in the same directory named "external_data/", and download the source data:

```Instructions to download the Social Chemistry dataset:
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

This script will compile Scene Elaboration dataset in folder: external_data_tidied_combined_used_to_train_DREAM

## DREAM Model:
Our T5-11B model is available in HuggingFace PyTorch format at:
https://beaker.org/ds/01FMN19KY0SZQQHAG1JECDFVH4

For additional instructions about using the DREAM model and sample commands, please refer to https://github.com/allenai/dream/blob/main/DREAM_model_instructions/README_DREAM_model.md.


# Citation
```
@article{dreamnaacl2022,
  title={DREAM: Improving Situational QA by First Elaborating the Situation},
  author={Gu, Yuling and Dalvi Mishra, Bhavana, and Clark, Peter},
  journal={NAACL},
  year={2022}
}
```

