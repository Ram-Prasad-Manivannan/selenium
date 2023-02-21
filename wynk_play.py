import cv2
import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv

import imageio_ffmpeg
import pygame.camera

import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# loading driver
driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 20)

# loading URL
driver.get("https://wynk.in/music")
time.sleep(2)
assert driver.title == "Free Music Online: Play & Download MP3 Songs | Wynk Music"

# Hindi playlist selection
driver.find_element(By.LINK_TEXT,"New Hindi Songs").click()
ele = wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Play Songs')]")))
ele.click()

# list of songs in playlist
songs = driver.find_elements(By.XPATH,"//div[@tabindex]")
num = len(songs)
print(num)
for i in range(1, num+1):
    # elem = driver.find_element(By.XPATH,f"//div[@tabindex={i}]/div/div[3]/div/div[1]/a")
    # print(elem.get_attribute("title"))
    elem = driver.find_element(By.XPATH,f"//div[@tabindex={i}]//div/a[@title]")
    print(f"Iterations {i} -:- ",elem.text)

# # Sampling frequency
# freq = 44100

# # Recording duration
# duration = 120

# # Start recorder with the given values of duration and sample frequency
# recording = sd.rec(int(duration * freq), samplerate=freq, channels=2)

# # Record audio for the given number of seconds
# sd.wait()

# # This will convert the NumPy array to an audio
# # file with the given sampling frequency
# write("recording0.wav", freq, recording)

# # Convert the NumPy array to audio file
# wv.write("recording1.wav", recording, freq, sampwidth=2)

# ScreenShot Camera operation
pygame.camera.init()
camlist = pygame.camera.list_cameras()
cam = pygame.camera.Camera(camlist[0], (640, 480))
cam.start()
image = cam.get_image()
pygame.image.save(image, "Self2.jpg")

from subprocess import Popen
from subprocess import call

cmd = 'ffmpeg -y -rtbufsize 2000M -f dshow  -i video="screen-capture-recorder" -s 1920x1080 -b:v 512k -r 20 -vcodec libx264 test.avi'


def terminate(process):
    if process.poll() is None:
        call('taskkill /F /T /PID ' + str(process.pid))


videoRecording = Popen(cmd)      # start recording
terminate(videoRecording)        # terminates recording
