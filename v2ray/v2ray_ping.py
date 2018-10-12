# -*- coding: utf-8 -*-
# !/usr/bin/env python3
# 登陆授权

# 获取服务器列表
# 转换json{
# "SVIP":"svip-kt.v2cloud.xyz",
# "HKT1":"hk-hkt.v2cloud.xyz"}
# 测速
# alias vpn='python3 /Users/joey/PycharmProjects/vpn/v2ray_ping.py [user_name] [password]'
import requests
import json
import os
import sys

json_file = os.getcwd() + "/vpn.json"


def auth(user_name, password):
    url = 'https://v2rayapi.com/client/api.php?s=user.auth'
    response = requests.post(url, data={'username': user_name,
                                        'password': password, 'getToken': '1'}, timeout=15)

    data = json.loads(response.text)
    print(response.text)
    token = data['data']
    print(token)
    return token


def get_vpn_list(token):
    url = 'https://v2rayapi.com/client/api.php?s=whmcs.hosting&token=' + token
    response = requests.get(url, timeout=15)
    data = json.loads(response.text)
    nodes = data['data'][0]['node']
    print(nodes)
    dict = {}
    tsl_list = []
    for node in nodes:
        print(node)
        name = node['name']  # .encode('latin1').decode('unicode_escape')
        server = node['server']
        print(name)
        dict[name] = server
        if node["tls"] == 1:
            tsl_list.append(name)
    print(dict)
    with open(json_file, 'w') as f:
        json.dump(dict, f)
    return json_file, tsl_list


def ping_vpn(vpn_json):
    os.system("mping -p " + vpn_json)
    os.system("rm " + json_file)


def main():
    user_name = sys.argv[1]
    password = sys.argv[2]
    print(user_name + " " + password)
    token = auth(user_name, password)
    if token is None:
        print("获取授权失败")
        return

    vpn_json, tsl_list = get_vpn_list(token)
    # vpn_json = get_vpn_list('d9ccc738-4e2e-49d3-aad0-3622ed176691')
    print(vpn_json)
    if vpn_json is None:
        print("获取vpn列表失败")
        return

    ping_vpn(vpn_json)
    print("支持 tsl 的服务器：")
    print(tsl_list)


if __name__ == '__main__':
    main()
