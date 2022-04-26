# DREAM

This is repository for our recent paper DREAM: Improving Situational QA by First Elaborating the Situation, NAACL 2022 (https://arxiv.org/abs/2112.08656)

## Dataset Creation:
The script for Scene Elaboration (SE) dataset creation is provided in two formats. 

For the script in Jupyter Notebbook format (.ipynb), follow the instructions in the Markdown to download the source data and run each cell in the notebook.


For the python script, when running the script, first create a folder in the same directory named "External_data/", and download the source data:
Instructions to download the Social Chemistry dataset:
1. Visit the website for the Social Chemistry project https://maxwellforbes.com/social-chemistry/ 
2. Scroll down to the "QUICK INFO" part, find the third column "DATA", "Social-Chem-101 Dataset 4.5M+ annotations 28 MB .zip" to "DOWNLOAD" the source data
3. Unzip the downloaded file and place it in "External_data" folder we created
Instructions to download the Story Commonsense dataset :
1. Visit the website for the Story Commonsense project https://uwnlp.github.io/storycommonsense/
2. At the top of the page, where the "Quick links" are, click "[download the data]"
3. Unzip the downloaded file and place it in "External_data" folder we created
Instructions to download the Moral Stories dataset :
1. The Moral Stories dataset is available at https://tinyurl.com/moral-stories-data
2. "Download" the compressed file from the link above 
3. Expand the downloaded file and place it in "External_data" folder we created
After downloading these, run the script as "python3 1_Use_external_data_sets_for_distant_supervision_DREAM.py"




## DREAM Model:
Our T5-11B model is available in HuggingFace PyTorch format at:
https://beaker.org/ds/01FMN19KY0SZQQHAG1JECDFVH4

For additional instructions about using these models and sample commands please refer to https://github.com/allenai/entailment_bank/blob/main/README_models.md


# Citation
```
@article{dreamnaacl2022,
  title={DREAM: Improving Situational QA by First Elaborating the Situation},
  author={Gu, Yuling and Dalvi Mishra, Bhavana, and Clark, Peter},
  journal={NAACL},
  year={2022}
}
```

