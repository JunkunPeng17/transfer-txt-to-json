# transfer-txt-to-json
a simple way to transfer the text to json file(including dividing a paragraph

## How to use?
Open the transfer_json.py file and notice the following line

```
path = r'C:\Users\YT-WS02\Desktop\new\txt'
files = os.listdir(path)
```  
Here is the path to set, select the path of the txt text you need to convert to json file
```
then we need to read the text into the list first
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
```  
after that, we need to transfer the text from list to dict, since the json format is similar to the dict.
```
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
```
in this step, I also added a decision condition to determine whether the text enters the 
next paragraph and needs to be split to divide the text data into segments of json.

Finally, we do the json transfermation,using `json.dumps()` 
```
clean_path = r'C:\Users\YT-WS02\Desktop\new\json'
    with open(os.path.join(clean_path, file), "w", encoding='utf-8') as k:
        jas = json.dumps(string, ensure_ascii=False)
        k.write(jas)
```
Hoping this method can help you do deal with transfermation from txt to json.
