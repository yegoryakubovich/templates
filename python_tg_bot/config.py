#
# (c) 2023, Yegor Yakubovich, yegoryakubovich.com, personal@yegoryakybovich.com
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#


from configparser import ConfigParser


config = ConfigParser()
config.read('config.ini')

config_mysql = config['mysql']
config_redis = config['redis']
config_tg = config['tg']

MYSQL_HOST = config_mysql.get('host')
MYSQL_PORT = config_mysql.getint('port')
MYSQL_USER = config_mysql.get('user')
MYSQL_PASSWORD = config_mysql.get('password')
MYSQL_NAME = config_mysql.get('name')

REDIS_HOST = config_redis.get('host')
REDIS_PORT = config_redis.getint('port')
REDIS_PASSWORD = config_redis.get('password')
REDIS_DB = config_redis.getint('db')
REDIS_PREFIX = config_redis.get('prefix')

TG_BOT_KEY = config_tg.get('bot_key')

ORDERS_COUNT = 10
