# Scrapy settings for wangxiao project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'wangxiao'

SPIDER_MODULES = ['wangxiao.spiders']
NEWSPIDER_MODULE = 'wangxiao.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False
LOG_LEVEL = 'WARNING'

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en',
    'Cookie': 'autoLogin=true; UserCookieName=pc_402655544; OldUsername2=FV8k4TzONh86wTsI6hPgRA%3D%3D; OldUsername=FV8k4TzONh86wTsI6hPgRA%3D%3D; OldPassword=A2jOQgQVAQuSxIxgCqwGuA%3D%3D; UserCookieName_=pc_402655544; OldUsername2_=FV8k4TzONh86wTsI6hPgRA%3D%3D; OldUsername_=FV8k4TzONh86wTsI6hPgRA%3D%3D; OldPassword_=A2jOQgQVAQuSxIxgCqwGuA%3D%3D; pc_402655544_exam=fangchan; wxLoginUrl=http%3A%2F%2Fks.wangxiao.cn%2Fexampoint%2Flist%3Fsign%3Dcfe2; userInfo=%7B%22userName%22%3A%22pc_402655544%22%2C%22token%22%3A%227ed95763-b277-4f6d-bc2f-83c1c431ae92%22%2C%22headImg%22%3Anull%2C%22nickName%22%3A%22136****2109%22%2C%22sign%22%3A%22fangchan%22%2C%22isBindingMobile%22%3A%221%22%2C%22isSubPa%22%3A%220%22%2C%22userNameCookies%22%3A%22FV8k4TzONh86wTsI6hPgRA%3D%3D%22%2C%22passwordCookies%22%3A%22A2jOQgQVAQuSxIxgCqwGuA%3D%3D%22%7D; token=7ed95763-b277-4f6d-bc2f-83c1c431ae92'
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'wangxiao.middlewares.WangxiaoSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'wangxiao.middlewares.WangxiaoDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'wangxiao.pipelines.WangxiaoImagesPipeline': 300,
    'wangxiao.pipelines.WangxiaoPipeline': 301,
}
IMAGES_STORE = '../../00_素材箱/中大网校'

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

REQUEST_FINGERPRINTER_IMPLEMENTATION = '2.7'
