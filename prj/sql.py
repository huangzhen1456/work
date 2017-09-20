from sqlalchemy import create_engine  # 导入创建连接驱动
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from prj.settings import sql_address


engine = create_engine(sql_address, echo=False)  # 这个url可以用urlparse解析, 其中echo=True表示执行时显示sql语句
Base = declarative_base()  # 生成了declarative基类, 以后的model继承此类


SQL = sessionmaker(bind=engine)  # 创建一个Session类
#sql = Session()  # 生成一个Session实例,即一个会话链接
