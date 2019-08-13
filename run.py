import os
import sys
import time
import argparse as ap

Dataset = './datasets/'
Datas = ['intro','answer']

def main():
    dirlist = list()
    dirnames = os.listdir(Dataset)
    for dirname in dirnames:
        dirlist.append(dirname)
    parser = ap.ArgumentParser()
    parser.add_argument('Story',
                        type=int,
                        help = 'Choose your story. ex) 0')
    parser.add_argument('Count',
                        type=int,
                        help = 'How many recursive you want')
    
    args = parser.parse_args()
    story = args.Story
    count = args.Count

    filepath = [
        Dataset + dirnames[story] + '/' + Datas[0],
        Dataset + dirnames[story] + '/' + Datas[1]
    ]
    
    with open(filepath[0], 'r') as intro_fd:
        Datas[0] = intro_fd.read()
    with open(filepath[1], 'r') as answer_fd:
        Datas[1] = answer_fd.read()
    
    # The beginning of the legend.
    for character in Datas[0]:
        print(character, end='', flush=True)
        time.sleep(0.1)
    what_is_recursive_function(count)

def what_is_recursive_function(remained):
    for character in Datas[1]:
        print(character, end='', flush=True)
        time.sleep(0.1)
    remained -= 1
    if remained > 0:
        what_is_recursive_function(remained)
    else:
        print('...')

if __name__ == "__main__":
    main()

