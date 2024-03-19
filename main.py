import subprocess
import speedtest
import platform

os = platform.system()

#This function will give the user the name of the network
def network_name():
    if (os == "Darwin"):
        name = subprocess.check_output(["/System/Library/PrivateFrameworks/Apple80211.framework/Resources/airport", "-I"]).decode('utf-8').split("\n")[12]
    print("SSID: " + name.split(": ")[1])


def get_speed():
    st = speedtest.Speedtest()
    dow = st.download()
    print("Download speed: " + str(int(dow)))




while True:
    inp = input("1 - View name of the current network\n"
                "2 - View the speed of the current network\n")
    if inp == "1":
        network_name()
    if inp == "2":
        get_speed()

