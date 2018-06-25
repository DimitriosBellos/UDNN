# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np
import platform
import os
import sys
from src.utils.timer import Timer
from src.utils.colors import Colors


def printStep(seconds_):
    seconds = seconds_
    days = np.floor(seconds / (3600 * 24))
    seconds = seconds - days * 3600 * 24
    hours = np.floor(seconds / (3600))
    seconds = seconds - hours * 3600
    minutes = np.floor(seconds / (60))
    seconds = seconds - minutes * 60
    secondsf = np.floor(seconds)
    seconds = seconds - secondsf
    millis = np.floor(seconds * 1000)
    f = ''
    if days > 0:
        f = f + ('%d' % days) + 'd'
    if hours > 0:
        f = f + ('%d' % hours) + 'h'
    if minutes > 0:
        f = f + ('%d' % minutes) + 'm'
    if secondsf >= 0:
        f = f + ('%d' % secondsf) + 's'
    if millis > 0:
        if millis > 99:
            millis = np.around(millis, -1) / 10
        f = f + ('%d' % millis) + 'ms'
    return f


def printTime(seconds_):
    seconds = seconds_
    days = np.floor(seconds / (3600 * 24))
    seconds = seconds - days * 3600 * 24
    hours = np.floor(seconds / (3600))
    seconds = seconds - hours * 3600
    minutes = np.floor(seconds / (60))
    seconds = seconds - minutes * 60
    secondsf = np.floor(seconds)
    seconds = seconds - secondsf
    millis = np.floor(seconds * 1000)
    f = ''
    if days > 0:
        f = f + ('%d' % days) + 'd'
    if hours >= 0:
        f = f + ('%d' % hours) + 'h'
    if minutes >= 0:
        f = f + ('%d' % minutes) + 'm'
    if secondsf >= 0:
        f = f + ('%d' % secondsf) + 's'
    if millis > 0:
        if millis > 99:
            millis = np.around(millis, -1) / 10
        f = f + ('%d' % millis) + 'ms'
    return f


def getTermLength():
    if platform.system() == 'Windows':
        return 80
    tputf = os.popen('tput cols', 'r')
    w = int(tputf.read().split('\n')[0])
    tputf.close()
    return w


barDone = True
previous = -1
tm = ''
timer = []
times = []
indices = []
termLength = min(getTermLength(), 120)


def PrintProgress(epoch, totalepoches, strs):
    # defaults:
    # local barLength = termLength - 34
    global barDone
    global previous
    global tm
    global timer
    global times
    global indices
    global termLength
    barLength = 50
    smoothing = 100
    maxfps = 10
    syss = Colors()
    # Compute percentage
    percent = ((epoch) * barLength) / totalepoches
    # start new bar
    if (barDone and ((previous == -1) or (percent < previous))):
        barDone = False
        previous = -1
        tm = ''
        timer = Timer()
        times = [timer.get_value()]
        indices = [epoch]
    else:
        sys.stdout.write('\r')
    leng = len(('%d' % totalepoches))
    sys.stdout.write(syss().Magenta + 'Epoch:' + syss().Cyan + (' %d/%d' % (epoch, totalepoches)))
    # if (percent ~= previous and not barDone) then
    if (not barDone):
        previous = percent
        # print bar
        sys.stdout.write(syss().Green + '▕')
        for i in range(1, barLength + 1):
            if (i <= np.floor(percent)):
                sys.stdout.write(syss().Green + '█')
            elif (i == np.floor(percent) + 1):
                if (percent - np.floor(percent) < 0.0625):
                    sys.stdout.write(' ')
                elif (percent - np.floor(percent) < 0.1875):
                    sys.stdout.write(syss().Green + '▏')
                elif (percent - np.floor(percent) < 0.3125):
                    sys.stdout.write(syss().Green + '▎')
                elif (percent - np.floor(percent) < 0.4375):
                    sys.stdout.write(syss().Green + '▍')
                elif (percent - np.floor(percent) < 0.5625):
                    sys.stdout.write(syss().Green + '▌')
                elif (percent - np.floor(percent) < 0.6875):
                    sys.stdout.write(syss().Green + '▋')
                elif (percent - np.floor(percent) < 0.8125):
                    sys.stdout.write(syss().Green + '▊')
                elif (percent - np.floor(percent) < 0.9375):
                    sys.stdout.write(syss().Green + '▉')
                else:
                    sys.stdout.write(syss().Green + '█')
            else:
                sys.stdout.write(' ')
        sys.stdout.write(syss().Green + '▏')
        # time stats
        elapsed = timer.get_value()
        if (epoch - indices[0]) == 0:
            step = 0
        else:
            step = (elapsed - times[0]) / (epoch - indices[0])
        if epoch <= indices[0]:
            indices = []
            step = 0
        remaining = max(0, (totalepoches - epoch) * step)
        indices.append(epoch)
        times.append(elapsed)
        if len(indices) > smoothing:
            del indices[0]
            del times[0]
        # Print remaining time when running or total time when done.
        sys.stdout.write(syss().Red + ' MSE: ' + syss().Green + strs[0] + syss().Red + ' MSE_CI: ' + syss().Green + strs[1])
        tm = ' ETA: ' + printTime(remaining)
        tm = tm + ' | Elapsed: ' + printTime(elapsed)
        tm = tm + ' | Step: ' + printStep(step) + '              '
        sys.stdout.write(syss().Cyan + tm)
        # go back to center of bar, and print progress
        for i in range(1, int(18 + len(tm) + len(strs[0]) + len(strs[1]) + np.floor(barLength / 2) + 1)):
            sys.stdout.write('\b')
        sys.stdout.write(syss().Green + (' %3.2f%% ' % (percent * 100 / barLength)))
        # reset for next bar
        if (percent == barLength):
            barDone = True
            sys.stdout.write('\n')
        # flush
        sys.stdout.write('\r')
        sys.stdout.flush()
        return
    else:
        return


barDoneE = True
previousE = -1
tmE = ''
timerE = []
timesE = []
indicesE = []
termLengthE = min(getTermLength(), 120)


def PrintProgressE(epoch, totalepoches, strs):
    # defaults:
    # local barLength = termLengthE - 34
    global barDoneE
    global previousE
    global tmE
    global timerE
    global timesE
    global indicesE
    global termLengthE
    barLength = 50
    smoothing = 100
    maxfps = 10
    syss = Colors()
    # Compute percentage
    percent = ((epoch) * barLength) / totalepoches
    # start new bar
    if (barDoneE and ((previousE == -1) or (percent < previousE))):
        barDoneE = False
        previousE = -1
        tmE = ''
        timerE = Timer()
        timesE = [timerE.get_value()]
        indicesE = [epoch]
    else:
        sys.stdout.write('\r')
    leng = len(('%d' % totalepoches))
    sys.stdout.write(syss().Magenta + 'Epoch:' + syss().Cyan + (' %d/%d' % (epoch, totalepoches)))
    # if (percent ~= previousE and not barDoneE) then
    if (not barDoneE):
        previousE = percent
        # print bar
        sys.stdout.write(syss().Green + '▕')
        for i in range(1, barLength + 1):
            if (i <= np.floor(percent)):
                sys.stdout.write(syss().Green + '█')
            elif (i == np.floor(percent) + 1):
                if (percent - np.floor(percent) < 0.0625):
                    sys.stdout.write(' ')
                elif (percent - np.floor(percent) < 0.1875):
                    sys.stdout.write(syss().Green + '▏')
                elif (percent - np.floor(percent) < 0.3125):
                    sys.stdout.write(syss().Green + '▎')
                elif (percent - np.floor(percent) < 0.4375):
                    sys.stdout.write(syss().Green + '▍')
                elif (percent - np.floor(percent) < 0.5625):
                    sys.stdout.write(syss().Green + '▌')
                elif (percent - np.floor(percent) < 0.6875):
                    sys.stdout.write(syss().Green + '▋')
                elif (percent - np.floor(percent) < 0.8125):
                    sys.stdout.write(syss().Green + '▊')
                elif (percent - np.floor(percent) < 0.9375):
                    sys.stdout.write(syss().Green + '▉')
                else:
                    sys.stdout.write(syss().Green + '█')
            else:
                sys.stdout.write(' ')
        sys.stdout.write(syss().Green + '▏')
        # time stats
        elapsed = timerE.get_value()
        if (epoch - indicesE[0]) == 0:
            step = 0
        else:
            step = (elapsed - timesE[0]) / (epoch - indicesE[0])
        if epoch <= indicesE[0]:
            indicesE = []
            step = 0
        remaining = max(0, (totalepoches - epoch) * step)
        indicesE.append(epoch)
        timesE.append(elapsed)
        if len(indicesE) > smoothing:
            del indicesE[0]
            del timesE[0]
        # Print remaining time when running or total time when done.
        sys.stdout.write(syss().Red + ' MSE: ' + syss().Green + strs[0] + syss().Red + ' MSE_CI: ' + syss().Green + strs[1])
        tmE = ' ETA: ' + printTime(remaining)
        tmE = tmE + ' | Elapsed: ' + printTime(elapsed)
        tmE = tmE + ' | Step: ' + printStep(step) + '              '
        sys.stdout.write(syss().Cyan + tmE)
        # go back to center of bar, and print progress
        for i in range(1, int(18 + len(tmE) + len(strs[0]) + len(strs[1]) + np.floor(barLength / 2) + 1)):
            sys.stdout.write('\b')
        sys.stdout.write(syss().Green + (' %3.2f%% ' % (percent * 100 / barLength)))
        # reset for next bar
        if (percent == barLength):
            barDoneE = True
            sys.stdout.write('\n')
        # flush
        sys.stdout.write('\r')
        sys.stdout.flush()
        return
    else:
        return


barDoneT = True
previousT = -1
tmT = ''
timerT = []
timesT = []
indicesT = []
termLengthT = min(getTermLength(), 120)


def PrintProgressT(epoch, totalepoches, strs):
    # defaults:
    # local barLength = termLengthT - 34
    global barDoneT
    global previousT
    global tmT
    global timerT
    global timesT
    global indicesT
    global termLengthT
    barLength = 50
    smoothing = 100
    maxfps = 10
    syss = Colors()
    # Compute percentage
    percent = ((epoch) * barLength) / totalepoches
    # start new bar
    if (barDoneT and ((previousT == -1) or (percent < previousT))):
        barDoneT = False
        previousT = -1
        tmT = ''
        timerT = Timer()
        timesT = [timerT.get_value()]
        indicesT = [epoch]
    else:
        sys.stdout.write('\r')
    leng = len(('%d' % totalepoches))
    sys.stdout.write(syss().Magenta + 'Epoch:' + syss().Cyan + (' %d/%d' % (epoch, totalepoches)))
    # if (percent ~= previousT and not barDoneT) then
    if (not barDoneT):
        previousT = percent
        # print bar
        sys.stdout.write(syss().Green + '▕')
        for i in range(1, barLength + 1):
            if (i <= np.floor(percent)):
                sys.stdout.write(syss().Green + '█')
            elif (i == np.floor(percent) + 1):
                if (percent - np.floor(percent) < 0.0625):
                    sys.stdout.write(' ')
                elif (percent - np.floor(percent) < 0.1875):
                    sys.stdout.write(syss().Green + '▏')
                elif (percent - np.floor(percent) < 0.3125):
                    sys.stdout.write(syss().Green + '▎')
                elif (percent - np.floor(percent) < 0.4375):
                    sys.stdout.write(syss().Green + '▍')
                elif (percent - np.floor(percent) < 0.5625):
                    sys.stdout.write(syss().Green + '▌')
                elif (percent - np.floor(percent) < 0.6875):
                    sys.stdout.write(syss().Green + '▋')
                elif (percent - np.floor(percent) < 0.8125):
                    sys.stdout.write(syss().Green + '▊')
                elif (percent - np.floor(percent) < 0.9375):
                    sys.stdout.write(syss().Green + '▉')
                else:
                    sys.stdout.write(syss().Green + '█')
            else:
                sys.stdout.write(' ')
        sys.stdout.write(syss().Green + '▏')
        # time stats
        elapsed = timerT.get_value()
        if (epoch - indicesT[0]) == 0:
            step = 0
        else:
            step = (elapsed - timesT[0]) / (epoch - indicesT[0])
        if epoch <= indicesT[0]:
            indicesT = []
            step = 0
        remaining = max(0, (totalepoches - epoch) * step)
        indicesT.append(epoch)
        timesT.append(elapsed)
        if len(indicesT) > smoothing:
            del indicesT[0]
            del timesT[0]
        # Print remaining time when running or total time when done.
        sys.stdout.write(syss().Red + ' MSE: ' + syss().Green + strs[0] + syss().Red + ' MSE_CI: ' + syss().Green + strs[1])
        tmT = ' ETA: ' + printTime(remaining)
        tmT = tmT + ' | Elapsed: ' + printTime(elapsed)
        tmT = tmT + ' | Step: ' + printStep(step) + '              '
        sys.stdout.write(syss().Cyan + tmT)
        # go back to center of bar, and print progress
        for i in range(1, int(18 + len(tmT) + len(strs[0]) + len(strs[1]) + np.floor(barLength / 2) + 1)):
            sys.stdout.write('\b')
        sys.stdout.write(syss().Green + (' %3.2f%% ' % (percent * 100 / barLength)))
        # reset for next bar
        if (percent == barLength):
            barDoneT = True
            sys.stdout.write('\n')
        # flush
        sys.stdout.write('\r')
        sys.stdout.flush()
        return
    else:
        return
