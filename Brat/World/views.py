from django.shortcuts import render,HttpResponse
import os.path,sys,glob,json,re
from .models import Label,Entity,RelationShip,Label_RelationShip
from django.utils.encoding import smart_str


# Create your views here.

def muban(request):
    q = request.get_full_path_info()
    return render(request,'muban.html',{'path':q})


# def mengban(request):
#     path = os.path.abspath('static/document')
#     print('path', path)
#     aa = os.access(path,os.F_OK)
#     list = []
#     if os.path.exists(path):  # 判断路径是否存在
#         zi_path = os.listdir(path)  # 获取该目录下的所有文件或文件夹目录
#         for c in zi_path:
#             d = os.path.join(path, c)  # 得到该文件下所有目录的路径
#             if os.path.isdir(d):  # 判断该路径下是否是文件夹
#                 youxiao_path = os.path.split(d)
#                 list.append(youxiao_path[1] + '/')
#     print('list', list)
#     context = {'document':list}
#     # if request.method == 'POST':
#     #     pat = request.POST['pat']
#     #     path = os.path.abspath('static/document/'+pat)
#     #     list = []
#     #     if os.path.exists(path):  # 判断路径是否存在
#     #         zi_path = os.listdir(path)  # 获取该目录下的所有文件或文件夹目录
#     #         for c in zi_path:
#     #             d = os.path.join(path, c)  # 得到该文件下所有目录的路径
#     #             if os.path.isdir(d):  # 判断该路径下是否是文件夹
#     #                 youxiao_path = os.path.split(d)
#     #                 list.append(youxiao_path[1] + '/')
#     #     print('list', list)
#     #     context = list
#     #     return HttpResponse(context)
#     # else:
#     return render(request,'demo.html',context)
#
#
# def document_path(path):
#     list = []
#     if os.path.exists(path):  # 判断路径是否存在
#         zi_path = os.listdir(path)  # 获取该目录下的所有文件或文件夹目录
#         for c in zi_path:
#             d = os.path.join(path, c)  # 得到该文件下所有目录的路径
#             if os.path.isdir(d):  # 判断该路径下是否是文件夹
#                 youxiao_path = os.path.split(d)
#                 list.append(youxiao_path[1] + '/')
#     print('list', list)
#     return list
#
# def mengban_one(request):
#     path = os.path.abspath('static/document')
#     aaa = request.POST['pat']
#     # inf = request.get_full_path_info()
#     # a = inf.split('/', -1)
#     # one_path = inf.split('/',-1)[-2]
#     # path = os.path.abspath(path+'/'+one_path)
#     path = os.path.abspath(path+'/'+aaa)
#     # aaaa = os.access(abc, os.F_OK)
#     aa = os.access(path, os.F_OK)
#     lister = document_path(path)
#     # list = []
#     # if os.path.exists(path):  # 判断路径是否存在
#     #     zi_path = os.listdir(path)  # 获取该目录下的所有文件或文件夹目录
#     #     for c in zi_path:
#     #         d = os.path.join(path, c)  # 得到该文件下所有目录的路径
#     #         if os.path.isdir(d):  # 判断该路径下是否是文件夹
#     #             youxiao_path = os.path.split(d)
#     #             list.append(youxiao_path[1] + '/')
#     # print('list', list)
#     return render(request,'document_one.html',{'list':lister})
#
#
# def mengban_two(request):
#
#     return render(request,'demo.html')


def page(request):
    q = request.get_full_path_info()
    calg = request.path.split('.html/')[1]
    # mm = request.path.split('/')[-2]
    # aa = os.path.basename(calg)

    # pa = request.path.split('/')[-2]
    # pb = request.path.split('/')[-3]
    # pp = pb+'/'+pa
    # po = os.path.abspath(pp)
    # oo = calg[8:]
    gg = ('static/document/'+calg)[:-1]
    # bb,bc = os.path.splitext(pa)
    txt = []
    # aaaaa = gg.endswith('.txt')
    if gg.endswith('.txt'):  #显示带有文件扩展名的文件名

        # bbb = os.path.split(gg)
        # files = []
        # ccc = os.path.dirname(gg)
        for fa in os.walk(os.path.dirname(gg)):
            for ddd in fa:
                pass
            # print('ddd',ddd)
            # files = ddd
        with open(gg,"r",encoding='utf-8') as f:
            line = f.readline()
            # line = line.strip('\n')
            while line:
                txt.append(line)
                line = f.readline()
                # liner = line.strip('\n')
                # txt.append(liner)

                # print(line)
        # while '' in txt:
        #     txt.remove()
        # h = render(request, 'read.html', {'line': txt, 'path': q})
        entiey_list = Entity.objects.all()
        # entiey_str = ''
        # for i in entiey_list:
        #     ts = i.entity_name + '1' + str(i.entity_label) + '3'
        #     entiey_str = entiey_str + ts
        # print(entiey_str)
        lr_list = Label_RelationShip.objects.all()
        # lr_str = ''
        # for j in lr_list:
        #     rl = str(j.lr_labelA) + '1' + str(j.lr_labelB) + '2' + str(j.lr_relationship) + '3'
        #     lr_str = lr_str + rl
        # print(lr_str)
        #
        # # ss = '????abcsa撒'
        # # ss.encode('iso-8859-1')
        # # ss.decode('UTF-8','strict').encode('iso-8859-1')
        # # ss.encode('UTF-8').decode('UTF-8','strict').encode('iso-8859-1')
        # # h.set_cookie('shiti', bytes(ss, 'utf-8').decode('ISO-8859-1'))
        # h.set_cookie('shiti',bytes(entiey_str, 'utf-8').decode('ISO-8859-1'))
        # # h.set_cookie('one', '11111', 14 * 24 * 3600 * 1000)
        # h.set_cookie('lr',bytes(lr_str, 'utf-8').decode('ISO-8859-1'))
        # ada = request.COOKIES
        # print(ada)
        # return h
        context = {
            'line': txt,
            'path': q,
            'entiey_list':entiey_list,
            'lr_list':lr_list,
            'filesd':ddd
        }
        return render(request, 'read.html',context)




        # return render(request,'read.html',{'line':txt,'path':q})
    else:
        catalog = os.listdir('./static/document/'+calg)  # 获取该目录下的所有文件或文件夹目录
        file=[]
        fils = []
        for i in catalog:  #re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None
            if re.match(r'^\.+', i, re.M|re.I):  #re.M:多行匹配，影响 ^ 和 $    re.I:使匹配对大小写不敏感
                catalog.remove(i)
            elif os.path.isfile('./static/document/'+calg+i):  #判断文件是否存在
                # catalog.remove(i)
                file.append(i)
            else:
                fils.append(i)
        if calg:
            fils.insert(0,'..')  #将指定对象(../文件夹)插入到列表中的指定位置
        return render(request,'mengban.html',{'info':calg,'catalog':fils,'files':file})


def Cancel(request):

    return render(request,'cancel.html')


