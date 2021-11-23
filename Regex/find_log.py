import re

def  FindLog(file):
    f = open(file)
    # Logfile = '''10.254.254.28 - - \[06/Aug/2007:00:07:21 -0700\] "GET .*jpg HTTP/1.0" 302 306 "-" "Mozilla/5.0 \(Macintosh; U; PPC Mac OS X Mach-O; en-US; rv:1.8.0.1; Google-TR-3\) Gecko/20060111 Firefox/1.5.0.1"'''
    tf=f.read()
    find_img = re.findall("GET (.*\.jpg).*/(.\..\..\..)",tf)
    result = []
    for i in find_img :
        e="http://"+i[1]+i[0]
        result.append(e)
    result1= set(result)
    for i in result1:
        print(i)

print("=========================================Place Code==============================================")
FindLog("place_code.txt")
print("=========================================Animal Code==============================================")
FindLog("animal_code.txt")