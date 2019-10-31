#!/usr/bin/python
# encoding: UTF-8
import os
import re
import json

path = r'C:\Users\YT-WS02\Desktop\new\total'
files = os.listdir(path)
for file in files:

    f = open(os.path.join(path, file), 'r', encoding='utf-8')
    f = f.read()
    text = []
    sentence = ''
    for word in f:

        if word == '\n':
            sentence += word
            text.append(sentence)
            sentence = ''
        else:
            sentence += word

    s = []
    index = 0
    result = {}
    while index < len(text):
        if text[index].strip() == '':
            text[index] = text[index]
        elif text[index].strip() != '':
            text[index] = text[index].strip("\n")
        s.append(text[index])
        index += 1
    f2 = ''.join(s)
    string = f2.split("\n")

    clean_path = r'C:\Users\YT-WS02\Desktop\new\medical txt clean_json'
    with open(os.path.join(clean_path, file), "w", encoding='utf-8') as k:
        jas = json.dumps(string, ensure_ascii=False)
        k.write(jas)
