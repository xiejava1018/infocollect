# -*- coding: utf-8 -*-
"""
    :author: XieJava
    :url: http://ishareread.com
    :copyright: © 2019 XieJava <xiejava@ishareread.com>
    :license: MIT, see LICENSE for more details.
"""
import requests
from bs4 import BeautifulSoup
from app.exts import db

from app.module.models.dbmodels import WhoisInfo

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}

whois_service_url2='http://whois.chinafu.com/whois.php'

domain_info_dict={'Domain Name':'域名','Registrar':'注册商','Registrar Abuse Contact Email':'联系邮箱','Registrar Abuse Contact Phone':'联系电话','Creation Date':'注册日期','Updated Date':'更新日期','Registry Expiry Date':'到期日期','Registrar WHOIS Server':'域名服务器','Name Server':'DNS','Domain Status':'状态'}

def getwhoisinfobydute(domain):
    whois_service_url = 'https://www.dute.me/tools/whois/?action=do'
    post_data={"domain":domain}
    ret_result = {}
    try:
        post_result=requests.post(whois_service_url,post_data)
        if post_result.status_code==200:
            ret_str = post_result.content.decode('utf-8')
            soup = BeautifulSoup(ret_str, 'lxml')
            items=soup.find_all('br')
            for item in items:
                item_info=item.previous
                if ":" in item_info:
                    item_split_info=item_info.split(':')
                    key=item_split_info[0].strip()
                    if key in domain_info_dict:
                        key=domain_info_dict[key]
                        value = item_split_info[1].strip()
                        if key in ret_result:
                            value=ret_result[key]+' '+value
                        ret_result[key]=value
            ret_result['详情'] = ret_str
    except Exception as r:
        print('未知错误 %s' % (r))
    #ret_result=json.dumps(ret_result,ensure_ascii=False)
    return ret_result

def getwhoisinfobychinafu(domain):
    ret_result = {}
    result=getWhoisInfoFromDB(domain)
    if len(result)==0:
        whois_service_url = 'http://whois.chinafu.com/whois.php'
        post_data={"domain":domain}

        try:
            post_result=requests.post(whois_service_url,post_data)
            if post_result.status_code == 200:
                ret_str = post_result.content.decode('utf-8')
                soup = BeautifulSoup(ret_str, 'lxml')
                items_tr =soup.find(name='table',attrs={'class':'listtable'}).find_all(name='tr')
                for item_tr in items_tr:
                    td_item=item_tr.find(name='td')
                    if 'colspan' in td_item.attrs:
                        key_name='详情'
                        key_value=td_item.find(name='div',id='tab1').text
                    else:
                        key_name=item_tr.find(name='th').text
                        key_value=item_tr.find(name='td').text
                    ret_result[key_name]=key_value
                addchinafuWhoisInfo2DB(ret_result)
        except Exception as r:
            print('未知错误 %s' % (r))
    #ret_result = json.dumps(ret_result, ensure_ascii=False)
    else:
        ret_result=result[0]
    return ret_result

def getWhoisInfoFromDB(domainname):
    whoisInfos=db.session.execute('select * from whoisinfo where domain_name="%s" and updated_time > DATE_SUB(CURDATE(), INTERVAL 1 WEEK)' % domainname).fetchall()
    whoisInfo_dics=[]
    for whoisInfo in whoisInfos:
        chinafuwhoisinfo_dic=chinafuwhoisinfo2dic(whoisInfo)
        whoisInfo_dics.append(chinafuwhoisinfo_dic)
    return whoisInfo_dics

def chinafuwhoisinfo2dic(whoisinfo):
    chinafuwhoisinfo_dic={}
    chinafuwhoisinfo_dic['域名DomainName']=whoisinfo.domain_name
    chinafuwhoisinfo_dic['域名状态Domain Status']=whoisinfo.domain_status
    chinafuwhoisinfo_dic['注册商Sponsoring Registrar']=whoisinfo.registrar
    chinafuwhoisinfo_dic['DNS 服务器Name Server']=whoisinfo.name_server
    chinafuwhoisinfo_dic['注册日期Registration Date']=whoisinfo.registrar_creation_date
    chinafuwhoisinfo_dic['更新日期Update Date']=whoisinfo.registrar_updated_date
    chinafuwhoisinfo_dic['到期日期Expiration Date']=whoisinfo.registrar_expiry_date
    chinafuwhoisinfo_dic['详情']=whoisinfo.detail
    chinafuwhoisinfo_dic['来源']=whoisinfo.source
    return chinafuwhoisinfo_dic

def addchinafuWhoisInfo2DB(chinafuWhoisInfo_dic):
    chinafuWhois=WhoisInfo()
    chinafuWhois.domain_name=chinafuWhoisInfo_dic.get('域名DomainName')
    chinafuWhois.domain_status=chinafuWhoisInfo_dic.get('域名状态Domain Status','')
    chinafuWhois.registrar=chinafuWhoisInfo_dic.get('注册商Sponsoring Registrar','')
    chinafuWhois.name_server=chinafuWhoisInfo_dic.get('DNS 服务器Name Server','')
    chinafuWhois.registrar_creation_date=chinafuWhoisInfo_dic.get('注册日期Registration Date','')
    chinafuWhois.registrar_updated_date = chinafuWhoisInfo_dic.get('更新日期Update Date', '')
    chinafuWhois.registrar_expiry_date = chinafuWhoisInfo_dic.get('到期日期Expiration Date', '')
    chinafuWhois.detail=chinafuWhoisInfo_dic.get('详情', '')[0:10000]
    chinafuWhois.source = '中国福网'
    db.session.execute('delete from whoisinfo where domain_name="%s" and source="%s"' % (chinafuWhoisInfo_dic.get('域名DomainName'), chinafuWhois.source))
    db.session.add(chinafuWhois)
    db.session.commit()


if __name__=='__main__':
    ipinfo=getwhoisinfobychinafu('transfar.com')
    print(ipinfo)