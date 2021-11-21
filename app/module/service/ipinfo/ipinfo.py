import json
import geoip2.database
import requests

from app.module.models.dbmodels import IPInfo
from app.exts import db

from config import Config

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}

ipinfo_dic={
  "ip": "114.114.114.114",
  "hostname": "public1.114dns.com",
  "city": "Beijing",
  "region": "Beijing",
  "country": "CN",
  "loc": "39.9075,116.3972",
  "org": "AS56046 China Mobile communications corporation",
  "timezone": "Asia/Shanghai",
  "readme": "https://ipinfo.io/missingauth"
}

def getipinfo(ip):
    ipinfos=getIPInfo_dics(ip)
    if len(ipinfos)==0:
        ipinfo1=getipinfobytaobao(ip)
        ipinfo2=getipinfobyipinfo(ip)
        ipinfo3=getipinfobyipapi(ip)
        ipinfo4=getipinfobygeoip2(ip)
        if len(ipinfo1)>0:
            ipinfos.append(ipinfo1)
        if len(ipinfo2)>0:
            ipinfos.append(ipinfo2)
        if len(ipinfo3)>0:
            ipinfos.append(ipinfo3)
        if len(ipinfo4)>0:
            ipinfos.append(ipinfo4)
    return ipinfos

def getipinfobytaobao(ip):
    taobaoIp_url = 'https://ip.taobao.com/outGetIpInfo'
    post_data={"ip":ip,"accessKey":"alibaba-inc"}
    ret_ipinfo= {}
    try:
        return_data=requests.post(taobaoIp_url,post_data)
        #其中返回数据中code的值的含义为，0：成功，1：服务器异常，2：请求参数异常，3：服务器繁忙，4：个人qps超出
        return_json=json.loads(return_data.text)
        if return_json['code']==0:
            ret_ipinfo['ip']=return_json['data']['ip']
            ret_ipinfo['country']=return_json['data']['country']
            ret_ipinfo['region']=return_json['data']['region']
            ret_ipinfo['org']=''
            ret_ipinfo['city'] = return_json['data']['city']
            ret_ipinfo['isp']=return_json['data']['isp']
            ret_ipinfo['loc'] = ''
            ret_ipinfo['timezone'] = ''
            ret_ipinfo['source']='淘宝IP'
            addIPInfo2DB(ret_ipinfo)
    except Exception as e:
        print('未知错误 %s' % (e))
    return ret_ipinfo

def getipinfobyipinfo(ip):
    api_url='http://ipinfo.io/'+ip
    ipinfo = {}
    try:
        req_return = requests.get(api_url)
        if req_return.status_code == 200:
            ipinfo = json.loads(req_return.text)
            ipinfo['source']='ipinfo.io'
            addIPInfo2DB(ipinfo)
    except Exception as e:
        print('未知错误 %s' % (e))
    return ipinfo

def getipinfobyipapi(ip):
    api_url='http://ip-api.com/json/'+ip
    ipinfo={}
    try:
        req_return=requests.get(api_url)
        if req_return.status_code==200:
            ipinfo=json.loads(req_return.text)
            ipinfo['ip'] = ip
            ipinfo['source'] = 'ip-api.com'
            ipinfo['loc'] = str(ipinfo['lat'])+','+str(ipinfo['lon'])
            addIPInfo2DB(ipinfo)
    except Exception as e:
        print('未知错误 %s' % (e))
    return ipinfo

def getipinfobygeoip2(ip):
    ipinfo={}
    dbdir=Config.geoLiteDBdir
    with geoip2.database.Reader(dbdir) as reader:
        response = reader.city(ip)
        ipinfo['ip'] =ip
        ipinfo['country'] = response.country.names['zh-CN']
        ipinfo['region'] =''
        ipinfo['city']=response.city.name
        ipinfo['org'] =''
        ipinfo['loc'] = str(response.location.latitude)+','+str(response.location.longitude)
        ipinfo['timezone'] = response.location.time_zone
        ipinfo['source'] = 'GeoIP'
        addIPInfo2DB(ipinfo)
    return ipinfo

def addIPInfo2DB(ipinfo):
    #如果超过7天就开始更新,先删除后插入
    newipinfo = IPInfo()
    newipinfo.ip = ipinfo.get('ip')
    newipinfo.country = ipinfo.get('country','')
    newipinfo.region = ipinfo.get('region','')
    newipinfo.city = ipinfo.get('city','')
    newipinfo.org = ipinfo.get('org','')
    newipinfo.isp = ipinfo.get('isp', '')
    newipinfo.loc = ipinfo.get('loc','')
    newipinfo.timezone = ipinfo.get('timezone','')
    newipinfo.source = ipinfo.get('source')
    db.session.execute('delete from ipinfo where ip="%s" and source="%s"' % (ipinfo.get('ip'),ipinfo.get('source')))
    db.session.add(newipinfo)
    db.session.commit()

def getIPInfo_dics(ip):
    ipinfos=db.session.execute('select * from ipinfo where ip="%s" and updatetime > DATE_SUB(CURDATE(), INTERVAL 1 WEEK)' % ip).fetchall()
    ipinfo_dics=[]
    for ipinfo in ipinfos:
        ipinfo_dic=ipinfo2dic(ipinfo)
        ipinfo_dics.append(ipinfo_dic)
    return ipinfo_dics

def ipinfo2dic(IPInfo):
    ret_ipinfo = {}
    ret_ipinfo['ip'] =IPInfo.ip
    ret_ipinfo['country'] = IPInfo.country
    ret_ipinfo['region'] = IPInfo.region
    ret_ipinfo['org'] = IPInfo.org
    ret_ipinfo['city'] = IPInfo.city
    ret_ipinfo['isp'] =IPInfo.isp
    ret_ipinfo['loc'] = IPInfo.loc
    ret_ipinfo['timezone'] = IPInfo.timezone
    ret_ipinfo['source'] = IPInfo.source
    return ret_ipinfo

if __name__=='__main__':
    ipinfo=getipinfobyipapi('114.114.114.114')
    print(ipinfo)