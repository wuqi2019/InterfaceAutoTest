

def sso_login():
    """sso登录"""
    pass


def bmy_login(indta, getToken=True):
    """企业云登录"""
    url = f'{HOST}/auth/login'
    # token加密
    authorization = get_authorization()
    header = {"Authorization": authorization}

    payload = {"username": "", "password": "", "imageId": "", "grant_type": "passwordImageCode", "imageCode": ""}
    # 账号
    payload['username'] = indata['username']

    # 密码加密
    password_Encrypted = pwd_encrypted(indata['password'])
    payload['password'] = password_Encrypted

    # 获取图片信息
    imageinfo = get_imageCode(payload['username'], payload['password'])
    payload['imageId'] = imageinfo[0]
    payload['imageCode'] = imageinfo[1]

    # print("我是header：",header)
    # print('我是url：',url)
    # print('我是payload：',payload)

    # # 请求
    resp = requests.post(url, data=payload, headers=header)
    if getToken:
        token = resp.json()['data']['token']  # 数据权限会藏在token中
        return get_authorization(defaultToken=token)
    else:
        return resp.json()



