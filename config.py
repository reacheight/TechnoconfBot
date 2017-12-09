import os

token = os.environ['BOT_TOKEN']

about_text_file = 'data/about_data/about_text_message'
help_text_file = 'data/help_data/help_text_message'
bl_text_file = 'data/bl_data/bl_text_messages'
bl_images_locations = 'data/bl_data/images/'
deer_messages_location = 'data/deer_data/messages'
math_test_file = 'data/tests/math'
test_files = {'math' : 'data/tests/math',
              'rus' : 'data/tests/rus',
              'phys' : 'data/tests/phys',
              'inf' : 'data/tests/inf'}

wolfram_appid = os.environ['WOLFRAM_APPID']
wolfram_bad_status_message = "Запрос не найдён.\nЕсли ты ввёл его на русском, то попробуй ввести его на английском."
wolfram_empty_query_message = "Использование: `/wolfram <запрос>` или `/wf <запрос>`"

tts_empty_query_message = "Использование: `/voice <запрос>` или `/tts <запрос>`"

my_id = os.environ['MY_ID']

kek_message = "Вы ботом ошиблись.."

cho_pacani_anime_sticker = 'CAADAgADJwADtIuIDaIy4m-uZXREAg'
chto_pacani_pattern = r'(?iu).*чт?[оеё],? п[ао][цс][ао]ны'
