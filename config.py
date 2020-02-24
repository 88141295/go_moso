articleId = "6E69F4F1-518A-11EA-9C7F-98039B1848C6&id=DB3CC8C0-8262-C3ED-A312-7DC32791B771"#此处为蓝墨云活动的id
courseId = "6E69F4F1-518A-11EA-9C7F-98039B1848C6"#此处为蓝墨云的班级id
sleepNumber = 40#此值/60等于蓝墨云真实的做题用时时间
k = 20#此值代表随机选择试题的数量
URL_ROOT = r'https://www.mosoteach.cn/web/index.php?c=passport&m=account_login'#蓝墨云登陆提交地址
values = {
        'account_name': '15766771113',  # 此处为蓝墨云的账号
        'user_pwd': 'linchucheng',  # 此处为蓝墨云的密码
        'remember_me': 'N'  # 是否记住登陆状态，默认不记住
}
headers = {
        'Host': 'www.mosoteach.cn',
        'Accept-Encoding': 'gzip, deflate',
        'Origin': 'https://www.mosoteach.cn',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Referer': 'https://www.mosoteach.cn/web/index.php?c=passport&m=index',
}

subJectUrl = "https://www.mosoteach.cn/web/index.php?c=interaction_quiz&m=reply&clazz_course_id=" + courseId + "&id=" + articleId + "&order_item=group"
