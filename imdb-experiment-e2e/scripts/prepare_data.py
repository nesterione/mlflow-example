from glob import glob 
import os
import sys
import pandas as pd 

input_folder = '../data/raw'
output_folder = '../data/prep'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

def read_files(src, label):
    data = []
    for file in glob(src):
        name = os.path.basename(file).replace('.txt','')
        score = int(name.split('_')[1])
        with open(file, 'r', encoding='utf-8') as f:
            review = f.read()
            data.append((review, score, label))
    return data

# Prepare train
train_neg = os.path.join(input_folder,'train/neg/*.txt')
train_pos = os.path.join(input_folder,'train/pos/*.txt')
train_data = read_files(train_neg, 'neg') + read_files(train_pos, 'pos')

df = pd.DataFrame(train_data)
df.columns = ['Review', 'Score', 'Expected']
df.index.name = 'Id'
df.to_csv(os.path.join(output_folder,'train.csv'), index=True)

# Prepare test
test_neg = os.path.join(input_folder,'test/neg/*.txt')
test_pos = os.path.join(input_folder,'test/pos/*.txt')
test_data = read_files(test_neg, 'neg') + read_files(test_pos, 'pos')
df = pd.DataFrame(test_data)
df.columns = ['Review', 'Score', 'Expected']
df.index.name = 'Id'
test_df = df.drop(columns = ['Score', 'Expected'])
test_df.to_csv(os.path.join(output_folder, 'test.csv'), index=True)