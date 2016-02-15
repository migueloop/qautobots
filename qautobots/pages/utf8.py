# coding=utf-8
from __future__ import unicode_literals

"""
A collection of UTF-8 strings.

The utf8 module contains UTF-8 strings for use in testing
input/output fields.  String are organized by language sets
with the exception of the general set which has phrases
that try to us as many characters (if not all) in that langauage

"""

general = {
    'arabic':
        'صِف خَلقَ خَودِ كَمِثلِ الشَمسِ إِذ بَزَغَت \
        — يَحظى الضَجيعُ بِها نَجلاءَ مِعطارِ  \
        هلا سكنت بذي ضغثٍ فقد زعموا \
        — شخصت تطلب ظبياً راح مجتازا \
        اصبر على حفظ خضر واستشر \
        فطنا، وزج همك في بغداذ منثملا \
        نصٌّ حكيمٌ لهُ سِرٌّ قاطِعٌ وَذُو شَأنٍ عَظيمٍ \
        مكتوبٌ على ثوبٍ أخضرَ ومُغلفٌ بجلدٍ أزرق',
    'bengali': 'আমি কাঁচ খেতে পারি, তাতে আমার কোনো ক্ষতি হয় না।',
    'bhutan':
        'ཨ་ཡིག་དཀར་མཛེས་ལས་འཁྲུངས་ཤེས་བློའི་གཏེར༎ ཕས་རྒོལ་ཝ་སྐྱ\
        ེས་ཟིལ་གནོན་གདོང་ལྔ་བཞིན༎ ཆགས་ཐོགས་ཀུན་བྲལ་མཚུངས་མེ\
        ད་འཇམ་དབྱངསམཐུས༎ མཧཱ་མཁས་པའི་གཙོ་བོ་ཉིད་འགྱུར་ཅིག།',
    'chinese_simple':
        '独立寒秋, 湘江北去, 橘子洲头。看万山红遍, 层林尽染; 漫江碧透，\
        百舸争流。 鹰击长空，鱼翔浅底，万物霜天竞自由。怅寥廓，问苍茫大地, \
        谁主沉浮',
    'chinese_traditional':
        '天地玄黃　宇宙洪荒　日月盈昃　辰宿列張 \
        寒來暑往　秋收冬藏  閏餘成歲　律召調陽 \
        雲騰致雨　露結為霜　金生麗水　玉出崑崗 \
        劍號巨闕　珠稱夜光　果珍李柰　菜重芥薑 \
        海鹹河淡　鱗潛羽翔  龍師火帝　鳥官人皇　\
        始製文字　乃服衣裳　推位讓國　有虞陶唐 \
        吊民伐罪　周發殷湯　坐朝問道　垂拱平章 \
        愛育黎首　臣伏戎羌  遐邇壹體　率賓歸王 \
        鳴鳳在樹　白駒食場　化被草木　賴及萬方',
    'danish':
        'Vår sære Zulu fra badeøya spilte jo whist og \
        quickstep i min taxi.',
    'devanagari':
        'ऋषियों को सताने वाले दुष्ट राक्षसों के राजा रावण का सर्वनाश \
        करने वाले विष्णुवतार भगवान श्रीराम, अयोध्या के महाराज दशरथ \
        के बड़े सपुत्र थे।',
    'emoji': u'\U0001f634' u'\U0001f638' u'\U0001f637',
    'english': 'The quick brown fox jumps over the lazy dog.',
    'french':
        'Les naïfs ægithales hâtifs pondant à Noël où il gèle sont sûrs \
        d\'être déçus en voyant leurs drôles d\'œufs abîmés.',
    'german':
        'Im finſteren Jagdſchloß am offenen Felsquellwaſſer \
        patzte der affig-flatterhafte kauzig-höf‌liche Bäcker über \
        ſeinem verſifften kniffligen C-Xylophon.',
    'greek':
        'Ο καλύμνιος σφουγγαράς ψιθύρισε πως θα βουτήξει \
        χωρίς να διστάζει.',
    'hebrew': 'דג סקרן שט לו בים זך אך לפתע פגש חבורה נחמדה שצצה כך.',
    'icelandic': 'Kæmi ný öxi hér, ykist þjófum nú bæði víl og ádrepa.',
    'italian':
        'Questa non è una frase: specialità regìa gigolò né \
        tiramisù o il paté.',
    'japanese_hiragana':
        'いろはにほへど　ちりぬるを わがよたれぞ　つねならむ \
        うゐのおくやま　けふこえて あさきゆめみじ　ゑひもせず',
    'japanese_katakana':
        'イロハニホヘト チリヌルヲ ワカヨタレソ ツネナラ ウヰノオクヤマ \
        ケフコエテ アサキユメミシ ヱヒモセスン',
    'kannada': 'ನನಗೆ ಹಾನಿ ಆಗದೆ, ನಾನು ಗಜನ್ನು ತಿನಬಹುದು',
    'korean': '키스의 고유조건은 입술끼리 만나야 하고 특별한 기술은 필요치 않다.',
    'malayalam':
        'അജവും ആനയും ഐരാവതവും ഗരുഡനും കഠോര \
        സ്വരം പൊഴിക്കെ ഹാരവും ഒഢ്യാണവും ഫാലത്തില്‍ \
        മഞ്ഞളും ഈറന്‍ കേശത്തില്‍ ഔഷധ എണ്ണയുമായി \
        ഋതുമതിയും അനഘയും ഭൂനാഥയുമായ ഉമ ദുഃഖഛവിയോടെ \
        ഇടതു പാദം ഏന്തി ങ്യേയാദൃശം നിര്‍ഝരിയിലെ \
        ചിറ്റലകളെ ഓമനിക്കുമ്പോള്‍ ബാ‍ലയുടെ കണ്‍കളില്‍ \
        നീര്‍ ഊര്‍ന്നു വിങ്ങി.',
    'myanmar':
        'သီဟိုဠ်မှ ဉာဏ်ကြီးရှင်သည် \
        အာယုဝဍ္ဎနဆေးညွှန်းစာကို \
        ဇလွန်ဈေးဘေးဗာဒံပင်ထက် အဓိဋ္ဌာန်လျက် \
        ဂဃနဏဖတ်ခဲ့သည်။',
    'polish': 'Pójdźże, kiń tę chmurność w głąb flaszy!',
    'portugese':
        'o próximo vôo à noite sobre o Atlântico, põe \
        freqüentemente o único médico',
    'russian': 'В чащах юга жил-был цитрус? Да, но фальшивый экземпляр! ёъ.',
    'spanish':
        'El pingüino Wenceslao hizo kilómetros bajo \
        exhaustiva lluvia y frío, añoraba a su querido cachorro.',
    'swedish': 'Flygande bäckasiner söka hwila på mjuka tuvor.',
    'taiwanese': 'Góa ē-tàng chia̍h po-lê, mā bē tio̍h-siong.',
    'tamil': 'நான் கண்ணாடி சாப்பிடுவேன், அதனால் எனக்கு ஒரு கேடும் வராது.',
    'telugu': 'నేను గాజు తినగలను మరియు అలా చేసినా నాకు ఏమి ఇబ్బంది లేదు',
    'thai':
        'เป็นมนุษย์สุดประเสริฐเลิศคุณค่า กว่าบรรดาฝูงสัตว์เดรัจฉาน \
        จงฝ่าฟันพัฒนาวิชาการ อย่าล้างผลาญฤๅเข่นฆ่าบีฑาใคร \
        ไม่ถือโทษโกรธแช่งซัดฮึดฮัดด่า หัดอภัยเหมือนกีฬาอัชฌาสัย \
        ปฏิบัติประพฤติกฎกำหนดใจ พูดจาให้จ๊ะ ๆ จ๋า ๆ น่าฟังเอยฯ.',
    'tibetan':
        '༈ དཀར་མཛེས་ཨ་ཡིག་ལས་འཁྲུངས་ཡེ་ཤེས་གཏེར། །ཕས་རྒོལ་ཝ་སྐྱ\
        ེས་ཟིལ་གནོན་གདོང་ལྔ་བཞིན། །ཆགས་ཐོགས་ཀུན་བྲལ་མཚུངས་མེ\
        ད་འཇམ་བྱངས་མཐུས། །མ་ཧཱ་མཁས་པའི་གཙོ་བོ་ཉིད་གྱུར་ཅིག།',
}