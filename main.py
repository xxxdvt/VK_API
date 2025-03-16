import json
import time
import vk_api as vk
from api import authenticate_vk, publish_post
from apscheduler.schedulers.blocking import BlockingScheduler
from db import create_dataset


def run(data):
    vk_api_instance, upload_api = authenticate_vk()

    for item in data:
        post = (f"Название товара: {item['title']}\n"
                f"Цена: {item['price']}\n"
                f"Скидка: {item['discount']}%\n"
                f"Ссылка: {item['referral_link']}\n")
        image_url = item['image_url']
        publish_post(vk_api_instance, upload_api, post, image_url)
        time.sleep(10)

    print('Functions called')


def main():
    data = create_dataset()
    scheduler = BlockingScheduler()
    scheduler.add_job(run, 'interval', args=[data], minutes=1)  # 'run' is run every 1 minute
    scheduler.start()


if __name__ == "__main__":
    main()
