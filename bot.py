import telebot
import requests
from bs4 import BeautifulSoup
from time import sleep
from app.analyzer import analyze, Keywords
from app.client import *
from app.check import isBanned, ban

SERVER_NAME = '---'
SERVER_ID = 0
isGlobal = False
bot = telebot.AsyncTeleBot('---')
SEARCH_URL = 'https://mp3legenda.com/?q='
Admins = [395809791, 288371758, 492633325, 415434846, 390512841, -1001453719673]
Block_Author = ['']
headers = {
    'Encoding': 'gzip, deflate, br',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    'Content-Length': '9576',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Host': 'mp3legenda.com',
    'Origin': 'https://mp3legenda.com',
    'Referer': '',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}
data = {
    'id': '', 
    'ids': '',
    'allhashes': '220596592_427874987&&655&&275881996952b41a62_a58bbd48896e4310ef_6d85f0aa54a707dd01_,-18113215_167437275&&0&&94a9357020b52fefab_b9d2aa84436029c402_6c85c8558809b20aa4_,149211566_456240058&&655&&7bdb66dcdb19408edf_9cb475d60bfb44a79d_60a6719e4ca3c415fd_,135975305_103505057&&655&&e6dd091ad4b5332be2_acf0c230ae4a006ca3_e762e212ccf27a954a_,2950952_225982597&&655&&f3e0a3ec07e3a0e359_e3ace5ceb0930705a9_f720221f31bff9755f_,393485601_456239032&&655&&8b5fd0e5ce82f53c23_e4fe724a8e48c8c116_cbd4d9414cb7cab4d3_,219131970_301426106&&655&&91665c0ec19cb885c2_6ae8d2d87ed47e8e26_5e34b6374d1dcc3178_,105824804_199171319&&655&&3fea680fc053d0a824_3ad5a71f780b990ad7_e625763d7011ca1fe2_,140667320_456240744&&655&&a0cb3f5b41494a6d7e_90bbc1306669bd323f_b82dcd12cbdb9b414b_,235335579_392603051&&655&&36ddd40825d064ae79_7a4a3a9b19d233f0b3_9e26c95b828d0cd1c2_,12501233_245001763&&655&&0a8df9beeed2b0d2b7_1c932a2272f19b2989_1b53b814d01308de51_,301575331_364535105&&655&&a63adda1facc10a7b1_17b199af3a09c75656_0fa08bd73457199680_,104145733_144027040&&655&&ce689f755b34b2441a_dd0f9ab1ebe23069b2_93b5b17ceb053fe3e7_,30633450_75944425&&0&&ad479525659431ffdd_6fd756ad400587edce_4397745f47c893dd81_,94388256_90158741&&655&&2dcf8083afde993d3b_fc5b0b8fe1d2abf3c9_a480ff769d2237061d_,4442694_456239120&&655&&533ccc4d0693572798_aed6592ff504753f53_bce63f7ad32d2c2321_,72230453_73097313&&655&&e429bd736bfc4c9538_d9e877a4863823eece_d4c22242c3b8023651_,137609755_124628455&&655&&2b90e247de12f68ed0_e5aac8f47c869ede06_db016ea40a309357b3_,10904543_424243153&&655&&477be3b503ce9b287d_97fd3a862677251dd1_79d7080d0b70f7aefb_,2000007372_248641966&&655&&f250848d23f2d9b115_78705d5fac6fef13fe_657ce99eaca871f3a1_,2773135_65871771&&655&&146b177771a3baa908_15c074b417ac3bc87b_5b82b0ddeddbc0fbe5_,144258422_456239076&&655&&a7a95913734aab77e7_06380635eb9a03e13b_870244188ae9b43330_,213354226_223143794&&655&&60e06e44dab621eace_c5cd90a626d8be3f8b_fff46185c52729db0f_,221621831_226754107&&655&&54afd411df11d324da_f71bf871325972ffd8_4603a0850b6a85f2c2_,136862525_456239071&&655&&2932e2ecd2bf0912cc_7da61f47b31f30adaf_612e3423f6469e5cb5_,239062342_254257832&&655&&310906e21185183df7_de6b39a5070b916c14_032f992de81a46f54e_,206031837_423396151&&655&&c8a43971ebde969136_efa113c279bd6699fc_377f53dbd55db1ad1b_,155096967_363144074&&655&&15bd75046bb7b38a00_467327b90b74ffbf19_505452a6354c4679df_,30570493_57755126&&655&&b784050233b9a90071_174ef31c88b8b16865_257d07769c3ee3de0a_,85885438_78016597&&655&&478bd6f0053c8e84d4_41cd97a8192aff8102_df17fceb6f91a598d6_,123703611_93815239&&655&&0e84bf9f931c27f260_64939abe10e3e89109_d455dbca41aa62ca3a_,2803100_456239189&&655&&c04e72f5bca197b7a7_cc515f9ae37d966f97_7da4a49bc02c9fab72_,104382716_89474880&&655&&a67911c412d2f410eb_b685e87d2b5b7b7f9a_1a8b2f151cd45488b9_,145240389_207024640&&655&&845ed2a0683843a681_c9387f28d903753151_0395a599d4fdf785e1_,50161976_88982102&&655&&ea54ab20a263683029_13b3c732201f10d0ef_218001d09fbcbe79d8_,103501724_243813199&&655&&00228eb13fb7a7426a_ce2b61b9dc7557e3ce_61a7fdb36a0c6a067e_,232478949_284341610&&655&&5039b2437db1ba1fbc_87b9898285542b06c0_3d69ae4d71766f7ae2_,462314418_456239730&&655&&defe1c14353d22344e_700a79d26ab5240281_52c639d5e125200e8a_,7975381_184747083&&655&&eebada707a7caac158_f3b985905a842a1c30_346472a1f493bb8212_,1865381_69835495&&655&&2c687b182acfeb3611_46a922e2ba94fc8429_847fb1b46fbfb40fa0_,108996236_98761097&&655&&17a9c96f0374ad717b_6f372f4dfea587ffd8_616d011d9ae1944cb2_,234953935_421259144&&655&&ba86163d60e06018b5_0dd63006670967b8ba_2a62cf330186232563_,2000273760_399779314&&655&&36a2b2e880099f51d5_9881384d41f56a1d24_c9bdb2096496157b99_,136695378_456239074&&655&&f021411d2f72e72a4d_93ceb7e2fac9ce74c7_85213146bafe46274b_,133163668_456239053&&0&&_691bdfaf2edb5b41e2_,2000457823_297955790&&0&&2f3274f3d45f89b95f_3a545036ff71cffb0b_5d1dd1c4a69c288376_,2000486458_456240064&&655&&bca2522b95fcc6d47e_f9cb7f796e10ff64eb_765e438b394c8c5d3d_,2000087008_456240716&&0&&5c91c4cb231a607fb3_0f174547336f72978d_144b3c07eb0b7ce6b1_,7504983_162911990&&655&&e3edc8760d257eee99_24566f30d328c8edd0_9bfa7503493e6050cf_,150760093_419210641&&655&&61e7072d9185669ca4_4245d1abcccf394ecd_b4c6b537e96e6f6faf_,13557018_131001048&&0&&7204cdff0931105291_9b4998737e741c5e56_0d89151da2b22333d4_,1237058_63857630&&655&&11214c1e06d387d6e6_5bd48a34cc89018ed4_1b9e8ed70e730f0b34_,38733189_410949492&&655&&3ee6c84c3a120e9223_5c89cb78818bf59b04_49d8a61f7991575ff1_,114121361_456239379&&655&&615d6c9a088178bfdb_1e09d9686d98c407dd_91b4c21e79a6978bb7_,26657391_456240211&&655&&477734f290152ddeda_b1ed07117524a5ae6a_73fb22d701c0d8c208_,2000094939_260557868&&655&&cdeccbc0d35feae825_06f8991067b49d014a_11e6a62a9db14d236e_,2000040741_307590454&&655&&33192650d5eccff8ca_a87f6d8d41d3d6e33f_668793eb4d248f55ab_,-72545153_456239098&&655&&5594d8a964e0112645_1d2d5fdf6c83dd58cf_eba9af39dbb63bf29e_,124782462_384390020&&655&&0662a83ed01bb89b70_e4c23480c95a70d9ca_9fc6c14fe7e2772448_,345290548_456239253&&655&&c7147a570aa6edc80a_fbf090d5e632f20e80_4f341704e4d60c5bcb_,131755930_349230351&&655&&a8e8c0e2540ad6f760_b2ed0f8a2ca3aa84ad_55a6616b4fb10237b9_,139260938_383895894&&655&&157eaf2ca195dc1d26_d28fa3cd2ce197e334_03c0f509203e4296f1_,124782462_384385205&&655&&661f3c99b2bf95aab7_6750c653b9beefef47_ce7818382d07a99870_,80755653_456239062&&0&&3da0400b7962c34036_ec14d07c2008b2a433_d9faa8a7e156a15034_,20230253_397605874&&0&&b3f4bfebeab9daa126_dd2b5f8521c6ffa2f9_a2b760e2f83e36c401_,4169718_71550097&&0&&82e0692f7108cc06b8_e83681bb52bd726549_9d326e1f882662b0dc_,226354209_266279136&&655&&4437867d8835ff11e2_960d437851bb78eb6a_3f70f9cd8c7a79c9b9_,58471756_456239257&&655&&f3cd08a15a5f9f0cae_93350be13dada47feb_2b2393245a6dd3f135_,164034111_456239052&&655&&f085e4b9e83392ef1e_7a1e5aa04e65591c98_08094c2b91f6f8747f_,124782462_384390906&&655&&dfe60c1a3e198075ca_3347624c07734c57ec_75803c55e3b2f09085_,2000230489_272995528&&655&&c1fcf9ed7033791014_af1b8cb841e6e58c1e_de415b1e878c6e43ae_,186799519_190396540&&0&&03cb9cb7758bf6baaf_dac75a1531e5ab5b54_61c49211e5d97737de_,135958166_244699629&&655&&c45976a768c3428348_2f0f223ae24ed52778_bca5273f2ded2baa77_,11545184_426990640&&655&&6509bf7a0d58c9993f_6afee1722a6c191c79_abd24e864b8d657916_,20230253_397605890&&0&&4f4bd5ce70390b8108_3791da8e7b0d8e1e78_9a4f91d55aaf40a24a_,15340483_456239107&&0&&7b26237c2e2fe1007d_a896ff9821752b4577_95aed532f30881b9f9_,300944358_456239035&&655&&369d4b195514a43272_a3ac3f0d86fbe94b81_864666e18017ccb8ec_,-31899344_125111756&&655&&8a95717135131063c2_de94496242999bbe94_180e7a372cc2bc5d02_,202632102_193190236&&655&&3d082a3cabf268556a_98f871ae81c245a18b_fc3615156eaca0afe2_,131755930_436982403&&655&&4ed303ffaa2c15e028_7e51f0aeda99502b6e_e5866a2e751abe038a_,-178052569_456239103&&655&&8e676fd737b4ca1562_736b32fe0a1c345fc3_130ffbd4f5aae97c24_,126657490_96128576&&655&&71ba11a4679b040672_16002edf8ae24e2c74_42fdc4881665919b07_,202739971_456239108&&655&&4ac4aa518d4ab18c89_10c18f5701ab539875_c9a95ce0fa0b1ba433_,133163668_456239052&&0&&f06eccf794f4e52d27_2e624a593819dade63_f94f6698ac6eadff26_,141590975_284404053&&655&&8dae9c7b1e7a5f6bb5_ce1e5b13ed35f5194c_6ab60c93fd0f620577_,89570828_215263460&&655&&5d7d14cd4fcdd44c6d_7780e42c6ca2c3f961_f412f724153a1e43e8_,371969386_456239021&&655&&3827d84d8efb699eaf_3d97d0e2b61e58eae9_58ba193c2806bdc2c4_,131755930_422673098&&655&&559fafe8c91c01e2c1_4cb8bc891be99f0160_94ad2fa69aeaee89ba_,43440407_456239187&&655&&917ae60c34677efd05_b5cad637ae05398737_0414cb90f63d531948_,444180064_456239047&&655&&324417935ef6665339_9af7caffc5a88b1e43_8d718d1d4031654ec2_,142527819_118834774&&655&&4dea0a460a4e53897a_6b9778999c302357ec_fbc46b8997e414edbe_,9251761_456239999&&655&&bf232ce3484bb0d752_1d69ac3787e06e3abe_d9c50bbe3153d47ccd_,2000499593_301276690&&0&&6e8c93eb2876a7f21d_b28c26a2ddddd627f2_667fda4fbde05719c1_,202739971_241662828&&655&&9612f82a910dfba338_e9caad5a37951fb6b1_1fdd935096e19bbf33_,210539285_456239120&&655&&a156f83bbc8793d18f_74c022f1d6a9c7b68e_020020f2feb5a8a247_,23859285_58244002&&655&&4aafdfdd180424d942_66b26b6111771a15d8_c8ba3a0746fc947642_,402242_97503748&&655&&ccd38c9cf07ffd74f1_23f8e347a9ee49a2fb_45296821ef4b921a19_,2000346455_456240515&&655&&37ef4655ac8ce3bc4b_d15f0dc45406f11554_374566c34d318534e7_,269693149_456239025&&655&&79e1f7ac00be60964a_e105c16a86d421d97c_18bba78f75f9f83a7a_,5463792_456239177&&655&&b55ee9027dd5410489_231b12f003f16b5edb_3166518bc3750c1247_',
    'ua': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36',
    'li_artist': '',
    'li_song': ''
}


@bot.message_handler(commands=['start'])
def start_message(message):
    print('start from', message.chat.id)
    bot.send_message(message.chat.id, 'Отправьте мне автора и полное название трека. Например: {/set Ну, чтобы без "курить"}')
    sleep(0.1)


@bot.message_handler(commands=['skip'])
def stop_function(message):
    if message.chat.id in Admins:
        print('skip from', message.chat.id)
        client = Client(SERVER_NAME, SERVER_ID)
        client.send_text('skip')
        bot.send_message(message.chat.id, 'Пропускаю трэк, Сэр ' + message.from_user.first_name + ' ' + message.from_user.last_name)
    sleep(0.1)


@bot.message_handler(commands=['ban'])
def stop_function(message):
    if message.chat.id in Admins:
        bot.send_message(message.chat.id, 'Добавил ключ-слово, Сэр ' + message.from_user.first_name + ' ' + message.from_user.last_name)
        Keywords.append(message.text[5:])
    sleep(0.1)


@bot.message_handler(commands=['show_ban'])
def show_ban_function(message):
    if message.chat.id in Admins:
        result = ''
        for key in Keywords:
            result += key + '\n'
        bot.send_message(message.chat.id, result)
    sleep(0.1)


@bot.message_handler(commands=['renew'])
def renew_function(message):
    if message.chat.id in Admins:
        client = Client(SERVER_NAME, SERVER_ID)
        client.send_text('start_play')
        bot.send_message(message.chat.id, 'Включаю колонку, Сэр ' + message.from_user.first_name + ' ' + message.from_user.last_name)
    sleep(0.1)


@bot.message_handler(commands=['stop'])
def stop_function(message):
    if message.chat.id in Admins:
        client = Client(SERVER_NAME, SERVER_ID)
        client.send_text('stop_play')
        bot.send_message(message.chat.id, 'Выключаю колонку, Сэр ' + message.from_user.first_name + ' ' + message.from_user.last_name)
    sleep(0.1)


@bot.message_handler(commands=['clear'])
def order_function(message):
    if message.chat.id in Admins:
        client = Client(SERVER_NAME, SERVER_ID)
        client.send_text('clearStack')
        bot.send_message(message.chat.id, 'Стэк чист, Сэр ' + message.from_user.first_name + ' ' + message.from_user.last_name)
    sleep(0.1)


@bot.message_handler(commands=['order'])
def clear_function(message):
    client = Client(SERVER_NAME, SERVER_ID)
    Array = list(map(str, client.send_stac_req('getStack')[1:][:-1].split("/*/ ")))
    result = ''
    if Array[0] == '' and len(Array) == 1:
        bot.send_message(message.chat.id, 'Песни еще не заказаны)')
        sleep(0.1)
        return
    for i in range(len(Array)):
        if message.chat.id in Admins:
            result += str(i+1)+') ' + list(map(str, Array[i].split('^')))[0] + ' - ' + list(map(str, Array[i].split('^')))[1] + '\n'
        else:
            result += str(i+1)+') ' + list(map(str, Array[i].split('^')))[0] + '\n'
    bot.send_message(message.chat.id, result)
    sleep(0.1)


@bot.message_handler(commands=['set'])
def handle_message(message):
    client = Client(SERVER_NAME, SERVER_ID)
    Array = client.send_stac_req('getStack')
    Music = list(map(str, Array[1:][:-1].split("/*/ ")))
    if str(message.chat.id) in Array and message.chat.id not in Admins:
        bot.send_message(message.chat.id, 'Ваш трэк уже стоит в очереди.')
        sleep(0.1)
        return
    if len(Music)>=29:
        bot.send_message(message.chat.id, 'Слишком много музыки в очереди попробуйте позже.')
        sleep(0.1)
        return
    message.text = message.text[5:]
    Words = message.text.split()
    request = (SEARCH_URL + '+'.join(Words)).lower()
    page = requests.get(request)
    if page.status_code == 200:
        soup = BeautifulSoup(page.text, 'html.parser')
        lyrics = soup.find('div', class_='lyrics')
        if lyrics == None:
            bot.send_message(message.chat.id, 'Извините, трек временно недоступен... Попробуйте другой.')
            sleep(0.1)
            return
        if message.chat.id not in Admins:
            if not analyze(lyrics.text):
                bot.send_message(message.chat.id, 'Трек не прошел цензуру... Попробуйте другой.')
                sleep(0.1)
                return
        info = soup.find('ul', class_='info')
        name = info.find_all('li')[0].text[6:]
        title = info.find_all('li')[1].text[22:]
        if (title+' '+name) in Array:
            bot.send_message(message.chat.id, 'Песня уже добавлена в список) Чтобы проверить список песен пропишите /order.')
            sleep(0.1)
            return
        headers['Referer'] = request.encode('utf-8')
        data['li_song'] = title.encode('utf-8')
        data['li_artist'] = name.encode('utf-8')
        r = requests.post('https://mp3legenda.com/play.php', headers=headers, data=data)
        if r.text == '':
            bot.send_message(message.chat.id, 'Я не нашел текст этого трека, попробуйте позже.')
        else:
            client = Client(SERVER_NAME, SERVER_ID)
            client.send_text('add^'+r.text+'^'+title+' '+name+'^'+str(message.chat.id))
            bot.send_message(message.chat.id, 'Песня принята. Вы встали в очередь. Ваша песня - '+name+' '+title+'\n') 
    else:
        bot.send_message(message.chat.id, 'Я не смог найти эту песню, повторите запрос позже.')
    sleep(0.1)

if __name__ == "__main__":
    bot.polling()
