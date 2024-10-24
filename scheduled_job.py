import time 
import os
import django

from selenium_scripts.bot import InstagramBot
from selenium_scripts.config import username,password

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SocialBoost.settings')

django.setup()

from insta_boost.models import BotRequest
def execute_selenium_script(record: dict):
    obj = BotRequest.objects.filter(id=record['id'])[0]

    obj.status = 'progress'
    obj.save()
    
    # for following an account
    if record['request_type'] == 'follow':
        print('request type is follow..')
        bot =InstagramBot(username, password)
        print('bot object created: ', bot)
        bot.login()
        print('logged in..')
        bot.dismiss_save_login_prompt()
        bot.dismiss_notification_prompt()
        status = bot.follow_user(record['insta_profile'])

        print('got status : ', status)
        if status == True:
           print('in if')
           obj.status = 'success'
           obj.save()

        else:
            print('in else')
            obj.status = 'failed'
            obj.save()

    # for comment on a post
    elif record['request_type'] == 'comment':
        bot =InstagramBot(username, password)
        bot.login()
        #bot.dismiss_save_login_prompt()
        #bot.dismiss_notification_prompt()
        #bot.comment_on_post()
        status = bot.comment_on_post(record['post_url'])

        if status == True:
           
           obj.status = 'success'
           obj.save()

        else:
            
            obj.status = 'failed'
            obj.save()

    # for like on a post
    elif record['request_type'] == 'like':
        print("executing like")
        bot =InstagramBot(username, password)
        bot.login()
        #bot.dismiss_save_login_prompt()
        #bot.dismiss_notification_prompt()
        #bot.comment_on_post()
        status = bot.like_post(record['post_url'])
        

        if status == True:
           
           obj.status = 'success'
           obj.save()

        else:
            
            obj.status = 'failed'
            obj.save()

     

def get_in_queue_records_from_db():
    records = BotRequest.objects.filter(status='queue').values()
    return records

# def connect_to_db():
#     pass

if __name__ == '__main__':
    while True:
        time.sleep(5)
        records = get_in_queue_records_from_db()
        if not records:
            print('No new records found!')
        else:
            for record in records:
                print(record)
                execute_selenium_script(record=record)
