# 生活小助理
import random
#r = random.randint(1,16)
#print(r)

phone_numbers_str = "匪警[110],火警[119],急救中心[120],道路交通事故报警[122],水上求救专用电话[12395],天气预报[12121],报时服务[12117],森林火警[12119],电力服务[95598],红十字会急救台[999],公安短信报警[12110],通用紧急求救[112],信产部IP/网站备案[010-66411166]"
weather_str = "北京,2019年1月12日,多云,8°C,-4°C,南风3级~上海,2019年1月12日,小雨,9°C,6°C,北风2级~广州,2019年1月12日,阵雨转多云,22°C,15°C,持续无风向微风"

# 生成双色球
def generate_unionlotto(number):
    for j in range(0,int(number)):
        for i in range(0,6):
            red = random.randint(1,33)
            print(red,end = " ")
        blue = random.randint(1,16)
        print(blue)

# 号码百事通功能
def find_phone(keyword):
    phone_list = phone_numbers_str.split(",")
    for p in phone_list:
        if p.find(keyword) != -1:
            print(p)

def get_weather(city):
    city_list = weather_str.split("~")
    print(city_list)
    weather_data = {}
    for i in range(0, len(city_list)):
        w = city_list[i].split(",")
        # print(w)
        weather = {"name": w[0], "date": w[1], "weather": w[2], "max": w[3], "min": w[4], "wind": w[5]}
        # print(weather)
        weather_data[weather["name"]] = weather
    #print(weather_date)
    if city in weather_data:
        return weather_data.get(city)
    else:
        return {}

while(True):
    print("1-双色球随机选号")
    print("2-号码百事通")
    print("3-明日天气预报")
    print("0-结束程序")
    c = input("请输入功能编号:")
    if c == "1":
        n = input("您要生成几注双色球号码:")
        generate_unionlotto(n)
    elif c == "2":
        n = input("请输入您要查询的机构或电话号码:")
        find_phone(keyword=n)
    elif c == "3":
        n = input("请输入您要查询的城市:")
        w = get_weather(n)
        print(w)
        if "name" in w:
            print("{date}{name}{weather}{max}/{min}{wind}".format_map(w))
        else:
            print("未找到{0}的天气数据".format(n))
        print("=================================================")
    elif c == "0":
        break
    else:
        print("您输入的功能编号有误,请重新输入")
print("感谢您的使用，祝您生活愉快，再见！")
