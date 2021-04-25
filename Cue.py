# coding: utf-8
import os
import sys

class cueFile:
    def __init__(self, filename):

        self._fileName = filename

        self._Performer = '佚名'
        self._Title = '未知专辑名'
        self._Content = []

    def SetTitle(self, title):
        self._Title = title

    def SetPerformer(self, performer):
        self._Performer = performer

    def GetContent(self):
        return self._Content;

    def SaveContentToFile(self, filename):
        file_object = open(filename, 'w')
        for str0 in self._Content:
            file_object.write(str0 + "\r\n")
            #print(str0)
        file_object.close()


    def CueFromDir(self, dirpath):
        self._Content=[]
        self._Content.append('PERFORMER "' + self._Performer + '"')
        self._Content.append('TITLE "' + self._Title + '"')
        self._Content.append(' ')

        _Index = 1
        for filename in os.listdir(os.path.dirname(dirpath)):
            name = filename[:filename.find('.')]
            ext = filename[filename.rfind('.'):]
            # print(ext)
            ext=ext.upper()
            if ext != '.APE' and ext != '.WAV' and ext != '.FLAC' and ext != '.MP3':
                continue


            _linestr = 'FILE "' + filename + '" BINARY'
            self._Content.append(_linestr)

            _linestr = '    TITLE "' + name + '"'
            self._Content.append(_linestr)

            tmp = '%02d' % _Index
            _linestr = '    TRACK ' + tmp + ' AUDIO'
            self._Content.append(_linestr)

            self._Content.append('    INDEX 01 00:00:00')
            _Index += 1

        self.SaveContentToFile(dirpath + self._fileName)
        print("Cue file created !!!")
