import os
import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Python For Beginners", page_icon=":books:", layout="wide")

github_path = "https://raw.githubusercontent.com/Chase-Yi/Python-For-Beginners/refs/heads/main/image"

@st.cache_data
def load_image(image_path):
    return image_path

key_concept = ['Print','Variable','Math','Comment','Data Type','Interactive Mode','Input','Condition',
    'Logical Operators', 'List', 'Dictionary', 'For Loop', 'While Loop', 'String Formatting', 'Function',
    'Importing Module', 'Object-Oriented Programming', 'Class', 'Inheritance', 'File Path', 'Read File', 'Write File',
    'Higher-order function & Lambda']

if 'current_option' not in st.session_state:
    st.session_state['current_option'] = key_concept[0]

option = option_menu(
    menu_title=None,
    options=key_concept,
    icons=['filetype-py']*len(key_concept),
    orientation='horizontal',
    default_index=key_concept.index(st.session_state['current_option']),
    key='menu')

st.session_state['current_option'] = option

if option == 'Print':
    st.write('### print | 打印')

    st.page_link("https://www.bilibili.com/video/BV1944y1x7SW/?p=6&share_source=copy_web&vd_source=7bf7c3af03910ae8dbc83caae78ba1aa",
                label="print | 让程序给你打印“爸爸”", icon=":material/smart_display:")
    py_1 = '''
        print("Dad!")
        print("妈！！")
        '''
    st.code(py_1,language='python')

    st.page_link("https://www.bilibili.com/video/BV1944y1x7SW/?p=7&share_source=copy_web&vd_source=7bf7c3af03910ae8dbc83caae78ba1aa",
                label="更多 print | 让程序给你打印一首诗", icon=":material/smart_display:")
    py_2 = '''
        print("你好" + " 这是一句代码" + " 哈哈")
        '''
    py_3 = '''
        print("""君不见，黄河之水天上来，奔流到海不复回。
        君不见，高堂明镜悲白发，朝如青丝暮成雪。
        人生得意须尽欢，莫使金樽空对月。
        天生我材必有用，千金散尽还复来。
        烹羊宰牛且为乐，会须一饮三百杯。
        岑夫子，丹丘生，将进酒，君莫停。
        与君歌一曲，请君为我倾耳听。
        钟鼓馔玉不足贵，但愿长醉不复醒。
        古来圣贤皆寂寞，惟有饮者留其名。
        陈王昔时宴平乐，斗酒十千恣欢谑。
        主人何为言少钱，径须沽取对君酌。
        五花马，千金裘，呼儿将出换美酒，
        与尔同销万古愁。""")
        '''
    st.code(py_2,language='python')
    st.code(py_3,language='python')

if option == 'Variable':
    st.write('### variable | 变量')

    st.page_link("https://www.bilibili.com/video/BV1944y1x7SW/?p=8&share_source=copy_web&vd_source=7bf7c3af03910ae8dbc83caae78ba1aa",
                label="Python变量 | 怎么让程序记住你对象的手机号", icon=":material/smart_display:")
    py_4 = '''
    greet = "您好，吃了么，"
    greet_chinese = greet
    greet_english = "Yo what's up, "
    greet = greet_english
    print(greet + "张三")
    print(greet + "李四")
    print(greet + "王五")
    print(greet_chinese + "张三")
    '''
    st.code(py_4,language='python')

    st.page_link("https://www.bilibili.com/video/BV1944y1x7SW/?p=9&share_source=copy_web&vd_source=7bf7c3af03910ae8dbc83caae78ba1aa",
                label="Python命名规则 | 哪些变量名算好名字", icon=":material/smart_display:")
    # add image
    st.image(load_image(os.path.join(github_path, 'variable_1.png')),caption="下划线命名法")
    st.image(load_image(os.path.join(github_path, 'variable_2.png')))
    st.image(load_image(os.path.join(github_path, 'variable_3.png')),caption="Python keywords")

if option == 'Math':
    st.write('### math | 数学')

    st.page_link("https://www.bilibili.com/video/BV1944y1x7SW/?p=10&share_source=copy_web&vd_source=7bf7c3af03910ae8dbc83caae78ba1aa",
                label="Python数学运算 | 用代码秒杀计算器", icon=":material/smart_display:")
    py_5 = '''
    # 写一个一元二次求根公式计算器
    # x^(2) + 9x + 20 
    
    import math
    a = 1
    b = 9
    c = 20
    delta = b ** 2 - 4 * a * c
    print((-b + math.sqrt(delta)) / (2 * a))
    print((-b - math.sqrt(delta)) / (2 * a))
    '''
    st.code(py_5,language='python')

if option == 'Comment':
    st.write('### comment | 注释')

    st.page_link("https://www.bilibili.com/video/BV1944y1x7SW/?p=11&share_source=copy_web&vd_source=7bf7c3af03910ae8dbc83caae78ba1aa",
                label="Python注释 | 悄悄在代码里骂用户？", icon=":material/smart_display:")
    py_6 = '''
    # print("君不见，黄河之水天上来，奔流到海不复回。")
    # print("君不见，高堂明镜悲白发，朝如青丝暮成雪。")
    # print("人生得意须尽欢，莫使金樽空对月。")
    # print("天生我材必有用，千金散尽还复来。")
    # print("烹羊宰牛且为乐，会须一饮三百杯。")
    # print("岑夫子，丹丘生，将进酒，君莫停。")
    # print("与君歌一曲，请君为我倾耳听。")
    # print("钟鼓馔玉不足贵，但愿长醉不复醒。")
    # print("古来圣贤皆寂寞，惟有饮者留其名。")
    # print("陈王昔时宴平乐，斗酒十千恣欢谑。")
    # print("主人何为言少钱，径须沽取对君酌。")
    # print("五花马，千金裘，呼儿将出换美酒，")
    # print("与尔同销万古愁。")
    '''
    py_7 = '''
    """
    我是一段更加啰嗦的注释
    我感觉我有很多话想说
    以至于一行根本不够
    """
    '''
    st.code(py_6,language='python')
    st.code(py_7,language='python')

if option == 'Data Type':
    st.write('### data type | 数据类型')

    st.page_link("https://www.bilibili.com/video/BV1944y1x7SW/?p=12&share_source=copy_web&vd_source=7bf7c3af03910ae8dbc83caae78ba1aa",
                label="Python数据类型 | 程序世界的物种们", icon=":material/smart_display:")
    # add image
    st.image(load_image(os.path.join(github_path, 'data_type_1.png')),caption="数据类型")
    py_8 = '''
    # 对字符串求长度
    s = "Hello world!"
    print(len(s))
    
    # 通过索引获取单个字符
    print(s[0])
    print(s[len(s) - 1])
    
    # 布尔类型
    b1 = True
    b2 = False
    
    # 空值类型
    n = None
    
    # type函数
    print(type(s))
    print(type(b1))
    print(type(n))
    print(type(1.5))
    
    # 不能对布尔类型的变量使用len函数，因此下面一行会报错
    # len(b1)
    '''
    st.code(py_8,language='python')

if option == 'Interactive Mode':
    st.write('### interactive mode | 交互模式')

    st.page_link("https://www.bilibili.com/video/BV1944y1x7SW/?p=13&share_source=copy_web&vd_source=7bf7c3af03910ae8dbc83caae78ba1aa",
                label="Python交互模式 | 读一行执行一行", icon=":material/smart_display:")
    #add image
    st.image(load_image(os.path.join(github_path, 'interactive_mode_1.png')),caption="交互模式")

if option == 'Input':
    st.write('### input | 输入')

    st.page_link("https://www.bilibili.com/video/BV1944y1x7SW/?p=14&share_source=copy_web&vd_source=7bf7c3af03910ae8dbc83caae78ba1aa",
                label="Python input | 写个用户问答互动程序", icon=":material/smart_display:")
    py_9 = '''
    # 因为当前网页中提供的Python代码编辑器不支持用户输入功能,故采用直接赋值给变量的方法来代替用户输入
    # BMI = 体重 / (身高 ** 2)
    # user_weight = float(input("请输入您的体重（单位：kg）："))
    # user_height = float(input("请输入您的身高（单位：m）："))
    
    user_weight = float(70)
    user_height = float(1.8)
    user_BMI = user_weight / (user_height) ** 2
    print(f'您的体重为： {user_weight}kg')
    print(f'您的身高为： {user_height}m')
    print("您的BMI值为：" + str(user_BMI))
    '''
    st.code(py_9,language='python')

if option == 'Condition':
    st.write('### condition | 条件语句')

    st.page_link("https://www.bilibili.com/video/BV1944y1x7SW/?p=15&share_source=copy_web&vd_source=7bf7c3af03910ae8dbc83caae78ba1aa",
                label="Python条件语句 | 对象今天会生气吗", icon=":material/smart_display:")
    py_10 = '''
    # 因为当前网页中提供的Python代码编辑器不支持用户输入功能,故采用直接赋值给变量的方法来代替用户输入
    # mood_index = int(input("对象今天的心情指数是："))
    
    mood_index = int(90)
    if mood_index >= 60:
        print("恭喜，今晚应该可以打游戏，去吧皮卡丘！")
    else:  # mood_index < 60
        print("为了自个儿小命，还是别打了。")
    '''
    st.code(py_10,language='python')

    st.page_link("https://www.bilibili.com/video/BV1944y1x7SW/?p=16&share_source=copy_web&vd_source=7bf7c3af03910ae8dbc83caae78ba1aa",
                label="Python嵌套/多条件判断 | 对象今天会生气吗 II", icon=":material/smart_display:")
    py_11 = '''
    # 因为当前网页中提供的Python代码编辑器不支持用户输入功能,故采用直接赋值给变量的方法来代替用户输入
    # BMI = 体重 / (身高 ** 2)
    # user_gender = input("请输入您的性别，M或F（M表示男，F表示女）：")
    # user_weight = float(input("请输入您的体重（单位：kg）："))
    # user_height = float(input("请输入您的身高（单位：m）："))
    
    user_gender = 'M'
    user_weight = 70
    user_height = 1.8
    user_BMI = user_weight / user_height ** 2
    print("您的BMI值为：" + str(user_BMI))
    
    # 偏瘦：user_BMI <= 18.5
    # 正常：18.5 < user_BMI <= 25
    # 偏胖：25 < user_BMI <= 30
    # 肥胖：user_BMI > 30
    if user_BMI <= 18.5:
        if user_gender == "M":
            print("先生您好，此BMI值属于偏瘦范围。")
        elif user_gender == "F":
            print("女士您好，此BMI值属于偏瘦范围。")
        else:
            print("此BMI值属于偏瘦范围。")
    elif 18.5 < user_BMI <= 25:
        if user_gender == "M":
            print("先生您好，此BMI值属于正常范围。")
        elif user_gender == "F":
            print("女士您好，此BMI值属于正常范围。")
        else:
            print("此BMI值属于正常范围。")
    elif 25 < user_BMI <= 30:
        if user_gender == "M":
            print("先生您好，此BMI值属于偏胖范围。")
        elif user_gender == "F":
            print("女士您好，此BMI值属于偏胖范围。")
        else:
            print("此BMI值属于偏胖范围。")
    else:
        if user_gender == "M":
            print("先生您好，此BMI值属于肥胖范围。")
        elif user_gender == "F":
            print("女士您好，此BMI值属于肥胖范围。")
        else:
            print("此BMI值属于肥胖范围。")
    '''
    st.code(py_11,language='python')

if option == 'Logical Operators':
    st.write('### logical operators | 逻辑运算')

    st.page_link("https://www.bilibili.com/video/BV1944y1x7SW/?p=17&share_source=copy_web&vd_source=7bf7c3af03910ae8dbc83caae78ba1aa",
                label="Python逻辑运算 | 今年过节能收礼吗", icon=":material/smart_display:")
    #add image
    st.image(load_image(os.path.join(github_path, 'logical_operators_1.png')))
    st.image(load_image(os.path.join(github_path, 'logical_operators_2.png')))

if option == 'List':
    st.write('### list | 列表')

    st.page_link("https://www.bilibili.com/video/BV1944y1x7SW/?p=18&share_source=copy_web&vd_source=7bf7c3af03910ae8dbc83caae78ba1aa",
                label="Python列表 | 创一个购物清单", icon=":material/smart_display:")
    py_12 = '''
    shopping_list = []
    # 往购物清单里添加两个商品
    shopping_list.append("键盘")
    shopping_list.append("键帽")
    # 往购物清单里移除一个商品
    shopping_list.remove("键帽")
    # 往购物清单里添加两个商品
    shopping_list.append("音响")
    shopping_list.append("电竞椅")
    # 更改购物清单的第二个商品
    shopping_list[1] = "硬盘"
    
    print(shopping_list)
    print(len(shopping_list))
    print(shopping_list[0])
    
    # 定义一个价格列表
    price = [799, 1024, 200, 800]
    # 获取最高的价格
    max_price = max(price)
    # 获取最低的价格
    min_price = min(price)
    # 获取从低到高排序好的价格列表
    sorted_price = sorted(price)
    print(max_price)
    print(min_price)
    print(sorted_price)
    '''
    st.code(py_12,language='python')

if option == 'Dictionary':
    st.write('### dictionary | 字典')

    st.page_link("https://www.bilibili.com/video/BV1944y1x7SW/?p=19&share_source=copy_web&vd_source=7bf7c3af03910ae8dbc83caae78ba1aa",
                label="Python字典 | 创个秒查流行语的词典", icon=":material/smart_display:")
    py_13 = '''
    # 因为当前网页中提供的Python代码编辑器不支持用户输入功能,故采用直接赋值给变量的方法来代替用户输入 
    # 结合input、字典、if判断，做一个查询流行语含义的电子词典程序
    slang_dict = {"觉醒年代":"《觉醒年代》首次以电视剧的形式回溯中国共产党的孕育和创立过程，生动再现中国近代历史的大变局，深刻讲述中国人民是怎样选择了中国共产党。该剧播出后广受好评，成为党史学习教育的生动教材。",
                "YYDS":"“永远的神”的拼音缩写，用于表达对某人的高度敬佩和崇拜。2021年东京奥运会期间，不管是杨倩夺得首金，还是全红婵一场决赛跳出三个满分，或是“苏神”站上百米决赛跑道，全网齐喊“YYDS”，奥运期间一度刷屏。"}
    slang_dict["双减"] = "指进一步减轻义务教育阶段学生作业负担和校外培训负担。其目标是使学校教育教学质量和服务水平进一步提升，作业布置更加科学合理，学校课后服务基本满足学生需要，学生学习更好回归校园，校外培训机构培训行为全面规范。"
    slang_dict["破防"] = "原指在游戏中突破了对方的防御，使对方失去防御能力。现指因遇到一些事或看到一些信息后情感上受到很大冲击，内心深处被触动，心理防线被突破。"
    slang_dict["元宇宙"] = "源于小说《雪崩》的科幻概念，现指在XR（扩展现实）、数字孪生、区块链和AI（人工智能）等技术推动下形成的虚实相融的互联网应用和社会生活形态。现阶段，元宇宙仍是一个不断演变、不断发展的概念。Facebook（脸书）对外公布更名为“Meta”，该词即来源于“Metaverse”（元宇宙）。"
    slang_dict["绝绝子"] = "该词流行于某网络节目，节目中一些粉丝用“绝绝子”为选手加油。多用于赞美，表示“太绝了、太好了”。这个词引发了网友对网络语言的关注和讨论。"
    slang_dict["躺平"] = "该词指人在面对压力时，内心再无波澜，主动放弃，不做任何反抗。“躺平”更像是年轻人的一种解压和调整方式，是改变不了环境便改变心态的自我解脱。短暂“躺平”是为了积聚能量，更好地重新出发。"
    slang_dict["伤害性不高，侮辱性极强"] = "一段网络视频中，两名男子相互夹菜，而同桌的另一名女子则显得很孤单。于是有网友调侃“伤害性不高，侮辱性极强”。后被网友用来调侃某事虽然没有实质性危害，但是却令人很难堪。"
    slang_dict["我看不懂，但我大受震撼"] = "源自导演李安在纪录片《打扰伯格曼》（2013）里评价一部影视作品的话。现多用于表示自己对某件事情的不解、震惊。"
    slang_dict["强国有我"] = "源自建党百年天安门广场庆典上青年学子的庄严宣誓。“请党放心，强国有我”是青年一代对党和人民许下的庄重誓言，彰显着新时代中国青年的志气、骨气、底气。"
    
    # query = input("请输入您想要查询的流行语：")
    query = '躺平'
    if query in slang_dict:
        print(f"您查询的 <{query}> 含义如下")
        print(slang_dict[query])
    else:
        print("您查询的流行语暂未收录。")
        print("当前本词典收录词条数为：" + str(len(slang_dict)) + "条。")
    '''
    st.code(py_13,language='python')

if option == 'For Loop':
    st.write('### for loop | for循环')

    st.page_link("https://www.bilibili.com/video/BV1944y1x7SW/?p=20&share_source=copy_web&vd_source=7bf7c3af03910ae8dbc83caae78ba1aa",
                label="Python for循环 | 找出不正常体温", icon=":material/smart_display:")
    py_14 = '''
    total = 0 
    
    for i in range(1,101):
        total = total + i 
    print(total)
    '''
    st.code(py_14,language='python')

if option == 'While Loop':
    st.write('### while loop | while循环')

    st.page_link("https://www.bilibili.com/video/BV1944y1x7SW/?p=21&share_source=copy_web&vd_source=7bf7c3af03910ae8dbc83caae78ba1aa",
                label="Python while循环 | 捕捉日落", icon=":material/smart_display:")
    py_15 = '''
    list1 = ['你','好','吗','兄','弟']
    
    i = 0
    while i < len(list1):
        print(list1[i])
        i = i + 1
    '''
    st.code(py_15,language='python')

if option == 'String Formatting':
    st.write('### string formatting | 格式化字符串')

    st.page_link("https://www.bilibili.com/video/BV1944y1x7SW/?p=22&share_source=copy_web&vd_source=7bf7c3af03910ae8dbc83caae78ba1aa",
                label="Python 格式化字符串 | 优雅群发春节短信", icon=":material/smart_display:")
    py_16 = '''
    gpa_dict = {"小明":3.251, "小花":3.869, "小李":2.683, "小张":3.685}
    for name, gpa in gpa_dict.items():
        print('**************************************************')
        print("{0}你好, 你的当前绩点为 {1:.2f}".format(name, gpa))
        print('**************************************************')
        print(f"{name}你好, 你的当前绩点为: {gpa:.2f}")
    '''
    st.code(py_16,language='python')

if option == 'Function':
    st.write('### function | 函数')

    st.page_link("https://www.bilibili.com/video/BV1944y1x7SW/?p=23&share_source=copy_web&vd_source=7bf7c3af03910ae8dbc83caae78ba1aa",
                label="Python函数（上） | 不做代码复读机", icon=":material/smart_display:")
    py_17 = '''
    def calculate_sector(central_angle, radius):
        # 接下来是一些定义函数的代码
        sector_area = central_angle / 360 * 3.14 * radius ** 2
        print(f"圆心角为: {central_angle}度 & 半径为: {radius} 的扇形面积为: {sector_area}")
    
    calculate_sector(160,30)
    calculate_sector(60,15)
    calculate_sector(30,16)
    '''
    st.code(py_17,language='python')

    st.page_link("https://www.bilibili.com/video/BV1944y1x7SW/?p=24&share_source=copy_web&vd_source=7bf7c3af03910ae8dbc83caae78ba1aa",
                label="Python函数（下） | 不做代码复读机", icon=":material/smart_display:")
    py_18 = '''
    """
    写一个计算BMI的函数，函数名为 calculate_BMI。
    1. 可以计算任意体重和身高的BMI值
    2. 执行过程中打印一句话，"您的BMI分类为：xx"
    3. 返回计算出的BMI值
    
    BMI = 体重 / (身高 ** 2)
    
    BMI分类
    偏瘦：BMI <= 18.5
    正常：18.5 < BMI <= 25
    偏胖：25 < BMI <= 30
    肥胖：BMI > 30
    """
    
    def calculate_BMI(weight, height):
        BMI = weight / height ** 2
        if BMI <= 18.5:
            category = "偏瘦"
        elif BMI <= 25:
            category  = "正常"
        elif BMI <= 30:
            category = "偏胖"
        else:
            category = "肥胖"
        print(f"您的BMI分类为：{category}")
        return BMI
    
    result = calculate_BMI(70, 1.8)
    print(result)
    '''
    st.code(py_18,language='python')

if option == 'Importing Module':
    st.write('### importing module | 引入模块')

    st.page_link("https://www.bilibili.com/video/BV1944y1x7SW/?p=25&share_source=copy_web&vd_source=7bf7c3af03910ae8dbc83caae78ba1aa",
                label="Python引入模块 | 别人写的，拿来吧你", icon=":material/smart_display:")
    #add image
    st.image(load_image(os.path.join(github_path, 'importing_module_1.png')))
    st.image(load_image(os.path.join(github_path, 'importing_module_2.png')))

if option == 'Object-Oriented Programming':
    st.write('### object-oriented programming | 面向对象编程')

    st.page_link("https://www.bilibili.com/video/BV1944y1x7SW/?p=26&share_source=copy_web&vd_source=7bf7c3af03910ae8dbc83caae78ba1aa",
                label="8分钟搞懂面向对象编程", icon=":material/smart_display:")
    #add image
    st.image(load_image(os.path.join(github_path, 'oop_1.png')))
    st.image(load_image(os.path.join(github_path, 'oop_2.png')))

if option == 'Class':
    st.write('### class | 类')

    st.page_link("https://www.bilibili.com/video/BV1944y1x7SW/?p=27&share_source=copy_web&vd_source=7bf7c3af03910ae8dbc83caae78ba1aa",
                label="Python创建类（上）| 没对象？实例化一个", icon=":material/smart_display:")
    py_19 = '''
    class CuteCat:
        def __init__(self, cat_name, cat_age, cat_color):
            self.name = cat_name
            self.age = cat_age
            self.color = cat_color
    
    cat1 = CuteCat("Jojo", 2, "橙色")
    print(f"小猫{cat1.name}的年龄是{cat1.age}岁，花色是{cat1.color}")
    '''
    st.code(py_19,language='python')

    st.page_link("https://www.bilibili.com/video/BV1944y1x7SW/?p=28&share_source=copy_web&vd_source=7bf7c3af03910ae8dbc83caae78ba1aa",
                label="Python创建类（下）| 当上帝的时刻到了", icon=":material/smart_display:")
    py_20 = '''
    # 定义一个学生类
    # 要求：
    # 1. 属性包括学生姓名、学号，以及语数英三科的成绩
    # 2. 能够设置学生某科目的成绩
    # 3. 能够打印出该学生的所有科目成绩
    
    class Student:
        def __init__(self, name, student_id):
            self.name = name
            self.student_id = student_id
            self.grades = {"语文": 0, "数学": 0, "英语": 0}
    
        def set_grade(self, course, grade):
            if course in self.grades:
                self.grades[course] = grade
    
        def print_grades(self):
            print(f"学生{self.name} (学号：{self.student_id}) 的成绩为：")
            for course in self.grades:
                print(f"{course}: {self.grades[course]}分")
    
    chen = Student("小陈", "100618")
    chen.set_grade("语文", 92)
    chen.set_grade("数学", 94)
    chen.print_grades()
    '''
    st.code(py_20,language='python')

if option == 'Inheritance':
    st.write('### inheritance | 类继承')

    st.page_link("https://www.bilibili.com/video/BV1944y1x7SW/?p=29&share_source=copy_web&vd_source=7bf7c3af03910ae8dbc83caae78ba1aa",
                label="Python 类继承 | 老鼠的儿子会打洞", icon=":material/smart_display:")
    py_21 = '''
    # 类继承练习：人力系统
    # - 员工分为两类：全职员工 FullTimeEmployee、兼职员工 PartTimeEmployee。
    # - 全职和兼职都有"姓名 name"、"工号 id"属性，
    #   都具备"打印信息 print_info"（打印姓名、工号）方法。
    # - 全职有"月薪 monthly_salary"属性，
    #   兼职有"日薪 daily_salary"属性、"每月工作天数 work_days"的属性。
    # - 全职和兼职都有"计算月薪 calculate_monthly_pay"的方法，但具体计算过程不一样。
    
    class Employee:
        def __init__(self, name, id):
            self.name = name
            self.id = id
    
        def print_info(self):
            print(f"员工名字：{self.name}，工号：{self.id}")
    
    class FullTimeEmployee(Employee):
        def __init__(self, name, id, monthly_salary):
            super().__init__(name, id)
            self.monthly_salary = monthly_salary
    
        def calculate_monthly_pay(self):
            return self.monthly_salary
    
    class PartTimeEmployee(Employee):
        def __init__(self, name, id, daily_salary, work_days):
            super().__init__(name, id)
            self.daily_salary = daily_salary
            self.work_days = work_days
    
        def calculate_monthly_pay(self):
            return self.daily_salary * self.work_days
    
    zhangsan = FullTimeEmployee("张三", "1001", 6000)
    lisi = PartTimeEmployee("李四", "1002", 230, 15)
    zhangsan.print_info()
    lisi.print_info()
    print(zhangsan.calculate_monthly_pay())
    print(lisi.calculate_monthly_pay())
    '''
    st.code(py_21,language='python')

if option == 'File Path':
    st.write('### file path  | 文件路径')

    st.page_link("https://www.bilibili.com/video/BV1944y1x7SW/?p=30&share_source=copy_web&vd_source=7bf7c3af03910ae8dbc83caae78ba1aa",
                label="Python文件路径 | 文件在哪里，代码咋知道", icon=":material/smart_display:")
    #add image
    st.image(load_image(os.path.join(github_path, 'file_path_1.png')),caption="绝对路径")
    st.image(load_image(os.path.join(github_path, 'file_path_2.png')),caption="相对路径")

if option == 'Read File':
    st.write('### read file  | 读取文件')

    st.page_link("https://www.bilibili.com/video/BV1944y1x7SW/?p=31&share_source=copy_web&vd_source=7bf7c3af03910ae8dbc83caae78ba1aa",
                label="Python文件操作（上）| 会读文件，程序便有了眼睛", icon=":material/smart_display:")
    py_22 = '''
    import tempfile

    content = """
    ########################################
    你好，
    希望学习Python的每一秒钟都能给你带来无尽的快乐! 
    如果没有的话，那就接着学下去吧哈哈~~~
    ########################################
    """
    
    with tempfile.NamedTemporaryFile(delete=False, suffix=".txt", mode="w", encoding="utf-8") as temp_file:
        temp_file.write(content)
        temp_file_path = temp_file.name
    
    # 1. read方法读文件
    with open(temp_file_path, "r", encoding="utf-8") as f:
        content = f.read()
        print(content)
    
    # 2. readline方法读文件
    with open(temp_file_path, "r", encoding="utf-8") as f:
        line = f.readline()
        while line != "":
            print(line)
            line = f.readline()
    
    # 3. readlines方法读文件
    with open(temp_file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            print(line)
    '''
    st.code(py_22,language='python')

if option == 'Write File':
    st.write('### write file  | 写入文件')

    st.page_link("https://www.bilibili.com/video/BV1944y1x7SW/?p=32&share_source=copy_web&vd_source=7bf7c3af03910ae8dbc83caae78ba1aa",
                label="Python文件操作（下）| 会写文件，程序便有了记忆", icon=":material/smart_display:")
    py_23 = '''
    import tempfile

    # 任务1：创建一个临时文件并写入内容
    with tempfile.NamedTemporaryFile(delete=False, mode="w", encoding="utf-8", suffix=".txt") as temp_file:
        temp_file.write("""我欲乘风归去，又恐琼楼玉宇，高处不胜寒。""")
        temp_file_path = temp_file.name  # 保存临时文件的路径
    
    # 任务2：以追加模式打开文件并写入额外内容
    with open(temp_file_path, "a", encoding="utf-8") as temp_file:
        temp_file.write("""起舞弄清影，何似在人间。""")
    
    # 显示临时文件内容
    with open(temp_file_path, "r", encoding="utf-8") as temp_file:
        poem_content = temp_file.read()
        print(poem_content)
    '''
    st.code(py_23,language='python')

if option == 'Higher-order function & Lambda':
    st.write('### higher-order function & lambda  | 高阶和匿名函数')

    st.page_link("https://www.bilibili.com/video/BV1944y1x7SW/?p=36&share_source=copy_web&vd_source=7bf7c3af03910ae8dbc83caae78ba1aa",
                label="Python高阶和匿名函数 | 脱了马甲也要认识", icon=":material/smart_display:")
    py_24 = '''
    # 高阶函数
    
    def calculate_and_print(num, calculator, formatter):
        result = calculator(num)
        formatter(num, result)
    
    def print_with_vertical_bar(num, result):
        print(f"""
        | 数字参数 | {num} |
        | 计算结果 | {result} |""")
    
    def calculate_square(num):
        return num * num
    
    def calculate_cube(num):
        return num * num * num 
    
    def calculate_plus_10(num):
        return num + 10 
        
    def calculate_times_5(num):
        return num * 5
    
    calculate_and_print(3, calculate_square, print_with_vertical_bar)
    calculate_and_print(3, calculate_cube, print_with_vertical_bar)
    calculate_and_print(7, calculate_plus_10, print_with_vertical_bar)
    calculate_and_print(7, calculate_times_5, print_with_vertical_bar)
    '''
    st.code(py_24,language='python')
    py_25 = '''
    # 匿名函数 
    
    print((lambda num1, num2: num1+num2)(2, 3))
    '''
    st.code(py_25,language='python')

