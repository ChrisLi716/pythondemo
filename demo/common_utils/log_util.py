import logging
import logging.config  # config 配置
import traceback

# 定义三种日志输出格式开始
# 其中name为getlogger指定的名字
standard_format = '[%(asctime)s][%(threadName)s:%(thread)d][task_id:%(name)s][%(filename)s:%(lineno)d]' \
                  '[%(levelname)s][%(message)s]'
simple_format = '[%(levelname)s][%(asctime)s][%(filename)s:%(lineno)d]%(message)s'
id_simple_format = '[%(levelname)s][%(asctime)s] %(message)s'

# log文件名
logfile_path_staff = r'C:\Users\Administrator\Desktop\log\routin_inspection.log'

# log配置字典
# LOGGING_DIC第一层的所有的键不能改变
LOGGING_DIC = {
    'version': 1,  # 版本号
    'disable_existing_loggers': False,  # 固定写法
    'formatters': {
        'standard': {
            'format': standard_format
        },
        'simple': {
            'format': simple_format
        },
    },
    'filters': {},
    'handlers': {
        # 打印到终端的日志
        'sh': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',  # 打印到屏幕
            'formatter': 'simple'
        },
        # 打印到文件的日志,收集info及以上的日志
        'fh': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件
            'formatter': 'standard',
            'filename': logfile_path_staff,  # 日志文件
            'maxBytes': 300,  # 日志大小 300字节
            'backupCount': 5,  # 轮转文件的个数
            'encoding': 'utf-8',  # 日志文件的编码
        },
    },
    'loggers': {
        # logging.getLogger(__name__)拿到的logger配置
        '': {
            'handlers': ['sh', 'fh'],  # 这里把上面定义的两个handler都加上，即log数据既写入文件又打印到屏幕
            'level': 'ERROR',
            'propagate': True,  # 向上（更高level的logger）传递
        }
    },
}


def md_logger():
    # 导入上面定义的logging配置 通过字典方式去配置这个日志
    logging.config.dictConfig(LOGGING_DIC)
    # 生成一个log实例  这里可以有参数 传给task_id
    logger = logging.getLogger()
    return logger
    # logger.debug('It works!')  # 记录该文件的运行状态


dic = {
    'username': '小黑'
}


def login():
    for i in range(0, 100):
        md_logger().info(f"{dic['username']}登陆成功")


try:
    login()
except Exception:
    md_logger().error("xxxxxxxxxxxxxxxxxxxx")
