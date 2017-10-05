import logging
import time
from threading import Thread, Event

from respeaker import Microphone


def task(quit_event):
    mic = Microphone(quit_event=quit_event)

    while not quit_event.is_set():
        if mic.wakeup('respeaker'):
            print('Wake up')
            data = mic.listen()
            text = mic.recognize(data)
            if text:
                print('Recognized %s' % text)


def main():
    print('ReSpeaker is running..')
    logging.basicConfig(level=logging.DEBUG)
    quit_event = Event()
    thread = Thread(target=task, args=(quit_event,))
    thread.start()
    while True:
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            print('Quit')
            quit_event.set()
            break
    thread.join()

if __name__ == '__main__':
    main()

