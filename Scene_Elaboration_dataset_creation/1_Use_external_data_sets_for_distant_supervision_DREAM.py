#!/usr/bin/env python
# coding: utf-8

# In[6]:


import json
import csv
import os
import random


# In[7]:


def make_sure_dir_exists(dir_to_check):
    if not os.path.exists(dir_to_check):
        os.makedirs(dir_to_check)


# In[ ]:


# !rm -r External_data/
# !rm -r External_data_tidied/
# !rm -r External_data_tidied_combined_used_to_train_DREAM/


# In[3]:


# We will store the orginal external datasets in a folder named "External_data"
get_ipython().system('mkdir External_data')

# We will store the extracted information from external datasets that we use 
# to build our Scene Elaboration (SE) dataset in a folder named "External_data_tidied"
get_ipython().system('mkdir External_data_tidied')


# ## External dataset: Social Chemistry
# To get rule of thumbs (ROT component of SE) in External_data_tidied/
# 

# Download the source dataset :
# 1. Visit the website for the Social Chemistry project https://maxwellforbes.com/social-chemistry/ 
# 2. Scroll down to the "QUICK INFO" part, find the third column "DATA", "Social-Chem-101 Dataset 4.5M+ annotations 28 MB .zip" to "DOWNLOAD" the source data
# 3. Unzip the downloaded file and place it in "External_data" folder we created
# 
# 

# In[19]:


def organize_data_sc_as_rot():
    dataset = "social_chemistry"
    out_dir = "External_data_tidied"
    scene_part = "rot" # what might other people say
    out_paths = []
    for train_dev_test in ["training", "dev", "test"]:
        out_path = "/".join([out_dir, scene_part , train_dev_test]) + ".json"
        out_paths.append(out_path)
        make_sure_dir_exists("/".join([out_dir, scene_part]))
    
    infile = "External_data/social-chem-101/social-chem-101.v1.0.tsv"

    judgment_types = []
    with open(infile, "r") as datafile,         open(out_paths[0], "w") as json_train, open(out_paths[1], "w") as json_dev,         open(out_paths[2], "w") as json_test :

        data = csv.reader(datafile, delimiter = "\t")
        data_split_idx = -1
        situation_idx = -1
        rot_idx = -1
        short_judgement_idx = -1
        
        id_cnt = 1
        train_cnt = 0
        dev_cnt = 0
        test_cnt = 0
        for i, annotation in enumerate(data):
            if i == 0:
                data_split_idx = annotation.index("split")
                situation_idx = annotation.index("situation")
                rot_idx = annotation.index("rot")
                short_judgement_idx = annotation.index("rot-judgment")

            else:  
                target_out = ""
                data_split = annotation[data_split_idx]
                situation = annotation[situation_idx]
                rot = annotation[rot_idx]
                short_judgement = annotation[short_judgement_idx].lower()
                
                if short_judgement not in judgment_types:
                    judgment_types.append(short_judgement)
                train_dev_test = data_split
                if data_split == "train":
                    json_file = json_train
                    train_dev_test = "training"
                    train_cnt += 1
                elif data_split == "dev":
                    json_file = json_dev
                    dev_cnt +=1
                else:
                    json_file = json_test
                    test_cnt +=1
                
                if not situation.endswith("."):
                    situation += "."
                    
                if rot != "" and not rot.endswith("."):
                        rot += "."
                json_file.write(json.dumps({"dataset": dataset , "id":  dataset  + "_" + train_dev_test + "_" + str(id_cnt),                 "question": "[SITUATION] " + situation + " [QUERY] " + scene_part,                 "answer": rot}))
                json_file.write("\n")
                json_file.flush()
                id_cnt += 1

        print("=" * 10, scene_part, "=" * 10)
        print("Total :", id_cnt - 1)
        print("train :", train_cnt)
        print("dev :", dev_cnt)
        print("test :", test_cnt)
        #print("judgement_types:", judgment_types)


# In[20]:


'''
You'd expect the following output from running the next line:
========== rot ==========
Total : 355922
train : 233501
dev : 29234
test : 93187
'''

organize_data_sc_as_rot()


# ## External dataset: Story Commonsense
# To get Motivation, Emotion in External_data_tidied/
# 
# 

# Download the source dataset :
# 1. Visit the website for the Story Commonsense project https://uwnlp.github.io/storycommonsense/
# 2. At the top of the page, where the "Quick links" are, click "[download the data]"
# 3. Unzip the downloaded file and place it in "External_data" folder we created
# 
# 

# In[11]:


def organize_data_story_commonsense(train_dev_test, scene_part):
    '''
    Input strings:
    train_dev_test : "training"/ "dev"/ "test"
    scene_part : "emotion", "motivation"
    '''
    dataset = "story_commonsense"
    out_dir = "External_data_tidied"
    out_path = "/".join([out_dir, scene_part,train_dev_test]) + ".json"
    make_sure_dir_exists("/".join([out_dir, scene_part]))
    
    if train_dev_test == "training":
        infile = "External_data/storycommonsense_data/csv_version/" + train_dev_test + "/allcharlinepairs.csv"
    else:
        if scene_part == "emotion":
            infile = "External_data/storycommonsense_data/csv_version/" + train_dev_test + "/" + scene_part + "/allcharlinepairs.csv"
        elif scene_part == "motivation":
            infile = "External_data/storycommonsense_data/csv_version/" + train_dev_test + "/motiv/allcharlinepairs.csv"


    with open(infile, "r") as datafile,         open(out_path, "w") as json_file:

        data = csv.reader(datafile)
        sentence_idx = -1
        character_idx = -1
        target_idx = -1
        id_cnt = 1 
        for i, annotation in enumerate(data):
            if i == 0:
                sentence_idx = annotation.index("sentence")
                character_idx = annotation.index("char")
                target_idx = annotation.index(scene_part)

            else:  
                situation = annotation[sentence_idx].strip()
                
                if annotation[target_idx] == "[\"none\"]":
                    target_out = ""
                else:
                    processed_annotation = json.loads(annotation[target_idx])
                    processed_annotation = ", ".join([x.lower() for x in processed_annotation])
                    target_out = get_possessive_form(annotation[character_idx]).capitalize() + " " + scene_part + " is " + processed_annotation
                    if target_out != "" and not target_out.endswith("."):
                        target_out += "."

                #print(situation, target_out) 
                if not situation.endswith("."):
                    situation += "."

                json_file.write(json.dumps({"dataset": dataset , "id":  dataset  + "_" + train_dev_test + "_" + str(id_cnt),                                 "question": "[SITUATION] " + situation + " [QUERY] " + scene_part,                                 "answer": target_out}))
                json_file.write("\n")
                json_file.flush()
                id_cnt += 1

        print("=" * 10, train_dev_test, "|", scene_part, "=" * 10)
        print("Total :", id_cnt - 1)


# In[12]:


'''
You'd expect the following output from running the next few lines:
========== training | emotion ==========
Total : 174691
========== training | motivation ==========
Total : 174691
========== dev | emotion ==========
Total : 53234
========== dev | motivation ==========
Total : 47547
========== test | emotion ==========
Total : 51891
========== test | motivation ==========
Total : 39359
'''
for train_dev_test in ["training", "dev", "test"]:
    for scene_part in ["emotion", "motivation"]:
        organize_data_story_commonsense(train_dev_test, scene_part)


# ## External dataset: Moral Stories
# To get moral, immoral_consequences in External_data_tidied/

# Download the source dataset :
# 1. The Moral Stories dataset is available at https://tinyurl.com/moral-stories-data
# 2. "Download" the compressed file from the link above 
# 3. Expand the downloaded file and place it in "External_data" folder we created
# 

# In[15]:


def organize_data_moral_stories(scene_part, train_dev_test):
    '''
    Input strings:
    train_dev_test : "training"/ "dev"/ "test"
    scene_part : "consequence"
    '''
    dataset = "moral_stories"
    
    out_dir = "External_data_tidied"
    out_path = "/".join([out_dir, scene_part , train_dev_test]) + ".json"
    make_sure_dir_exists("/".join([out_dir, scene_part]))
    
    if train_dev_test == "training":
        infile = "External_data/" + dataset + "_datasets/generation/consequence|action+context/norm_distance/train.jsonl"
    else:
        infile = "External_data/" + dataset + "_datasets/generation/consequence|action+context/norm_distance/" + train_dev_test + ".jsonl"

    with open(infile, "r") as datafile, open(out_path, "w") as json_file :

        data = datafile.readlines()
        

        id_cnt = 1
        for i, data_line in enumerate(data):
            annotation = json.loads(data_line)
            situation = annotation["situation"]
            tag = ""
            
            if "moral_action" in annotation:
                action = annotation["moral_action"]
                consequence = annotation["moral_consequence"]
                tag = "[moral_consequence]"

            elif "immoral_action" in annotation:
                action = annotation["immoral_action"]
                consequence = annotation["immoral_consequence"]
                tag = "[immoral_consequence]"

            json_file.write(json.dumps({"dataset": dataset , "id":  dataset  + "_" + train_dev_test + "_" + str(id_cnt),             "question": "[SITUATION] " + situation + " " + action + " [QUERY] " + scene_part,             "answer": tag + " " + consequence}))
            
            json_file.write("\n")
            json_file.flush()
            id_cnt += 1
            

        print("=" * 10, train_dev_test, "|", scene_part, "=" * 10)
        print("Total :", id_cnt - 1)


# In[16]:


'''
You'd expect the following output from running the next few lines:
========== training | consequence ==========
Total : 20000
========== dev | consequence ==========
Total : 2000
========== test | consequence ==========
Total : 2000
'''
for train_dev_test in ["training", "dev", "test"]:
    for scene_part in ["consequence"]:
        organize_data_moral_stories(scene_part, train_dev_test)


# ## Combine data
# 
# Downsample to make the training size from each source data is more blanaced.
# 
# Combine the sampled scene components into one folder (with training/dev/test files).

# In[21]:


outdir = "External_data_tidied_combined_used_to_train_DREAM/"
make_sure_dir_exists(outdir)

file_names = ["training.json", "dev.json", "test.json"]
global_final_new_data = 0 

for file_name in file_names:
    print(file_name)
    with open(outdir + file_name, "w") as outfile:
        for folder in os.listdir("External_data_tidied/"):

            if os.path.isfile("External_data_tidied/" + folder):
                continue # we want to copy from data folders, skip README file etc
            print("=" * 10, "Copying data from", folder, "subfolder...", "=" * 10)
            with open("External_data_tidied/" + folder + "/" + file_name , 'r') as infile:
                
                # read all lines from file
                infile_lines = infile.readlines()
                total_num_of_lines = len(infile_lines)
                print("Original total size", total_num_of_lines)
                
                if folder in ["motivation", "emotion"]:
                    ###
                    # For motivation (M) and emotion (E) components, sample 10% ~175k -> ~17.5K
                    # too much blanks, sample to control that 90% is not blank
                    ###
                    non_empty_line_ids = [i for i, line in enumerate(infile_lines) if json.loads(line)["answer"] != ""]
                    empty_line_ids = [i for i, line in enumerate(infile_lines) if json.loads(line)["answer"] == ""]
                    assert len(set(non_empty_line_ids) & set(empty_line_ids)) == 0
                    assert len(non_empty_line_ids) + len(empty_line_ids) == total_num_of_lines
                    
                    random.seed(12345)
                    sampled_line_nums_non_empty = random.sample(non_empty_line_ids, int((total_num_of_lines * 0.9) // 10))
                    print("non-empty sampled", len(sampled_line_nums_non_empty))
                    random.seed(12345)
                    sampled_line_nums_empty = random.sample(empty_line_ids, int((total_num_of_lines * 0.1) // 10))
                    print("empty sampled", len(sampled_line_nums_empty))
                    
                    sampled_line_nums = sampled_line_nums_non_empty + sampled_line_nums_empty
                    print("total sampled", len(sampled_line_nums))
                    
                    if len(sampled_line_nums) - (total_num_of_lines // 10) > 10:
                        print(len(sampled_line_nums), total_num_of_lines)
                else:
                    ###
                    # For rule of thumb a.k.a social norm (ROT) component, sample 10% ~233k -> ~23K
                    ###
                    random.seed(12345)
                    sampled_line_nums = random.sample(list(range(total_num_of_lines)), total_num_of_lines // 10)
                
                written_to_file_cnt = 0
                for i, line in enumerate(infile_lines):
                    if folder.endswith("consequence"):
                        ###
                        # For Consequence (Con) component, this dataset is smaller, so no need to sample
                        ###
                        written_to_file_cnt += 1
                        outfile.write(line)
                    else:
                        if i in sampled_line_nums:
                            written_to_file_cnt += 1
                            outfile.write(line)
                            
                if folder.endswith("consequence"):      
                    # this dataset is small, copy everything
                    assert written_to_file_cnt == total_num_of_lines
                else:
                    assert written_to_file_cnt == len(sampled_line_nums)
                    
            global_final_new_data += written_to_file_cnt
            print("External_data_tidied/" + folder + "/" + file_name, "copied!", "Copied", written_to_file_cnt, "lines.")
            
            


print("THIS DATASET HAS A TOTAL OF", global_final_new_data, "LINES!")


# In[ ]:


'''
You'd expect the following output from running the above lines:
training.json
========== Copying data from rot subfolder... ==========
Original total size 233501
External_data_tidied/rot/training.json copied! Copied 23350 lines.
========== Copying data from consequence subfolder... ==========
Original total size 20000
External_data_tidied/consequence/training.json copied! Copied 20000 lines.
========== Copying data from emotion subfolder... ==========
Original total size 174691
non-empty sampled 15722
empty sampled 1746
total sampled 17468
External_data_tidied/emotion/training.json copied! Copied 17468 lines.
========== Copying data from motivation subfolder... ==========
Original total size 174691
non-empty sampled 15722
empty sampled 1746
total sampled 17468
External_data_tidied/motivation/training.json copied! Copied 17468 lines.
dev.json
========== Copying data from rot subfolder... ==========
Original total size 29234
External_data_tidied/rot/dev.json copied! Copied 2923 lines.
========== Copying data from consequence subfolder... ==========
Original total size 2000
External_data_tidied/consequence/dev.json copied! Copied 2000 lines.
========== Copying data from emotion subfolder... ==========
Original total size 53234
non-empty sampled 4791
empty sampled 532
total sampled 5323
External_data_tidied/emotion/dev.json copied! Copied 5323 lines.
========== Copying data from motivation subfolder... ==========
Original total size 47547
non-empty sampled 4279
empty sampled 475
total sampled 4754
External_data_tidied/motivation/dev.json copied! Copied 4754 lines.
test.json
========== Copying data from rot subfolder... ==========
Original total size 93187
External_data_tidied/rot/test.json copied! Copied 9318 lines.
========== Copying data from consequence subfolder... ==========
Original total size 2000
External_data_tidied/consequence/test.json copied! Copied 2000 lines.
========== Copying data from emotion subfolder... ==========
Original total size 51891
non-empty sampled 4670
empty sampled 518
total sampled 5188
External_data_tidied/emotion/test.json copied! Copied 5188 lines.
========== Copying data from motivation subfolder... ==========
Original total size 39359
non-empty sampled 3542
empty sampled 393
total sampled 3935
External_data_tidied/motivation/test.json copied! Copied 3935 lines.
THIS DATASET HAS A TOTAL OF 113727 LINES!

'''


# ## What's next?
# 
# ### We now use this external data to create our scene generation model DREAM!

# In[ ]:




