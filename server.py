from flask import Flask, render_template, request
import json

Surahs = [
    ("الفاتحة", 7),
    ("البقرة", 286),
    ("آل عمران", 200),
    ("النساء", 176),
    ("المائدة", 120),
    ("الأنعام", 165),
    ("الأعراف", 206),
    ("الأنفال", 75),
    ("التوبة", 129),
    ("يونس", 109),
    ("هود", 123),
    ("يوسف", 111),
    ("الرعد", 43),
    ("إبراهيم", 52),
    ("الحجر", 99),
    ("النحل", 128),
    ("الإسراء", 111),
    ("الكهف", 110),
    ("مريم", 98),
    ("طه", 135),
    ("الأنبياء", 112),
    ("الحج", 78),
    ("المؤمنون", 118),
    ("النور", 64),
    ("الفرقان", 77),
    ("الشعراء", 227),
    ("النمل", 93),
    ("القصص", 88),
    ("العنكبوت", 69),
    ("الروم", 60),
    ("لقمان", 34),
    ("السجدة", 30),
    ("الأحزاب", 73),
    ("سبأ", 54),
    ("فاطر", 45),
    ("يس", 83),
    ("الصافات", 182),
    ("ص", 88),
    ("الزمر", 75),
    ("غافر", 85),
    ("فصلت", 54),
    ("الشورى", 53),
    ("الزخرف", 89),
    ("الدخان", 59),
    ("الجاثية", 37),
    ("الأحقاف", 35),
    ("محمد", 38),
    ("الفتح", 29),
    ("الحجرات", 18),
    ("ق", 45),
    ("الذاريات", 60),
    ("الطور", 49),
    ("النجم", 62),
    ("القمر", 55),
    ("الرحمن", 78),
    ("الواقعة", 96),
    ("الحديد", 29),
    ("المجادلة", 22),
    ("الحشر", 24),
    ("الممتحنة", 13),
    ("الصف", 14),
    ("الجمعة", 11),
    ("المنافقون", 11),
    ("التغابن", 18),
    ("الطلاق", 12),
    ("التحريم", 12),
    ("الملك", 30),
    ("القلم", 52),
    ("الحاقة", 52),
    ("المعارج", 44),
    ("نوح", 28),
    ("الجن", 28),
    ("المزمل", 20),
    ("المدثر", 56),
    ("القيامة", 40),
    ("الإنسان", 31),
    ("المرسلات", 50),
    ("النبأ", 40),
    ("النازعات", 46),
    ("عبس", 42),
    ("التكوير", 29),
    ("الإنفطار", 19),
    ("المطففين", 36),
    ("الإنشقاق", 25),
    ("البروج", 22),
    ("الطارق", 17),
    ("الأعلى", 19),
    ("الغاشية", 26),
    ("الفجر", 30),
    ("البلد", 20),
    ("الشمس", 15),
    ("الليل", 21),
    ("الضحى", 11),
    ("الشرح", 8),
    ("التين", 8),
    ("العلق", 19),
    ("القدر", 5),
    ("البينة", 8),
    ("الزلزلة", 8),
    ("العاديات", 11),
    ("القارعة", 11),
    ("التكاثر", 8),
    ("العصر", 3),
    ("الهمزة", 9),
    ("الفيل", 5),
    ("قريش", 4),
    ("الماعون", 7),
    ("الكوثر", 3),
    ("الكافرون", 6),
    ("النصر", 3),
    ("المسد", 5),
    ("الإخلاص", 4),
    ("الفلق", 5),
    ("الناس", 6)
]
app = Flask(__name__)

# Define the list of Surahs as tuples (label, value)
surah_options = [
    (surah[0], i+1) for i,surah in enumerate(Surahs)
]

# Define a dictionary to store the number of Ayahs for each Surah
ayah_numbers = {
    1: 7,
    2: 286,
    3: 200,
    4: 176,
    5: 120
}

for i, surah in enumerate(Surahs):
    ayah_number = surah[1]
    ayah_numbers[i+1] = ayah_number



# Define a list of Ayah options as tuples (value, label)

def save_to_db(obj: dict):
    data = []
    with open('db.jsonl', 'r') as f:
        for line in f.readlines():
            data.append(json.loads(line))
    
    if obj not in data:
        data.append(obj)
    data = list(data)
    with open('db.jsonl', 'w') as f:
        for line in data:
            json.dump(line, f, ensure_ascii = False)
            f.write('\n')
    print(data)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        surah = request.form['surah']
        question = request.form['question']
        answer = request.form['answer']
        from_ayah = int(request.form['from'])
        to_ayah = int(request.form['to'])
        # Process the form data as needed
        obj = {'Surah': surah, 'Question': question, 'Answer': answer, 'From': from_ayah, 'To': to_ayah}
        save_to_db(obj)
        print(obj)
    return render_template('index.html', surah_options=surah_options, ayah_numbers=ayah_numbers)

if __name__ == '__main__':
    app.run(debug=True)
