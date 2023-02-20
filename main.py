import lib
import time
from os.path import exists
import adafruit_dht
from subprocess import run

# Some variables
DHT = adafruit_dht.DHT22(15)
Today = time.localtime()
Path = "./spreadsheets/" + str(Today.tm_mday) + "-" + str(Today.tm_mon) + "-" + str(Today.tm_year) + ".xlsx"
Today = str(Today.tm_mday) + "/" + str(Today.tm_mon) + "/" + str(Today.tm_year)

if exists(Path) is False:
    lib.init()
    run("./links.sh")

lib.write(lib.CurrentTime(), DHT.temperature, DHT.humidity)

# Generate graph
lib.Graph()
lib.echo("temp", DHT.temperature)
lib.echo("humid", DHT.humidity)
print("Noted!")
time.sleep(600)
