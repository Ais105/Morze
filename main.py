from graphics import *
import time, math, pyaudio

def sound(sec):
    PyAudio = pyaudio.PyAudio
    BITRATE = 16000
    FREQUENCY = 12000

    LENGTH = sec

    NUMBEROFFRAMES = int(BITRATE * LENGTH)
    RESTFRAMES = NUMBEROFFRAMES % BITRATE
    WAVEDATA = ''

    for x in range(NUMBEROFFRAMES):
        WAVEDATA = WAVEDATA + chr(int(math.sin(x / ((BITRATE / FREQUENCY) / math.pi)) * 127 + 128))

    for x in range(RESTFRAMES):
        WAVEDATA = WAVEDATA + chr(128)

    p = PyAudio()
    stream = p.open(format=p.get_format_from_width(1),
                    channels=1,
                    rate=BITRATE,
                    output=True)

    stream.write(WAVEDATA)
    stream.stop_stream()
    stream.close()
    p.terminate()

def draw_point(win, a,b):

    pt = Circle(Point(a,b), 10)
    pt.setFill('green')
    pt.draw(win)

def draw_rect(win, a, b):

    lin = Line(Point(a, b), Point(a + 20, b))
    lin.setWidth(4)
    lin.setFill('green')
    lin.draw(win)

def write_tex(win, a, b, mes):

    mesage = Text(Point(a, b), mes)
    mesage.setTextColor('green')
    mesage.setStyle('italic')
    mesage.setSize(20)
    mesage.draw(win)

def main():

    s = str(input())
    win = GraphWin('morze_lang', 1500, 500) # give title and dimensions
    win.setBackground('black')
    #win.yUp() # make right side up coordinates!
    h = win.getHeight() / 3
    th = win.getHeight() / 2
    w = 20
    tw = 20
    d = {
        '.-' : 'А', '-...' : 'Б', '.--' : 'В', '--.' : 'Г', '-..' : 'Д', '.' : 'Е', '...-' : 'Ж',
        '--..' : 'З', '..' : 'И', '.---' : 'Й', '-.-': 'К', '.-..': 'Л', '--': 'М', '-.': 'Н',
        '---': 'О', '.--.': 'П', '.-.': 'Р', '...': 'С', '-': 'Т', '..-': 'У', '..-.': 'Ф', '....': 'Х',
        '-.-.': 'Ц', '---.': 'Ч', '----': 'Ш', '--.-': 'Щ', '.--.-.': 'Ъ', '-.--': 'Ы', '-..-': 'Ь',
        '...-...': 'Э', '..--': 'Ю', '.-.-': 'Я'
    }
    m = s.split()

    for c in m:

        for sim in c:

            if sim == '-':
                time.sleep(0.2)
                draw_rect(win, w, h)
                w += 25
                sound(0.6)

            elif sim == '.':
                time.sleep(0.2)
                draw_point(win, w, h)
                w += 25
                sound(0.2)
            else:
                continue

        write_tex(win, tw, th, d.get(c))
        tw += 30

    win.getMouse()

main()
