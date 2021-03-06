import logging
import threading
import time

import ezclib

log = logging.getLogger(__name__)


def main():
    client = ezclib.EzcapechatRTMPProtocol(ezclib.CONFIG.ROOM, ezclib.CONFIG.USER, ezclib.CONFIG.EMAIL, ezclib.CONFIG.PASSWORD)

    t = threading.Thread(target=client.connect)
    t.daemon = True
    t.start()

    while not client.is_connected:
        time.sleep(2)
    while client.is_connected:
        chat_msg = raw_input()
        client.send_public(chat_msg)


if __name__ == '__main__':
    formatter = '%(asctime)s : %(levelname)s : %(filename)s : %(lineno)d : %(funcName)s() : %(name)s : %(message)s'
    if ezclib.CONFIG.DEBUG_TO_FILE:
        logging.basicConfig(filename='ezclib_debug.log', level=ezclib.CONFIG.FILE_DEBUG_LEVEL, format=formatter)
    else:
        log.addHandler(logging.NullHandler)

    log.info('Starting ezcapechat client.')

    main()
