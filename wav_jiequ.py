# 切割语音文件
import re
import os
from pydub import AudioSegment

def file_name(file_dir):
    '''
    输入文件夹名称，并返回该文件夹下所有语音文件的完整路径(list类型)
    :param file_dir:
    :return:
    '''
    L = []
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if file.split('.')[-1] == 'wav':
                L.append(os.path.join(root, file))
        return L

def cut_to_3s(src_dir,des_3s_dir,seconds_per_split_file):
    '''
    切割语音长度
    :param src_dir: 用户需要切割的某个语音文件夹
    :param des_3s_dir: 切割后文件存储文件夹
    :param seconds_per_split_file: 切割后每个语音长度
    :return:
    '''

    # 获取该文件夹下所有语音数据
    filenames = file_name(src_dir)

    # 对每一个语音数据进行切片
    for filename in filenames:

        # 获取文件名字
        print("当前切割语音文件：    ", filename)
        sound = AudioSegment.from_wav(filename)

        # 获取音频持续时间（单位为秒s）,并计算可以切割多少段？

        seconds_of_file = sound.duration_seconds
        print("该音频持续时间为：", int(seconds_of_file), "秒")


        times = int(int(seconds_of_file) / seconds_per_split_file)
        print("当前语音共可切割：  ", times, " 次")

        # # 语音切割,以毫秒为单位
        start_time = 0
        internal = seconds_per_split_file*1000
        end_time = seconds_per_split_file*1000
        name=re.split(r'[\\ .]', filename)[-2]


        for i in range(times):
            # 语音文件切割
            part = sound[start_time:end_time]
            data_split_filename=os.path.join(des_3s_dir,name + '_' + str(i) + '.wav')
            print(i)
            # 保存切割文件
            part.export(data_split_filename, format="wav")

            start_time += internal
            end_time += internal
src_dir="/home/heeler/code/project/art/data/ddd/3/"
des_3s_dir="/home/heeler/code/project/art/data/ddd1/0/"
seconds_per_split_file=0.5
cut_to_3s(src_dir,des_3s_dir,seconds_per_split_file)
