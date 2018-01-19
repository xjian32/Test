import json
def djson():
    dicT={}
    key = ['Name','Phone']
    value = []
    name = input("Please input your name:")
    phone = int(input("Please input your phone:"))
    value.extend([name, phone])

    dicT = dict(zip(key, value))
    print('字典格式：\n', dicT)
    print('\n','='*50)
    print('\nJson格式：\n', json.dumps(dicT, ensure_ascii=False, indent=4))

if __name__ == '__main__':
    djson()
