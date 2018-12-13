import configparser
import os


class GetConfig:
    '''
    读取配置文件
    '''
    def __init__(self):
        self.cf = configparser.ConfigParser()
        self.cfpath = os.path.dirname(os.path.abspath('.'))+'\\config\\config.ini'
        self.cf.read(self.cfpath)

    def get_message(self, name):
        config_message = self.cf.get('browser', name)
        return config_message

if __name__=='__main__':
    print(GetConfig().get_message('Url'))
