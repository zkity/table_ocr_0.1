#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json


class util():
    def getConfig():
        try:
            with open('../res/conf.json', 'r') as cf:
                conf = json.loads(cf.read())
        except Exception as e:
            print('configure file broken or miss!')
            print(e)
            exit()

        try:
            bd_conf = conf.get('bd')
            app_id = bd_conf.get('app_id')
            api_key = bd_conf.get('api_key')
            secret_key = bd_conf.get('secret_key')

            us_conf = conf.get('us')
            mode = us_conf.get('mode')
            ora_path = us_conf.get('ora_path')
            excel_path = us_conf.get('excel_path')
        except Exception as e:
            print('configure file broken!')
            print(e)
            exit()

        return {
                "app_id": app_id,
                "api_key": api_key,
                "secret_key": secret_key,
                "mode": mode,
                "ora_path": ora_path,
                "excel_path": excel_path
                }
