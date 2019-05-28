def login_api(req):
    if req.method == 'GET':
        return render(req, 'login.html')
    else:
        params = req.POST
        # 用户输入的
        code = params.get("verify_code")
        # 从session获取的
        server_code = req.session.get("code")
        print(server_code)
        # 做判断比较
        if server_code.lower() == code.lower():
            return HttpResponse("验证成功")
        else:
            return HttpResponse('输入验证码错误')