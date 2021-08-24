from subprocess import check_output


def btest():
    # 用 node 直接执行 js 脚本
    bytesTxt = check_output(['node', 'bide.js', 'BD00795187'], timeout=100)
    print(bytesTxt.decode('utf8').strip())


if __name__ == '__main__':
    btest()
