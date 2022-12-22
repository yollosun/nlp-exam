from transformers import PegasusForConditionalGeneration, PegasusTokenizer
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM


class En_To_Ru_Translator:
    def __init__(self):
        self.en_ru_tokenizer = AutoTokenizer.from_pretrained(
            "Helsinki-NLP/opus-mt-en-ru")
        self.en_ru_model = AutoModelForSeq2SeqLM.from_pretrained(
            "Helsinki-NLP/opus-mt-en-ru")

    def translate_from_en_to_ru(self, en_text):
        text = en_text
        encoded_input = self.en_ru_tokenizer(text, return_tensors="pt")
        output = self.en_ru_model.generate(**encoded_input)
        out_text = self.en_ru_tokenizer.batch_decode(output,
                                                     skip_special_tokens=True)

        return out_text


class Ru_To_En_Translator:
    def __init__(self):
        self.ru_en_tokenizer = AutoTokenizer.from_pretrained(
            "Helsinki-NLP/opus-mt-ru-en")
        self.ru_en_model = AutoModelForSeq2SeqLM.from_pretrained(
            "Helsinki-NLP/opus-mt-ru-en")

    def translate_from_ru_to_en(self, ru_text):
        text = ru_text
        encoded_input = self.ru_en_tokenizer(text, return_tensors="pt")
        output = self.ru_en_model.generate(**encoded_input)
        out_text = self.ru_en_tokenizer.batch_decode(output,
                                                     skip_special_tokens=True)

        return out_text


class PegasusTransformer:
    def __init__(self, model_name_or_path):
        self.tokenizer = PegasusTokenizer.from_pretrained(model_name_or_path)
        self.model = PegasusForConditionalGeneration.from_pretrained(
            model_name_or_path)

    def paraphrase_russian_text(self, input_text_list):
        input_text_list = input_text_list[0].split(".")
        ru_to_en_translator = Ru_To_En_Translator()
        en_to_ru_translator = En_To_Ru_Translator()

        paraphrase = ""

        for i in input_text_list:
            print(i)
            paraphrase += en_to_ru_translator.translate_from_en_to_ru(
                self.__get_response(ru_to_en_translator.translate_from_ru_to_en(i)[0]))[0] + " "

        return paraphrase

    def paraphrase_english_text(self, input_text_list):
        paraphrase = ""
        for i in input_text_list:
            output = self.__get_response(i)
            paraphrase += output[0] + " "
        self.model = 0
        self.tokenizer = 0
        return paraphrase

    def __get_response(self, input_text):
        batch = self.tokenizer.prepare_seq2seq_batch(
            [input_text], truncation=True, padding='longest', max_length=60, return_tensors="pt")
        translated = self.model.generate(**batch, max_length=60, num_beams=10,
                                         num_return_sequences=1, temperature=1.5)
        tgt_text = self.tokenizer.batch_decode(
            translated, skip_special_tokens=True)
        return tgt_text
