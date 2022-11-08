import urllib.request
import time
import codecs

countries = ["BR","IN","ID","GB","DE","TH","MX","FR","JP","IT","CA","AU","TR","ES","VN","KR","TW","PH","MY","RU","ZA","AR","SE","NL","CL","PE","CO","PL","IL","GR","BE","CH","UA","SG","RO","DK","EG","NO","AT","HK","BD","PT","PK","IE","CN","EC","AE","SA","CZ","HU","FI","NG","PR","NZ","KH","MA","CR","BG","HR","IR","VE","GT","PY","LK","IQ","DO","MM","RS","BO","DZ","KZ","SK","KE","NP","LB","TN","LA","JO","CY","SV","LV","UY","AZ","HN","GE","BA","LT","BY","PA","KW","MK","SI","EE","GH","NI","QA","TZ","AL","SY","AO","CI","PS","XK","ZM","TT","LY","UG","CD","BN","LU","AM","JM","MN","MD","BH","AF","MZ","CM","OM","MO","RE","UZ","BW","SN","MT","IS","ME","SD","NA","ZW","MV","CU","ET","KP","MG","MW","FJ","HT","BS","MU","YE","PG","ML","KG","GP","BF","VA","BJ","SR","GY","SO","GN","MQ","GA","TG","CG","BB","BZ","NC","MP","CF","TD","NE","IM","AW","LS","JE","LR","CW","RW","PF","SS","KY","AD","SL","CV","GL","GF","BT","SZ","LC","FO","TJ","BM","AQ","GU","AG","MR","GM","MC","BI","GD","VI","SC","TM","SM","GW","GQ","GI","VC","VU","SB","LI","DJ","TC","KN","GG","DM","SX","ER","BQ","WS","EH","YT","TO","KM","TL","AS","ST","VG","MF","CK","AI","FK","SJ","PW","KI","FM","AN","NR","MH","GS","SH","MS","BL","WF","PM","TV","NU","CX","NF","PN","TF","CC","TK"]
#country = "US"

cities = []

# make a new file name with the current timestamp in the name
filename = "cities-"+str(time.time())+".txt"
# create the file
f = open(filename, "w+")

for country in countries:
    print("Starting "+country)
    page = 1
    while True:
        try:
            fp = urllib.request.urlopen("https://www.instagram.com/explore/locations/"+country+"/?page="+str(page))
        except urllib.error.HTTPError as e:
            print(str(page)+": "+str(e.code))
            break
        mybytes = fp.read()

        html = mybytes.decode("utf8")
        html = codecs.decode(html, 'unicode-escape')
        fp.close()

        # find all instances of this type of string: {"id":"c2438177","name":"Chicago","slug":"chicago-united-states"}
        for line in html.split('{"id":"'):
            if line.startswith('c'):
                id = line.split('","name":"')[0]
                name = line.split('","name":"')[1].split('","slug":"')[0]
                slug = line.split('","name":"')[1].split('","slug":"')[1].split('"}')[0]
                cities.append([id, name, slug])
                print(id, name, slug)
        
        # save the cities to the file
        for city in cities:
            f.write(city[0]+"\t"+city[1]+"\t"+city[2]+"\n")
        f.flush()

        time.sleep(3)
        page += 1
        #break
    time.sleep(3)