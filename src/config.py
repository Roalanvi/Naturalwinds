class Config:
    SECRET_KEY = 'B!1w8NAt1T^%kvhUI*S^'
class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_HOST = 'https://auth-db957.hstgr.io/index.php?route=/database/structure&server=1&db=u905391073_root'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'Citron1234'
    MYSQL_DB = 'u905391073_root'
config = {
    'development': DevelopmentConfig
}