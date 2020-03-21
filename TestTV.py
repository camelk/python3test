#-*- coding: UTF-8 -*- 
from TV import TV

def main():
	tv1 = TV()
	tv1.turnOn()
	tv1.setChannel(30)
	tv1.setVolume(3)
	
	tv2 = TV()
	tv2.turnOn()
	tv2.channelUp()
	tv2.channelUp()
	tv2.volumeUp()
	
	print("tv1 channel: ", tv1.getChannel(), "Volume:", tv1.getVolume())
	print("tv2 channel: ", tv2.getChannel(), "Volume:", tv2.getVolume())
	
main()
	
