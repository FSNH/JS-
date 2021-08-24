from subprocess import check_output


def test():
    # 直接调用
    # bytesTxt = check_output('node -e console.log(3+2)', timeout=100)
    # print(bytesTxt.decode('utf8').strip())

    # 用 node 直接执行 js 脚本
    bytesTxt = check_output(['node', 'baike.js', '54602011'], timeout=100)
    print(bytesTxt.decode('utf8').strip())


if __name__ == '__main__':
    test()
