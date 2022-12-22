# from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# ru_en_tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-ru-en")
# ru_en_model = AutoModelForSeq2SeqLM.from_pretrained(
#     "Helsinki-NLP/opus-mt-ru-en")

# en_ru_tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-ru")
# en_ru_model = AutoModelForSeq2SeqLM.from_pretrained(
#     "Helsinki-NLP/opus-mt-en-ru")


# def translate_from_en_to_ru(en_text):
#     text = en_text
#     encoded_input = en_ru_tokenizer(text, return_tensors="pt")
#     output = en_ru_model.generate(**encoded_input)
#     out_text = en_ru_tokenizer.batch_decode(output,
#                                             skip_special_tokens=True)
#     en_ru_tokenizer = 0
#     en_ru_model = 0

#     return out_text


# def translate_from_ru_to_en(ru_text):
#     text = ru_text
#     encoded_input = ru_en_tokenizer(text, return_tensors="pt")
#     output = ru_en_model.generate(**encoded_input)
#     out_text = ru_en_tokenizer.batch_decode(output,
#                                             skip_special_tokens=True)
#     ru_en_tokenizer = 0
#     ru_en_model = 0

#     return out_text
