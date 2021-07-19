#!/usr/bin/env python
# coding: utf-8

# In[5]:

from socket import *
import urllib
import re 

def getmixerargs():
    pygame.mixer.init()
    freq, size, chan = pygame.mixer.get_init()
    return freq, size, chan
def initmixer():
    BUFFER = 3072 # audio buffer size, number of samples since pygame 1.8.
    FREQ, SIZE, CHAN = getmixerargs()
    pygame.mixer.init(FREQ, SIZE, CHAN, BUFFER)
def playsound(soundfile):
    """Play sound through default mixer channel in blocking manner.
       This will load the whole sound into memory before playback"""
    pygame.init()
    pygame.mixer.init()
    sound = pygame.mixer.Sound(soundfile)
    clock = pygame.time.Clock()
    sound.play()
    while pygame.mixer.get_busy():
        clock.tick(1000)
def playmusic(soundfile):
    """Stream music with mixer.music module in blocking manner.
       This will stream the sound from disk while playing.
    """
    pygame.init()
    pygame.mixer.init()
    clock = pygame.time.clock()
    pygame.mixer.music.load(soundfile)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        clock.tick(1000)
def stopmusic():
    """stop currently playing music"""
    pygame.mixer.music.stop()
    
#HOW TO PLAY SONG:
initMixer()
#playmusic(filename)



def Flashmywindow(title):
    ID = win32gui.FindWindow(None, title)
    win32gui.FlashWindow(ID,True)
    
def FlashMyWindow2(title2):
    ID2 = win32gui.FlashWindow(None, title2)
    win32gui.FlashWindow(ID2,True)
    
def GetExternalIP():
    return str(gethostbyname(getfqdn()))

def FilteredMessage(EntryText):
    ""


# In[ ]:




