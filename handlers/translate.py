
from handlers.handler import Handler
import googletrans


class TranslateHandler(Handler):
    def __init__(self):
        self.state = {}

    @staticmethod  
    async def translate(inter,lang_to:str ,text:str):
        lang_to = lang_to.lower()
        if lang_to not in googletrans.LANGUAGES and lang_to not in googletrans.LANGCODES:
            raise ('Invalid argument')

        
        translator = googletrans.Translator()
        lang_detected=translator.detect(text).lang
        
        text_translated = translator.translate(text,src=lang_detected, dest=lang_to).text
        await inter.send(text_translated)
        
    @staticmethod
    def setup():
        TranslateHandler()
