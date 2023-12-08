from mastodon import Mastodon, StreamListener
import datetime
from dateutil.tz import tzutc 
import json
file_name = "very_secret_file.secret"

# %% DO NO RUN AGAIN
file_name = "very_secret_file.secret"

Mastodon.create_app("social-web-analytics",
api_base_url="https://mastodon.social",
to_file= file_name
)

# %% Run from here

# Substitute the name of the credentials file.
mastodon = Mastodon(
client_id = file_name
)

mastodon.log_in("arnobchaudhury@gmail.com", "6L9C%EaY,tD5?&^",
to_file=file_name
)

#%% Helpers
class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)
# Test
status = {'id': 111483021681561544, 'created_at': datetime.datetime(2023, 11, 27, 14, 38, 31, 890000, tzinfo=tzutc()), 'in_reply_to_id': None, 'in_reply_to_account_id': None, 'sensitive': False, 'spoiler_text': '', 'visibility': 'public', 'language': 'en', 'uri': 'https://mastodon.social/users/fiestasubaru/statuses/111483021681561544', 'url': 'https://mastodon.social/@fiestasubaru/111483021681561544', 'replies_count': 0, 'reblogs_count': 0, 'favourites_count': 0, 'edited_at': None, 'content': '<p>Looking at the Future of the 2024 Subaru vehicles in Albuquerque NM</p><p>Look for seven new 2024 Subaru vehicles in Albuquerque NM. Subaru is committed to making sure all your adventures are safe and comfortable. We deliver quality, comfort, and advanced performance in all our vehicles.</p><p><a href="https://fiestasubaru.com/looking-at-the-future-of-the-2024-subaru-vehicles-in-albuquerque-nm" target="_blank" rel="nofollow noopener noreferrer" translate="no"><span class="invisible">https://</span><span class="ellipsis">fiestasubaru.com/looking-at-th</span><span class="invisible">e-future-of-the-2024-subaru-vehicles-in-albuquerque-nm</span></a></p>', 'reblog': None, 'application': {'name': 'Web', 'website': None}, 'account': {'id': 109359409179069329, 'username': 'fiestasubaru', 'acct': 'fiestasubaru', 'display_name': 'Fiesta Subaru', 'locked': False, 'bot': False, 'discoverable': False, 'group': False, 'created_at': datetime.datetime(2022, 11, 17, 0, 0, tzinfo=tzutc()), 'note': '<p>Trusted Subaru dealership in Albuquerque, NM</p>', 'url': 'https://mastodon.social/@fiestasubaru', 'uri': 'https://mastodon.social/users/fiestasubaru', 'avatar': 'https://files.mastodon.social/accounts/avatars/109/359/409/179/069/329/original/1618af2eccd18860.png', 'avatar_static': 'https://files.mastodon.social/accounts/avatars/109/359/409/179/069/329/original/1618af2eccd18860.png', 'header': 'https://mastodon.social/headers/original/missing.png', 'header_static': 'https://mastodon.social/headers/original/missing.png', 'followers_count': 1, 'following_count': 0, 'statuses_count': 111, 'last_status_at': datetime.datetime(2023, 11, 27, 0, 0), 'noindex': False, 'emojis': [], 'roles': [], 'fields': []}, 'media_attachments': [{'id': 111483017173542817, 'type': 'image', 'url': 'https://files.mastodon.social/media_attachments/files/111/483/017/173/542/817/original/1ba2884c8dd36d03.png', 'preview_url': 'https://files.mastodon.social/media_attachments/files/111/483/017/173/542/817/small/1ba2884c8dd36d03.png', 'remote_url': None, 'preview_remote_url': None, 'text_url': None, 'meta': {'original': {'width': 620, 'height': 323, 'size': '620x323', 'aspect': 1.9195046439628483}, 'small': {'width': 620, 'height': 323, 'size': '620x323', 'aspect': 1.9195046439628483}}, 'description': None, 'blurhash': 'UyFPjQn$RjWW?doeWCayxuogjuaxaxofaxjZ'}], 'mentions': [], 'tags': [], 'emojis': [], 'card': None, 'poll': None, 'filtered': []}
with open('output_test.json', 'a', encoding='utf-8') as output_file:
     json.dump(str(status), output_file, ensure_ascii=False, cls=DateTimeEncoder)
     output_file.write('\n')  # Add a newline between JSON objectsx

def check_words_in_paragraph(paragraph):
    words_to_check = ['israel, palestine', 'hamas', 'gaza', 'israel-palestine conflict']

    # Convert to lowercase for case-insensitive comparison
    paragraph_lower = paragraph.lower()

    for word in words_to_check:
        if word in paragraph_lower:
            return True

    return False
# %%
class StdOutListener(StreamListener):
    def on_update(self, status):
        print(status.content)
        # Process the status update
        with open('output_ISREAL.json', 'a', encoding='utf-8') as output_file:
            # Save the JSON data to the file
            if(check_words_in_paragraph(status.content) == True):    
                json.dump(str(status), output_file, ensure_ascii=False, cls=DateTimeEncoder)
                output_file.write('\n')  # Add a newline between JSON objectsx
        return True
    def on_abort(self, err):
        print(err)
l = StdOutListener()
mastodon.stream_public(listener=l, timeout=7210)
