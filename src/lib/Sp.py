#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import shutil
import cv2 as cv
import numpy as np


class sp():
    def __init__(self):
        pass

    def split(self, pic_dir):
        if not os.path.exists(pic_dir):
            print('table pic dir: {} not exist!'.format(pic_dir))
            exit()
        pics = os.listdir(pic_dir)
        for pic in pics:
            print('split pic: {}'.format(pic))
            self.__ts__(pic_dir, pic)

    def __ts__(self, pic_dir, pic):
        pic_path = os.path.join(pic_dir, pic)
        ora = cv.imread(pic_path)
        gray = cv.cvtColor(ora, cv.COLOR_BGR2GRAY)
        ret1, th1 = cv.threshold(gray, 190, 255, cv.THRESH_BINARY)
        '''
        ret2, th2 = cv.threshold(gray, 0, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)
        '''

        # split the picture of table
        [r, c] = th1.shape

        tr = [np.sum(x) for x in th1]
        min_r = np.min(tr)
        st_r = 2 * min_r

        tc = [np.sum(x) for x in th1.T]
        min_c = np.min(tc)
        st_c = 2 * min_c

        sl_r = self.__findSP__(tr, st_r)
        sl_c = self.__findSP__(tc, st_c)

        deta_r = 1
        deta_c = 1

        sp_dir = '../res/sp/{}'.format(pic)
        if os.path.exists(sp_dir):
            shutil.rmtree(sp_dir, True)
            os.makedirs(sp_dir)
        else:
            os.makedirs(sp_dir)

        suffix = pic.split('.')[-1]

        # sp
        for ri in range(1, len(sl_r)):
            for ci in range(1, len(sl_c)):
                s_r = sl_r[ri-1] + deta_r
                e_r = sl_r[ri] - deta_r

                s_c = sl_c[ci-1] + deta_c
                e_c = sl_c[ci] - deta_c

                imgx = ora[s_r:e_r, s_c: e_c, :]
                imgx_name = os.path.join(sp_dir,
                                         'img_{}_{}_.{}'.format(ri, ci, suffix))
                cv.imwrite(imgx_name, imgx)

    def __findSP__(self, tlist, st):
        res = []
        for i in range(1, len(tlist)):
            if tlist[i] < st:
                if tlist[i-1] > st:
                    res.append(i)
        return res
