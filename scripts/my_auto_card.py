import sys

#TODO: consider organizing directory by set?
def file_name(s):
    s = s.replace("'","").replace(",","").replace(" ","")
    return "<$Depth$>./asset/cards/" + s.lower() + ".png"

def make_hover(name):
    img_file = file_name(name)
    return '<span class="hover_img"><a href="https://scryfall.com/search?q='+name+'">'+name+'<span> <img src="' + img_file + '" alt="image" height="300" /></span></a></span>'

def make_block(name):
    img_file = file_name(name)
    return '<div class="centered"><a class="#"><span><br> <img src="' + img_file + '" alt="image" height="300" /></span></a></div>'

def insert_autocard(text):
    while "[h[" in text:
        start = text.find("[h[")
        end = text.find("]]", start+1)
        text = text[:start] + make_hover(text[start+3:end]) + text[end+2:]
    while "[b[" in text:
        start = text.find("[b[")
        end = text.find("]]", start+1)
        text = text[:start] + make_block(text[start+3:end]) + text[end+2:]
    return text
