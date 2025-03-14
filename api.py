import dotenv
import vk_api
from vk_api.upload import VkUpload
import os
from photos import download_photo, delete_photo

config = dotenv.dotenv_values(".env")
TOKEN = config["TOKEN"]
GROUP_ID = config["GROUP_ID"]


def authenticate_vk():
    vk_session = vk_api.VkApi(token=TOKEN)
    vk_api_instance = vk_session.get_api()
    upload_api = VkUpload(vk_session)
    return vk_api_instance, upload_api


def publish_post(vk_instance, upload, msg, photo_path):
    download_photo(photo_path)
    photo = upload.photo_wall('photo.jpg', group_id=229289381)
    photo_id = photo[0]["id"]
    owner_id = photo[0]["owner_id"]
    attachments = 'photo{}_{}'.format(owner_id, photo_id)

    vk_instance.wall.post(
        owner_id=f"-{GROUP_ID}",
        from_group=1,
        message=msg,
        attachments=attachments,
    )
    delete_photo()
