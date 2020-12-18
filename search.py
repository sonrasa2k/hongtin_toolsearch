import googlesearch
from bs4 import BeautifulSoup
import requests

class search :
    def __init__(sefl,file_path):
        sefl.file_path = file_path
    def results_search(self):
        list_url_true = []
        list_title_true = []
        list_des_true = []
        list_key = []
        with open(self.file_path,encoding="utf8") as fp:
            line = fp.readline()
            cnt = 1
            while line:
                key = line.strip()
                print(key)
                list_key.append(key)
                rs = googlesearch.search(key,num_results=60,lang="vn")
                i = 0
                dung = 1
                while i < 80 and dung <= 20 :
                    try :
                        response = requests.get(rs[i])
                        soup = BeautifulSoup(response.content, "html.parser")
                        try :
                            titles = soup.find('meta',property="og:title").attrs["content"]
                        except :
                            titles = soup.find('title').text
                        dis = soup.find('meta', property="og:description").attrs["content"]
                        link_dau = '<link' + str(dung)+'>'
                        link_cuoi = '</link'+ str(dung)+'>'
                        rs[i] = link_dau+str(rs[i])+link_cuoi
                        list_url_true.append(rs[i])
                        print(rs[i])
                        title_dau = '<tieude' + str(dung)+'>'
                        title_cuoi = '</tieude'+ str(dung)+'>'
                        titles = title_dau + str(titles)+title_cuoi
                        print(titles)
                        list_title_true.append(titles)
                        mota_dau = '<mota' + str(dung)+'>'
                        mota_cuoi = '</mota'+ str(dung)+'>'
                        dis = mota_dau + str(dis) + mota_cuoi
                        list_des_true.append(dis)
                        print(dis)
                        dung += 1
                        i += 1
                    except:
                        print("trang web khong truy cap duoc")
                        i += 1
                    line = fp.readline()
                    cnt += 1
        for i in range(len(list_key)):
            file_name = str(list_key[i])+'.txt'
            with open(file_name,'w+',encoding="utf-8") as wf:
                list_key[i] = '<key>'+str(list_key[i])+'</key'
                wf.write(list_key[i]+'\n')
                j = i
                while j < i*20 + 20 :
                    wf.write(list_title_true[j]+'\n')
                    wf.write(list_url_true[j]+'\n')
                    wf.write(list_des_true[j]+'\n')
                    print("complete row")
                    j +=1
        wf.close()


