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


from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.redis import RedisStorage2
from aiogram.utils import executor

from app.aiogram.form import Form
from app.aiogram.handlers.start import handler_start
from config import TG_BOT_KEY, REDIS_HOST, REDIS_PORT, REDIS_PASSWORD, REDIS_DB, REDIS_PREFIX


bot = Bot(
    token=TG_BOT_KEY,
)
storage = RedisStorage2(
    host=REDIS_HOST,
    port=REDIS_PORT,
    password=REDIS_PASSWORD,
    db=REDIS_DB,
    pool_size=10,
    prefix=REDIS_PREFIX,
)
dp = Dispatcher(bot, storage=storage)
HANDLERS = [
    {'handler': handler_start, 'state': None, 'content_types': ['text']},
]


def handlers_create():
    [dp.register_message_handler(h['handler'], state=h['state'], content_types=h['content_types']) for h in HANDLERS]


def bot_create():
    handlers_create()
    executor.start_polling(dp)
