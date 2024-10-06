

W = '\x1b[1;37m'
G = '\x1b[1;32m'
R = '\x1b[1;91m'
S = '\x1b[1;36m'
B = '\x1b[1;34m'
Y = '\x1b[1;33m'
P = '\x1b[1;35m'
cnt=0
cp=0
ok=0
ok1=0
loop=0
died=0
live=0
import os,sys,time,re,uuid,base64,zlib,subprocess
from concurrent.futures import  ThreadPoolExecutor as tpe
try:
    import pycurl
    from io import BytesIO
except:
    os.system('pip install pycurl')
    import pycurl
    from io import BytesIO
try:import pycurl
except:os.system('pkg uninstall python;pkg install python -y;pip install pycurl')
try:import pycurl
except:print('\n Pycurl Module Error!\n Contact With Owner! ');exit()
import random
def random_ua():
    model = "iPhone"+str(random.randint(4,16))+','+str(random.randint(1,9))
    abc = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','X','Y','Z']
    build = str(random.randint(9,19))+random.choice(abc)+str(random.randint(50,199))
    fbsv = str(random.randint(4,16))+'_'+str(random.randint(1,9))+'_'+str(random.randint(1,9))
    ua1 = '[FBAN/FB4A;FBAV/323.0.0.46.119;FBBV/298672707;FBDM/{density=2.75,width=1080,height=2168};FBLC/ru_RU;FBRV/299927973;FBCR/MTS RUS;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/Redmi Note 9 Pro;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]'
    ua2 = "[FBAN/FB4A;FBAV/323.0.0.46.119;FBBV/298672707;FBDM/{density=2.75,width=1080,height=2168};FBLC/ru_RU;FBRV/299927973;FBCR/MTS RUS;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/Redmi Note 9 Pro;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]"
    dv_typ = random.choice(['SM-S911B','SM-S908B','SM-G998B','SM-G988B','SM-G973B','SM-N986B'])
    ua3 = f"[FBAN/FB4A;FBAV/323.0.0.46.119;FBBV/298672707;FBDM/{density=2.75,width=1080,height=2168};FBLC/ru_RU;FBRV/299927973;FBCR/MTS RUS;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/Redmi Note 9 Pro;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]"
    a = random.randrange(112,115)
    b = random.randrange(1000,10000)
    c = random.randrange(10,100)
    os_ver = random.randrange(10,13)
    dv_typ = random.choice(['RMX3686','RMX3393','RMX3081','RMX2170','RMX2061','RMX2020'])
    bl_typ = random.choice(['QP1A','SKQ1','TP1A','RKQ1','SP1A','RP1A'])
    dv_ver = random.randrange(100000,250000)
    sd_ver = random.randrange(1,10)
    ch_ver = f'{a}.0.{b}.{c}'
    ua4 = f'[FBAN/FB4A;FBAV/323.0.0.46.119;FBBV/298672707;FBDM/{density=2.75,width=1080,height=2168};FBLC/ru_RU;FBRV/299927973;FBCR/MTS RUS;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/Redmi Note 9 Pro;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]'
    a = random.randrange(112,115)
    b = random.randrange(1000,10000)
    c = random.randrange(10,100)
    os_ver = random.randrange(10,13)
    dv_typ = random.choice(['SM-S911B','SM-S908B','SM-G998B','SM-G988B','SM-G973B','SM-N986B'])
    bl_typ = random.choice(['PPR1','LRX21T','TP1A','RKQ1','SP1A','RP1A'])
    dv_ver = random.randrange(100000,250000)
    sd_ver = random.randrange(1,10)
    ch_ver = f'{a}.0.{b}.{c}'
    ua5 = f'[FBAN/FB4A;FBAV/323.0.0.46.119;FBBV/298672707;FBDM/{density=2.75,width=1080,height=2168};FBLC/ru_RU;FBRV/299927973;FBCR/MTS RUS;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/Redmi Note 9 Pro;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]'
    a = random.randrange(112,115)
    b = random.randrange(1000,10000)
    c = random.randrange(10,100)
    os_ver = random.randrange(10,13)
    dv_typ = random.choice(['vivo 1951','vivo 1918','V2011A','V2047','V2145','V2227A','V2160'])
    bl_typ = random.choice(['RP1A','PKQ1','QP1A','TP1A'])
    dv_ver = random.randrange(100000,250000)
    sd_ver = random.randrange(1,10)
    ch_ver = f'{a}.0.{b}.{c}'
    ua6 = f'[FBAN/FB4A;FBAV/323.0.0.46.119;FBBV/298672707;FBDM/{density=2.75,width=1080,height=2168};FBLC/ru_RU;FBRV/299927973;FBCR/MTS RUS;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/Redmi Note 9 Pro;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]'
    ua = random.choice([ua1,ua2,ua3,ua4,ua5,ua6])
    return(ua)
myid=uuid.uuid4().hex[:5].upper()
try:
    key1 = open('/data/data/com.termux/files/usr/bin/.mrTahiroxxx-cov', 'r').read()
except:
    kok=open('/data/data/com.termux/files/usr/bin/.mrTahiroxxx-cov', 'w');kok.write(myid);kok.close()
uid = os.getuid()
key1 = open('/data/data/com.termux/files/usr/bin/.mrTahiroxxx-cov', 'r').read()
kex=(f"Tahiro-XD~CREATE:{uid}TS{key1}110E==")
key2 = base64.b64encode(str(f"{kex}").encode('utf-8'))
key=(f"{key2}")
fkeyx = key.replace("b'","").replace("'","")
def linex():
    print('\033[1;37m------------------------------------------')
def clear():
    import os
    os.system("clear")
   print("""\033[1;37m   
▗▖ ▗▖▗▖   ▗▖  ▗▄▖  ▗▄▄▖   ▗▄▖ 
▐▌. ▞. ▐▌   ▐▌▐▌ ▐▌▐▌       ▐▌ ▐▌
▐▛▚▖ ▐▛▀▜▌▐▌ ▐▌ ▝▀▚▖▐▛ ▜▌
▐▌ ▐▌▐▌   ▐▌ ▚▄▞▘▗▄▄▞ ▐▌ ▐▌
------------------------------------------
 Author : Tahiroo
 Github : Unknown
 Tools  : Auto Facebook Register
 Contact: +923227508149
 Version: 1.0
\033[1;37m------------------------------------------""") 
try:
    clear()
    print(' Checking For Updates....')
    linex()
    lik=str(zlib.decompress(b'x\x9c\xcb())(\xb6\xd2\xd7O\xaeL*\xca\xac\xc8M\xd5K\xca\xc9O/.\xc8/\xd1K\xce\xcf\xd57202\xd17\xb0\xd4O,((\xca/K\xcc\xd1\xcb(\xc9\xcd\x01\x00\xe1\xc7\x12:')).replace("b'","").replace("'","")
    buffer = BytesIO()
    c = pycurl.Curl()
    c.setopt(c.URL, lik)
    c.setopt(c.WRITEDATA, buffer)
    c.perform()
    c.close()
    body = buffer.getvalue().decode('utf-8')
    response = body
    if "Version-1.5" in response:
        print(" Already Up To Date...")
        linex()
        print(' Checking For Approval....')
        linex()
        if kex in response:
            print('\033[1;32m Your Key is Approved....\033[1;37m');time.sleep(2)
        elif "Trail-30min" in response:
            print('\033[1;36m Enjoy Free Trial ....\033[1;37m');time.sleep(2)
        else:
            print("\033[1;31m Read note first! ")
            linex()
            print(" You cannot run this tool without Tahiro permeations \n Note: Agar Tool mai Koi Masla Aata HA To Me Jald Se Jald Try Kronga Fix Krne Ke Agr Nhi Hota To May Be kujh time lag jya fix krne me!\n payment krne ka bad return nhi hoge agr buy krna ha to ok else skip,exit")
            linex()
            print(" Your key: "+fkeyx);subprocess.check_output(["am", "start", "https://api.whatsapp.com/send?phone=+923203714588&text="+(" Hi Tahiro sir i want Buy Auto Create Ids Tool Please Approve My Token\n Token:- "+ fkeyx)]);time.sleep(2)
            exit('\n Run:  python createfb.py')
            sys.exit()
    else:
        print(' Update done successfully wait for setup! ')
        time.sleep(2)
        Create()
        exit()
except Exception as e:exit('\n Network connection error '+e)
def cvt(st,ran):
    try:
        if st == 'ok': cookie = ('c_user=%s;xs=%s;fr=%s;datr=%s;'%(ran['c_user'],ran['xs'],ran['fr'],ran['datr']))
        elif st == 'cp': cookie = ('checkpoint=%s;datr=%s;fr=%s;'%(ran['checkpoint'],ran['datr'],ran['fr']))
    except Exception as e : cookie = '; '.join([str(x)+"="+str(y) for x,y in ran])
    return(str(cookie))
    
def a(k):return k
import os,time,_md5,marshal,inspect 
if str(os.system)==str(print):
  exit()
  sys.exit()
  os._exit(0)
def random_ua():
    model = "iPhone"+str(random.randint(4,16))+','+str(random.randint(1,9))
    abc = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','X','Y','Z']
    build = str(random.randint(9,19))+random.choice(abc)+str(random.randint(50,199))
    fbsv = str(random.randint(4,16))+'_'+str(random.randint(1,9))+'_'+str(random.randint(1,9))
    ua1 = '[FBAN/FB4A;FBAV/323.0.0.46.119;FBBV/298672707;FBDM/{density=2.75,width=1080,height=2168};FBLC/ru_RU;FBRV/299927973;FBCR/MTS RUS;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/Redmi Note 9 Pro;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]'
    ua2 = "[FBAN/FB4A;FBAV/323.0.0.46.119;FBBV/298672707;FBDM/{density=2.75,width=1080,height=2168};FBLC/ru_RU;FBRV/299927973;FBCR/MTS RUS;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/Redmi Note 9 Pro;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]"
    dv_typ = random.choice(['SM-S911B','SM-S908B','SM-G998B','SM-G988B','SM-G973B','SM-N986B'])
    ua3 = f"[FBAN/FB4A;FBAV/323.0.0.46.119;FBBV/298672707;FBDM/{density=2.75,width=1080,height=2168};FBLC/ru_RU;FBRV/299927973;FBCR/MTS RUS;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/Redmi Note 9 Pro;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]"
    a = random.randrange(112,115)
    b = random.randrange(1000,10000)
    c = random.randrange(10,100)
    os_ver = random.randrange(10,13)
    dv_typ = random.choice(['RMX3686','RMX3393','RMX3081','RMX2170','RMX2061','RMX2020'])
    bl_typ = random.choice(['QP1A','SKQ1','TP1A','RKQ1','SP1A','RP1A'])
    dv_ver = random.randrange(100000,250000)
    sd_ver = random.randrange(1,10)
    ch_ver = f'{a}.0.{b}.{c}'
    ua4 = f'[FBAN/FB4A;FBAV/323.0.0.46.119;FBBV/298672707;FBDM/{density=2.75,width=1080,height=2168};FBLC/ru_RU;FBRV/299927973;FBCR/MTS RUS;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/Redmi Note 9 Pro;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]'
    a = random.randrange(112,115)
    b = random.randrange(1000,10000)
    c = random.randrange(10,100)
    os_ver = random.randrange(10,13)
    dv_typ = random.choice(['SM-S911B','SM-S908B','SM-G998B','SM-G988B','SM-G973B','SM-N986B'])
    bl_typ = random.choice(['PPR1','LRX21T','TP1A','RKQ1','SP1A','RP1A'])
    dv_ver = random.randrange(100000,250000)
    sd_ver = random.randrange(1,10)
    ch_ver = f'{a}.0.{b}.{c}'
    ua5 = f'[FBAN/FB4A;FBAV/323.0.0.46.119;FBBV/298672707;FBDM/{density=2.75,width=1080,height=2168};FBLC/ru_RU;FBRV/299927973;FBCR/MTS RUS;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/Redmi Note 9 Pro;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]'
    a = random.randrange(112,115)
    b = random.randrange(1000,10000)
    c = random.randrange(10,100)
    os_ver = random.randrange(10,13)
    dv_typ = random.choice(['vivo 1951','vivo 1918','V2011A','V2047','V2145','V2227A','V2160'])
    bl_typ = random.choice(['RP1A','PKQ1','QP1A','TP1A'])
    dv_ver = random.randrange(100000,250000)
    sd_ver = random.randrange(1,10)
    ch_ver = f'{a}.0.{b}.{c}'
    ua6 = f'[FBAN/FB4A;FBAV/323.0.0.46.119;FBBV/298672707;FBDM/{density=2.75,width=1080,height=2168};FBLC/ru_RU;FBRV/299927973;FBCR/MTS RUS;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/Redmi Note 9 Pro;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]'
    ua = random.choice([ua1,ua2,ua3,ua4,ua5,ua6])
    return(ua)
def Create():
    clear()
    import requests as r,re,random,os
    from bs4 import BeautifulSoup
    print()
    def rnd(a,b):
      return str(random.randint(a,b))
    
    def find(txtt,wrd):
       xx = re.findall('name="'+wrd+'" value="(.*?)"',txtt.replace("amp;",""))[0]
       return xx
    m=['Aijaz|Ali', 'Zulfiqar|Ali', 'Kamran|Wassan', 'Shoaib|Shoaib', 'Muhbbat|Wassan', 'Rana|Waseem', 'Paras|Paras', 'Rana|Mohsin', 'Aliali|Aliali', 'Ali|Ali', 'Ghulam|Ghulam', 'Waqar|Lakho', 'Junaid|Chandia', 'Asif|Jan', 'Ali|Gulam', 'Malik|Saab', 'Rana|Zakir', 'Zameer|Ali', 'Irshad|Jan', 'Gulam|Shabir', 'Tariq|Rajput', 'Sajid|Ali', 'Shamshad|Ali', 'Mola|Bux', 'Awais|Rao', 'Shahbaz|Ali', 'Rana|Sahil', 'Khadam|Faqir', 'Mukhtiar|Magsi', 'Ghulam|Ali', 'Shah|Mohammed', 'Rawal|Ali', 'ستار|دادا', 'Abdul|Majeed', 'Mer|Muhammad', 'Ali|Rajput', 'Rana|Farman', 'Ahtisham|Rajput', 'Alideno|Khoso', 'Own|Rana', 'Suhail|Ahmed', 'Gulzar|Ahmed', 'Ahamd|Jam', 'Tasawar|Rajput', 'Fida|Qureshi', 'Shamshad|Rahu', 'سوشل|ميڍيا', 'Sheeraz|Abbasi', 'Bashir|Ustad', 'Zubair|Rao', 'Zafar|Ali', 'Yaqoob|Ali', 'M|Soomar', 'Altaf|Hussain', 'Bahadur|Ali', 'Farman|Ali', 'Waris|Ali', 'Rana|Qurban', 'Muhammad|Khan', 'Asad|Asad', 'Sartaaj|Sartaaj', 'Rana|Kabir', 'Rana|Abdul', 'Ghulam|Hussain', 'Kirshan|Kumar', 'Adil|Rajpoot', 'Sahoowal|Sahoowal', 'عبد|الجبار', 'Imran|Ali', 'Faz|Mahammad', 'Safeel|Nawaz', 'ريا|ض', 'Haroon|Rana', 'Amjad|Ali', 'Kashii|Rajpoot', 'Junejo|Sahib', 'Altaf|Pahore', 'Ali|Rajput', 'Zeeshan|Ali', 'Muhammad|Muktiar', 'Iftikhar|Ahmand', 'Shahzeb|Ali', 'Faiz|Jutt', 'Chanesar|Khan', 'Ali|Shar', 'Zuhair|Ahmed', 'محب|علی', 'Siraj|Khaskheli', 'Rana|Dilshad', 'Ghazanfar|Ali', 'Rao|Awais', 'Jaan|Jaan', 'Syed|Junaid', 'Abdul|Ghaffar', 'Kirshan|Kumar', 'ابومحمد|احمد', 'Nisar|Hussain', 'Nasir|Dahri', 'Hakim|Khan', 'Ahsan|Raza', 'Nadir|Rind', 'Sålmàñ|Çh', 'GhulamNabi|Khaskhali', 'Umar|Lal', 'NabeelHy|Ka', 'Dilshad|Magsi', 'Haaji|Anwar', 'Nisar|Ahmed', 'Barkat|Ali', 'Irfan|Ali', 'Aslam|Khan', 'Hashim|Khoso', 'Abdul|Malik', 'Masroor|Zardari', 'Rao|Bilal', 'Nisarkhoso|Nisarkhoso', 'مرجع|الناطق', 'Sajawal|Rajput', 'Rana|Muhammad', 'Rana|Dilshad', 'Rana|Imran', 'Daniyal|Kazmi', 'Faqeer|Baboo', 'Azan|Jan', 'Gul|Hassan', 'Nadir|Jan', 'NadeemRind|Rind', 'Angel|Rodriguez', 'Allahbux|Rang', 'Ghullam|Muhammad', 'Talib|Hussain', 'Abid|Ali', 'Rana|Noushad', 'Ghulam|Hussain', 'Samir|Samir', 'Shahid|Rana', 'Janib|Janib', 'Maria|Albuquerque', 'Rana|Qasim', 'Faizan|Ali', 'Ali|Gul', 'Madeji|Power', 'Rajput|Faisal', 'Mansoor|Sahito', 'Ali|Dero', 'Razaq|Khaskheli', 'Muneer|Ali', 'Imran|Ali', 'Sakhawat|Ali', 'Khadim|Baloch', 'Rana|Taswar', 'Raouf|Chadhar', 'Umar|Shahzad', 'Shah|Mir', 'Irfsn|Irfsn', 'Abbas|King', 'Aftab|Ali', 'M|Raju', 'Ghulam|Mustafa', 'Gul|Sher', 'Nazim|Hussain', 'Malik|Jawed', 'Deedar|Hussain', 'Maham|Khan', 'Junaid|Rajput', 'Sawan|Ali', 'Sajwal|Rao', 'Ayaz|Ali', 'Irfan|Irfan', 'Hut|Khan', 'Ana|Mendez', 'Shakeel|Khosa', 'Javed|Javed', 'Dil|E', 'Rana|Adil', 'Rahil|Ali', 'Innayat|Ali', 'Aijaz|Abbasi', 'Jamil|Jan', 'Fidah|Khoso', 'Rana|Abdul', 'Rana|Junaid', 'Malik|Sajid', 'Ghulam|Ali', 'Ahsan|Ali', 'Imtiaz|Ali', 'Islam|Baloch', 'Hashim|Khoso', 'Sattar|Buledi', 'Nanik|Ram', 'Gul|Wali', 'Rahman|Khan', 'Ali|Hassan', 'Sooraj|Kumar', 'GhulamAbbas|Channa', 'Muhammad|Saleh', 'Ali|Ali', 'Ayazaliayaz|Ayazaliayaz', 'Asif|Baloch', 'Mujeeb|Bds', 'Rana|Mustak', 'Ali|Rind', 'Amjad|Ali', 'سلامدين|سلامدين', 'Himat|Ali', 'Amanullah|Abro', 'Shookat|Ali', 'Mushoque|Malokhani', 'Zulifqar|Ali', 'Fareed|Abro', 'Zuhaib|Ali', 'Rasmyh|Rasmyh', 'Zubair|Ali', 'Waheed|Ali', 'Mohsin|Shaikh', 'Muzamil|Rajput', 'Gul|Bahar', 'Zaffar|Khoso', 'Akram|Ali', 'Rana|Sajids', 'Noor|Highlights', 'Basher|Baloch', 'Musam|Aill', 'Jamshed|Rana', 'علی|مولا', 'Hero|G', 'Rematullha|Rajpoot', 'Ustad|Hanif', 'Zubair|Ali', 'Rana|Abdul', 'Kamran|Ali', 'Kosar|Vighamal', 'Mansoor|Ali', 'Nadeem|Raza', 'Niaz|Hussan', 'Awais|Malik', 'Ammar|Shoz', 'Atta|Mohmad', 'Naeem|Khan', 'Sanju|Bhai', 'Waseem|Abass', 'Ghulam|M', 'Muhammad|Urs', 'Zahid|Hussain', 'Rana|Rajput', 'Meer|Jan', 'Waris|Ali', 'Inayat|Np', 'Sher|Muhhammd', 'Rana|Muzfar', 'Beni|Solis', 'Suba|Ali', 'Umesh|Kumar', 'Basit|Kahout', 'Rafiq|Khaskali', 'Saira|Khan', 'Rizwan|Ali', 'Shahbaz|Ali', 'Ail|Aagsr', 'M|Rafiq', 'Alom|Alahaj', 'Muhmmad|Waris', 'Sameer|Ali', 'Rana|Qaser', 'Fkgkodfj|Xkxnxuc', 'Saijad|Ali', 'Nadeem|Jan', 'Ajkhoso|Ajkhoso', 'Huzaifa|Ansari', 'Mazhar|Abbas', 'Molaa|Bux', 'Mashuq|Ali', 'Aneel|Kumar', 'Zahid|Hussain', 'Alihyder|Kalhoro', 'Rana|Rana', 'Bashir|Ahmed', 'Khalid|Hussein', 'Mumtaz|Ali', 'Arif|Memon', 'Ayoub|Baloch', 'Tehmoor|Ali', 'Imran|Ali', 'Shamshad|Ali', 'Ghulam|Hussain', 'Sajjad|Panhwar', 'Mole|Deno', 'Farooq|Bhaijan', 'Israr|Jakhrani', 'Imtyaz|Ali', 'Adeel|Masih', 'Gull|Hassan', 'Tando|Adam', 'منظور|راهو', 'Rana|Rehman', 'Mamtaz|Sehto', 'Amjid|Ali', 'Rana|Mubashir', 'Hamidullah|Mangsi', 'Ghulam|Nabi', 'Ahmed|Ali', 'Syedjaved|Shah', 'Rao|Hassan', 'Papoo|Kumar', 'Mehtab|Ali', 'Rana|Kashif', 'Rana|Wnus', 'Farman|Ali', 'Zulifiqar|Zulifqar', 'Sadam|Chandio', 'Mitho|Mallah', 'کاشف|راجپوت', 'Shamshaad|Rahoo', 'Hajan|Abbasi', 'Muneer|Zaib', 'Ayaz|Ayaz', 'Zain|Ali', 'Ghulam|Muhammad', 'Rao|Bilal', 'Babu|Khan', 'Rana|Ikram', 'Rana|Nasir', 'Amen|Rajpot', 'Fardeen|Panhwar', 'نگاھ|حبيب', 'Nadeem|Ali', 'Najaf|Ali', 'عمران|عباسی', 'Sahil|Shah', 'Ali|Hassan', 'Sonu|Jani', 'Ajmal|Abbasi', 'Abn|Rajab', 'Imtiyaz|Yousufzai', 'Dildar|Ali', 'Adil|Rao', 'Badshah|Yt', 'Sawan|Ali', 'Ali|Ahmed', 'Amir|Ali', 'Amjad|Ali', 'Shahid|Khan', 'Siama|Khan', 'Gulam|Shabir', 'Tehmoor|Hassan', 'Ghulam|Ali', 'Masum|Ali', 'Dedar|Ali', 'Shani|Jutt', 'Rintu|Kumar', 'Sikandar|Shah', 'Furqan|Jutt', 'Rahil|Ali', 'Rana|Shehzad', 'Nisha|Kumari', 'Jamshed|Khan', 'Zawar|Safdar', 'Murtaza|Ali', 'Muhammad|Aijaz', 'Punhal|Ali', 'Bisharat|Mirbahar', 'Xtylíśh|Shahmir', 'نصيراحمد|ميمڻ', 'Darya|Khan', 'Imdad|Khoso', 'Allyas|Allyas', 'Amjad|Ali', 'Bhatti|G', 'Faizan|Aziz', 'Rashad|Baloch', 'Abdul|Jabar', 'Rana|Shafiq', 'Hamadullah|Lakho', 'Ziafat|Khan', 'Faqeer|N', 'Rana|Ibrar', 'Shafi|Muhmmad', 'Awees|Ali', 'Amir|Ali', 'Ali|Khan', 'QaMar|ZaMan', 'Rana|Naveed', 'فرینا|فرینا', 'Ghul|Sher', 'Safeer|Khaskhali', 'Rana|Asim', 'Farhan|Ali', 'Ghulam|Abbas', 'Zulfiqar|Ali', 'Zakir|Ali', 'Rhman|Ali', 'Rana|Ali', 'Muneer|Khan', 'Mumtaz|Ali', 'Nadeem|Ali', 'Zameer|Shah', 'Faheem|Ahmad', 'Pordip|Mandal', 'Shahzaib|Rahman', 'Zidi|Bacha', 'Waqar|Rajput', 'Ali|Akbar', 'Ali|Raza', 'Sabir|Ali', 'Rana|Qurban', 'Ali|Bahte', 'Sajad|Ali', 'Ahadattaullah|Malik', 'Muzammil|Hussain', 'Jan|Muhammad', 'Fasial|S', 'Ameer|NaNa', 'Makro|Sharif', 'Mithal|Khaskheli', 'محمدموسا|محمدموسا', 'Mitho|Mallah', 'Muzzamil|Ali', 'Ahmad|Hassan', 'Babar|Babar', 'Zawar|Muhammad', 'Rana|Nadir', 'Mazhar|Ali', 'Rana|Irfan', 'Bilal|Abbasi', 'Ghulam|Jaffar', 'Asif|Rana', 'Mœhäməd|Řhæ', 'M|Nawaz', 'Farooq|Ali', 'Ashfaq|Rahoo', 'Azmat|Ali', 'Mateen|Rana', 'Shan|Ali', 'Çhårîyē|Çhøkrī', 'Parwez|Ali', 'Azhar|Hussain', 'Shahabaz|Ali', 'Syed|Ghot', 'Zahid|Hussain', 'Mir|Babu', 'Zarik|M', 'Shakel|Ansari', 'Hafiz|Imran', 'Shah|Zaib', 'Bilal|Jan', 'Asif|Asif', 'Asif|Asif', 'Muzafar|Rajbut', 'Makhdoom|Ghulam', 'Rana|Farooq', 'Gulam|Yaseen', 'Ashiqe|Jatt', 'Arshad|Brohi', 'Nazeer|Ahmed', 'Sajad|Ali', 'Mircho|Mal', 'Rana|Junaid', 'Lakho|Mal', 'Sajid|Ali', 'Raees|Rahat', 'Irfan|Ali', 'Rana|Imran', 'Ali|Mughal', 'Riaz|Khan', 'Ahsan|Bozdar', 'Shahidalisolangi|Shahidalisolangi', 'Tariq|Tariq', 'Rao|Nasir', 'Zahid|Ali', 'Shahzad|Madni', 'Sarfaraz|Rahu', 'Mubashair|Rana', 'Ahsan|Khoso', 'Jalger|Bhatti', 'Rana|Wajid', 'Lala|Aziz', 'Shakir|Abbasi', 'Ali|Asgar', 'Ruble|Hasan', 'Abdul|Rehman', 'Azizullah|Soomro', 'Abbas|Ali', 'Muhammad|Ali', 'Rana|Wajid', 'Rana|Musharaf', 'Rashid|Qureshi', 'Shahmeer|Chandio', 'Shan|Ali', 'Ahmed|Qureshi', 'Zaheer|Abbas', 'Imran|Ali', 'Asif|Khan', 'Shahid|Ali', 'Mangii|Mangii', 'Momin|Ali', 'Meer|Shan', 'Muqu|Poiro', 'Umar|Shahzad', 'Waris|Ali', 'Numwar|Ali', 'Muhammad|Tahir', 'AKhtar|Ali', 'Rana|Sajid', 'Sarfarazmemon|Attad', 'Salim|Junejo', 'Mashque|Ali', 'Hassnan|Ali', 'Irfan|Ali', 'Adv|Ali', 'Himmat|Ali', 'Khalid|Jamil', 'Mohsin|Rajput', 'Syed|Nadir', 'Raheem|Punho', 'Rana|Abdullah', 'Rana|Noaman', 'Mansoor|Solangi', 'Imran|Jaan', 'Waris|Ali', 'Rana|Mubasher', 'Mujahid|Ali', 'Hussnain|Rajpoot', 'Chaudhary|Abdul', 'Haider|Baloch', 'Ali|Dino', 'Mir|Khan', 'Irfan|Fatima', 'Arshad|Baloch', 'Shakir|Abbasi', 'Naveed|Rind', 'Gul|Muhammad', 'Meer|Murtaza', 'Papo|Papo', 'Nisar|Ali', 'Gbhs|Bhit', 'Sadoro|Jan', 'Rana|Moon', 'Ramzan|Jan', 'Rana|Zakir', 'Rao|Waqas', 'M|Waqas', 'Rana|Rana', 'Rukhsar|Haidry', 'RaNa|BOby', 'M|Juman', 'Sadiq|Ali', 'Manik|Khan', 'Ran|A', 'Ghulab|Hussain', 'Ronaq|Ali', 'Tarique|Ali', 'Abdul|Qadir', 'Zawar|Sohana', 'Mehran|Rajput', 'Sikandar|Ali', 'Ãtîf|Â', 'Meer|Shahzeb', 'Sajjad|Abbasi', 'Rana|Naeem', 'Bashir|Ahmed', 'Rafeh|Rajpoot', 'ẞk|KhÄñ', 'Imtiaz|Khoso', 'Alex|Shahzad', 'Aman|Abbasi', 'Mehran|Rajput', 'Raja|Rajpot', 'Bahdur|Ali', 'Hammad|Ali', 'Salman|Salman', 'Shahzad|Shahzad', 'AtaullAh|Khan', 'Rafique|Mirani', 'Arbab|Ali', 'Nisar|Ali', 'Zahid|Hussain', 'Rana|Shahzad', 'Rana|Ramzan', 'Noro|Mohmad', 'Riaz|Rajput', 'Mahbat|Khan', 'Ahsan|Ali', 'Rana|Ikram', 'Qamar|Abbas', 'Jahanzib|Ali', 'Rana|Sunny', 'Rao|Yasir', 'Muhammad|Mithal', 'Ashiq|Hussain', 'Ha|Ni', 'Abdul|Latif', 'Meer|Mortaz', 'Meer|Zohaib', 'Zahid|Bhatti', 'Awais|Rajput', 'Ali|Bux', 'Abdul|Hakeem', 'Hassnain|Muavia', 'Syed|Junaid', 'Riaz|Machi', 'Ahsan|Abro', 'Hyder|Ali', 'Sattar|Sattar', 'Sayed|Sharafat', 'Syed|Bilalarif', 'Lal|Muhmmad', 'Mohsin|Ali', 'Asif|Ali', 'Juleed|Shah', 'Hayat|Khan', 'Ali|Bux', 'पवन|अल्लापुर', 'Ghulam|Nabi', 'Zaheer|Ali', 'Soomar|Bughio', 'Madad|Ali', 'Naeem|Chohan', 'Javed|Javed', '
