class Config():
    """基础数据库配置"""
    HOST = '192.168.0.121'
    PORT = '3306'
    DATA_BASE = 'flaskShopping'
    USER = 'mysql'
    PWD = '123456'
    DB_URL = f'mysql+pymysql://{USER}:{PWD}@{HOST}:{PORT}/{DATA_BASE}?charset=utf8'

    # 对app进行SqlAlchemy配置
    SQLALCHEMY_DATABASE_URI = DB_URL
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentMode(Config):
    """开发模式下的config配置"""

    # 开启bug调试模式
    DEBUG = True

    # 解决中文乱码
    JSON_AS_ASCII = False

    # 自动加载模板
    TEMPLATES_AUTO_RELOAD = True


class ProductionModels(Config):
    """生产模式下的config配置"""

    # 解决中文乱码
    JSON_AS_ASCII = False


class TestPattern(Config):
    pass


# 设置主域名
# SERVER_NAME = 'laizhitian.com:5000'
# 持久化回话生命时间
# PERMANENT_sessionObj_LIFETIME = timedelta(hours=2)

configDict = {
    "development": DevelopmentMode,
    "production": ProductionModels,
    "test": TestPattern
}