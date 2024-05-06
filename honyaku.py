import requests

xgengo="en"
ygengo="ja"

def honyaku(x):
    global xgengo,ygengo
    x=x.replace("&","%26")
    return requests.get(f"https://script.google.com/macros/s/AKfycbyjfnVscjQi8V1uuqh_TW8V_R-sPH7exk28r4xYXMEKSLUHGVmbPPF0BG00bYT2bBknEg/exec?text={x.replace('&','%26')}&source={xgengo}&target={ygengo}").text
print(honyaku("hello!"))
