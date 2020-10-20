import os
import sys
import time
from view import view
from preprocessing import preprocessing
from translator import translator
from voice import voice
import buttons


def main():
    event_handler = view()
    prep = preprocessing()
    trans = translator()
    announcer = voice()
    buttons.gpio_init()
    button_thread = buttons.Thread(target=buttons.thread_voice_flag, args=(1, event_handler))
    button_thread.start()

    while True:
        voc_event = event_handler.voice_flag
        cap_event = event_handler.capture_flag
        ret_val, cap_img = event_handler.handle_capture()
        event_handler.show_img(cap_img)

        if voc_event:
            print("hello")
            preprocessed_img = prep.preprocess_img(cap_img)
            paragraph_list = [prep.run_tesseract(preprocessed_img)]
            print(paragraph_list)
        #
        #     if is_eng:
        #         paragraph_list = trans.translate(paragraph_list, 'ko')
        #
        #     ptr_voice = announcer.store_voice(paragraph_list)  # default en
        #
        #     success = event_handler.print_voice(ptr_voice)
        #
        #     if not success:
        #         event_handler.print_error()
        #
            event_handler.set_voice_flag = False

        # time.sleep(1)
        # print("next")


if __name__ == '__main__':
    main()
