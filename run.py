#!/usr/bin/env python3
# coding=UTF8
from app.console import start
import logging


if __name__ == "__main__":
    logging.basicConfig(format='[%(asctime)s] %(filename)s:%(lineno)d %(levelname)s - %(message)s',
                        level=logging.INFO, filename='log.log', datefmt='%d.%m.%Y %H:%M:%S')
    start()

