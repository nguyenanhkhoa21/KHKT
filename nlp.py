import spacy

nlp = spacy.load("en_core_web_sm")
with open("data1/pyschology.txt", "r", encoding="utf-8") as f:
    text = f.read()
print(text)
doc = nlp(text)
print(doc)
print(len(text))
print(len(doc))
for token in text[0:20]:
    print(token)
for token in doc[0:20]:
    print(token)
for token in text.split()[:10]:
    print(token)

words = text.split()[:10]

i=5
for token in doc[i:8]:
    print(f"Spacy Token {i}:\n{token}\nWord split{i}\n{words[i]}\n\n")
    i = i + 1
for sent in doc.sents:
    print(sent)
"\n"
"\n"
sentences1 = list(doc.sents)[0]
print(sentences1)
token2 = sentences1[4]
print(token2)
print(f"'{token2.text}'")
print(token2.left_edge)
print(token2.right_edge)
# ent_type là mã số của loại thự thể    380 - Person 384 - GPE  0 - Không phải thực thể
print(token2.ent_type)   
# .ent_type ược sử dụng để truy xuất loại thực thể (entity type) của một token hoặc một cụm từ khi bạn thực hiện 
# nhận dạng thực thể có tên (NER - Named Entity Recognition).
# PERSON (tên người), ORG (tổ chức), GPE (tên địa danh), DATE (ngày tháng)
# và nhiều loại khác.
print(token2.ent_type_)               

# Trong spaCy, thuộc tính .ent_iob_ (Inside-Outside-Beginning) được sử dụng để cho biết vị trí của token trong một thực thể có tên 
# (Named Entity). Nó thể hiện liệu token đó là bên trong, bên ngoài, hoặc bắt đầu của một thực thể. 
# B (Beginning): Token này là token đầu tiên của một thực thể.
# I (Inside): Token này nằm bên trong một thực thể nhưng không phải là token đầu tiên.
# O (Outside): Token này không thuộc về bất kỳ thực thể nào.
print(token2.ent_iob_)
# Trong spaCy, thuộc tính .lemma_ trả về gốc từ (lemma) của một token. 
# Gốc từ là dạng cơ bản của một từ, loại bỏ các biến thể ngữ pháp như chia động từ, số nhiều, v.v
print(sentences1[29].lemma_)
# thuộc tính .morph trả về các đặc điểm hình thái học của một token, như thì, số, ngôi, giới tính, và cách chia động từ hoặc danh từ.
#Số: số ít hay số nhiều (Singular, Plural)
# Thì: quá khứ, hiện tại, tương lai (Past, Present,future)
# Ngôi: ngôi thứ nhất, thứ hai, thứ ba (1st, 2nd, 3rd)
# Giới tính: giống đực, giống cái (Masculine, Feminine)
# Thể: chủ động hay bị động (Active, Passive)
print(sentences1[29].morph)#Aspect=Perf:Hđ đã hoàn thành|Tense=Past:Hđ diễn ra trong quá khứ|VerbForm=Part:Đt ở dạng phân từ quá khứ.

# .pos_ trả về phân loại từ loại (part of speech) của một token dưới dạng chuỗi
# NOUN: Danh từ
# VERB: Động từ
# ADJ: Tính từ
# ADV: Trạng từ
# PRON: Đại từ
# PROPN: Danh từ riêng
# ADP: Giới từ
# DET: Mạo từ
# NUM: Số
# CONJ: Liên từ
# AUX: Động từ trợ giúp
# PUNCT: Dấu câu

print(sentences1[30].pos_)
# .dep_ trả về mối quan hệ phụ thuộc ngữ pháp (dependency relation) của một token trong một câu.
# nsubj: Chủ ngữ danh từ
# dobj: Tân ngữ trực tiếp
# prep: Giới từ
# pobj: Tân ngữ của giới từ
# amod: Tính từ mô tả danh từ
# acl: Mệnh đề tính từ
# conj: Liên từ
# ROOT: Từ gốc của câu (từ chính)
# det (mạo từ xác định danh từ)
# punct (dấu câu)
print(sentences1[12].dep_)
print(token2.dep_)

# .lang_ trả về ngôn ngữ của mô hình ngôn ngữ đang được sử dụng
print(token2.lang_)



































