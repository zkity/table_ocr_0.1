#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'zk'
__date__ = 'Jan 11 2020'

'''
generate an excel file from a picture of a table
'''
from lib.Util import util
from lib.Sp import sp
from lib.Ocr import ocr


def main():
    conf_dict = util.getConfig()
    sp_o = sp()
    sp_o.split(conf_dict.get('ora_path'))
    print('ocr ...')
    ocr_o = ocr(conf_dict.get('app_id'),
                conf_dict.get('api_key'),
                conf_dict.get('secret_key'),
                conf_dict.get('mode'),
                conf_dict.get('excel_path'))
    ocr_o.recon()


if __name__ == "__main__":
    main()
