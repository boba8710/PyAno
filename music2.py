import audiere
import time
import numpy
import threading

def setTempo(inVal):
	global tempo
	tempo = inVal
def playNote(note, inTime):
	tones[note].play()
	time.sleep(length(inTime))
	tones[note].stop()
def playChord(noteArray, inTime):
	for note in noteArray:
		tones[note].play()
	time.sleep(length(inTime))
	for note in noteArray:
		tones[note].stop()
def playMajorChord(root, inTime):
	baseFreq = notes[root]
	startingPoint = 0
	noteArray = [root]
	for i in range(0,len(intervals)):
		if intervals[i] == baseFreq:
			startingPoint = i
			break
	for key in notes:
		if notes[key] == intervals[startingPoint + 4]:
			noteArray.append(key)
		if notes[key] == intervals[startingPoint + 7]:
			noteArray.append(key)
	playChord(noteArray, inTime)
def playMinorChord(root, inTime):
	baseFreq = notes[root]
	startingPoint = 0
	noteArray = [root]
	for i in range(0,len(intervals)):
		if intervals[i] == baseFreq:
			startingPoint = i
			break
	for key in notes:
		if notes[key] == intervals[startingPoint + 3]:
			noteArray.append(key)
		if notes[key] == intervals[startingPoint + 7]:
			noteArray.append(key)
	playChord(noteArray, inTime)
def playDiminishedChord(root, inTime):
	baseFreq = notes[root]
	startingPoint = 0
	noteArray = [root]
	for i in range(0,len(intervals)):
		if intervals[i] == baseFreq:
			startingPoint = i
			break
	for key in notes:
		if notes[key] == intervals[startingPoint + 3]:
			noteArray.append(key)
		if notes[key] == intervals[startingPoint + 6]:
			noteArray.append(key)
	playChord(noteArray, inTime)
def playSuspendedChord(root, inTime):
	baseFreq = notes[root]
	startingPoint = 0
	noteArray = [root]
	for i in range(0,len(intervals)):
		if intervals[i] == baseFreq:
			startingPoint = i
			break
	for key in notes:
		if notes[key] == intervals[startingPoint + 5]:
			noteArray.append(key)
		if notes[key] == intervals[startingPoint + 7]:
			noteArray.append(key)
	playChord(noteArray, inTime)
def playOCChord(root, inTime):
	baseFreq = notes[root]
	startingPoint = 0
	noteArray = [root]
	for i in range(0,len(intervals)):
		if intervals[i] == baseFreq:
			startingPoint = i
			break
	for key in notes:
		if notes[key] == intervals[startingPoint + 2]:
			noteArray.append(key)
		if notes[key] == intervals[startingPoint + 7]:
			noteArray.append(key)
	playChord(noteArray, inTime)
def playASMChord(root, inTime):
	baseFreq = notes[root]
	startingPoint = 0
	noteArray = [root]
	for i in range(0,len(intervals)):
		if intervals[i] == baseFreq:
			startingPoint = i
			break
	for key in notes:
		if notes[key] == intervals[startingPoint + 5]:
			noteArray.append(key)
		if notes[key] == intervals[startingPoint + 8]:
			noteArray.append(key)
	playChord(noteArray, inTime)
def playPowerChord(root, inTime):
	baseFreq = notes[root]
	startingPoint = 0
	noteArray = [root]
	for i in range(0,len(intervals)):
		if intervals[i] == baseFreq:
			startingPoint = i
			break
	for key in notes:
		if notes[key] == intervals[startingPoint + 5]:
			noteArray.append(key)
		if notes[key] == intervals[startingPoint + 9]:
			noteArray.append(key)
	playChord(noteArray, inTime)
def rest(beats):
	time.sleep(length(beats))
def length(inInt):
	return tempo/inInt
def playIntervalChord(inArr, inTime):
	baseFreq = notes[inArr[0]]
	noteArray = [inArr[0]]
	inArr = inArr[1:]
	startingPoint = 0
	for i in range(0,len(intervals)):
		if intervals[i] == baseFreq:
			startingPoint = i
			break
	for i in inArr:
		for key in notes:
			if notes[key] == intervals[startingPoint + i]:
				noteArray.append(key)
	playChord(noteArray, inTime)
def playMajorScale(root, inTime):
	baseFreq = notes[root]
	startingPoint = 0
	noteArray = [root]
	for i in range(0,len(intervals)):
		if intervals[i] == baseFreq:
			startingPoint = i
			break
	
	for key in notes:
		if notes[key] == intervals[startingPoint + 2]:
			noteArray.append(key)
			break
	for key in notes:
		if notes[key] == intervals[startingPoint + 4]:
			noteArray.append(key)
			break
	for key in notes:
		if notes[key] == intervals[startingPoint + 5]:
			noteArray.append(key)
			break
	for key in notes:
		if notes[key] == intervals[startingPoint + 7]:
			noteArray.append(key)
			break
	for key in notes:
		if notes[key] == intervals[startingPoint + 9]:
			noteArray.append(key)
			break
	for key in notes:
		if notes[key] == intervals[startingPoint + 11]:
			noteArray.append(key)
			break
	for key in notes:
		if notes[key] == intervals[startingPoint + 12]:
			noteArray.append(key)
			break
	for key in notes:
		if notes[key] == intervals[startingPoint + 14]:
			noteArray.append(key)
			break
	for i in noteArray[::-1][1:]:
		noteArray.append(i)
	for n in range(0,len(noteArray)):
		playNote(noteArray[n], inTime)
def asynchPhrase(inPhrase):
	thr = threading.Thread(target = inPhrase, args = (), kwargs = {})
	thr.start()
def asynch(inCommand,args0,args1):
	thr = threading.Thread(target = inCommand, args=(args0,args1),kwargs={})
	thr.start()
intervals = []
intervalTones = []
tones = {}
notes = {"F8":5587.65,"E8":5274.04,"Ds8":4978.03, "Eb8":4978.03,"D8":4698.64,"Cs8":4434.92, "Db8":4434.92,"C8":4186.01,"B7":3951.07,"As7":3729.31, "Bb7":3729.31,"A7":3520,"Gs7":3322.44, "Ab7":3322.44,"G7":3135.96,"Fs7":2959.96, "Gb7":2959.96,"F7":2793.83,"E7":2637.02,"Ds7":2489.02, "Eb7":2489.02,"D7":2349.32,"Cs7":2217.46, "Db7":2217.46,"C7":2093,"B6":1975.53,"As6":1864.66, "Bb6":1864.66,"A6":1760,"Gs6":1661.22, "Ab6":1661.22,"G6":1567.98,"Fs6":1479.98, "Gb6":1479.98,"F6":1396.91,"E6":1318.51,"Ds6":1244.51, "Eb6":1244.51,"D6":1174.66,"Cs6":1108.73, "Db6":1108.73,"C6":1046.5,"B5":987.767,"As5":932.328, "Bb5":932.328,"A5":880,"Gs5":830.609, "Ab5":830.609,"G5":783.991,"Fs5":739.989, "Gb5":739.989,"F5":698.456,"E5":659.255,"Ds5":622.254, "Eb5":622.254,"D5":587.33,"Cs5":554.365, "Db5":554.365,"C5":523.251,"B4":493.883,"As4":466.164, "Bb4":466.164,"A4":440,"Gs4":415.305, "Ab4":415.305,"G4":391.995,"Fs4":369.994, "Gb4":369.994,"F4":349.228,"E4":329.628,"Ds4":311.127, "Eb4":311.127,"D4":293.665,"Cs4":277.183, "Db4":277.183,"C4":261.626,"B3":246.942,"As3":233.082, "Bb3":233.082,"A3":220,"Gs3":207.652, "Ab3":207.652,"G3":195.998,"Fs3":184.997, "Gb3":184.997,"F3":174.614,"E3":164.814,"Ds3":155.563, "Eb3":155.563,"D3":146.832,"Cs3":138.591, "Db3":138.591,"C3":130.813,"B2":123.471,"As2":116.541, "Bb2":116.541,"A2":110,"Gs2":103.826, "Ab2":103.826,"G2":97.9989,"Fs2":92.4986, "Gb2":92.4986,"F2":87.3071,"E2":82.4069,"Ds2":77.7817, "Eb2":77.7817,"D2":73.4162,"Cs2":69.2957, "Db2":69.2957,"C2":65.4064,"B1":61.7354,"As1":58.2705,"Bb1":58.2705,"A1":55,"Gs1":51.9131, "Ab1":51.9131,"G1":48.9994,"Fs1":46.2493, "Gb1":46.2493,"F1":43.6535,"E1":41.2034,"Ds1":38.8909, "Eb1":38.8909,"D1":36.7081,"Cs1":34.6478, "Db1":34.6478,"C1":32.7032,"B0":30.8677,"As0":29.1352, "Bb0":29.1352,"A0":27.5,"Gs0":25.9565, "Ab0":25.9565,"G0":24.4997,"Fs0":23.1247, "Gb0":23.1247,"F0":21.8268,"E0":20.6017,"Ds0":19.4454, "Eb0":19.4454,"D0":18.354,"Cs0":17.3239, "Db0":17.3239,"C0":16.3516}
d = audiere.open_device()
global tempo
tempo = 2.40
print("Initializing Tones...")

for key in notes:
	tones[key] = d.create_tone(notes[key])
usedList=[]
for key in notes:
	flag = False
	for i in usedList:
		if i == notes[key]:
			flag = True
	if not flag:
		intervals.append(notes[key])
	usedList.append(notes[key])
intervals = sorted(intervals)
print("Done")
'''
Instructions/Shitty Documentation:

playNote(String note, float length): Play a note (i.e. A4, Bb0, Cs8) 

for a duration (With whole note = 1, half = 2, quarter = 4 etc)
playChord(String[] noteArray, float length): Play a chord for a duration

playMajorChord(String root): Play a major chord with root "root". 

Minor, Suspended, Augmented Suspended Minor (ASM), OverCorrected (OC), 

and Power Chord (Power) work in exactly the same way.

use the rest(float length) command to rest for length beats

The tempo is presented in seconds per measure and is default 2.40. You can 

change that with the setTempo(float Tempo) command.

Another neat thing you can do is set up entire asynchronous phrases

but that will require some thinking and elbow grease.

Effecively, just define a method with a bunch of fun instructions in it and spin it up

as an asynchronous thread. You can get very complex melody this way.
'''
'''
#YOUR MUSIC GOES HERE  :)

#Toccata and Fugue in D minor
#J.S.B.
#Arr for script by Zaine Wilson
setTempo(4.80)

playNote("A4",32)
playNote("G4",32)
playNote("A4",4)
rest(8)
playNote("G4",32)
playNote("F4",32)
playNote("E4",32)
playNote("D4",32)
playNote("Db4",8)
playNote("D4",4)
rest(8)
playNote("A4",32)
playNote("G4",32)
playNote("A4",8)
rest(8)
playNote("E4", 16)
playNote("F4", 16)
playNote("Db4",16)
playNote("D4",4)
rest(8)
playNote("A4",32)
playNote("G4",32)
playNote("A4",8)
rest(8)
playNote("G4",32)
playNote("F4",32)
playNote("E4",32)
playNote("D4",32)
playNote("Db4",8)
playNote("D4",4)
rest(8)
asynch(playNote,"D4",4)
playNote("D3",4)

asynch(playChord,["D4","F4","A4"],16)
playChord(["D3","F3"],16)

asynch(playChord,["D4","F4","A4"],16)
playChord(["D3","F3","A3"],16)

asynch(playChord,["D4","F4","A4","D5"],16)
playChord(["D3","F3","A3","D4"],16)

asynch(playChord,["D4","F4","A4","Db5"],2)
playChord(["D3","F3","A3","Db4"],2)

asynch(playChord,["D4","G4","A4","D5"],8)
playChord(["D3","G3","A3","D4"],8)

asynch(playChord,["D4","E4","A4","D5"],8)
playChord(["D3","E3","A3","D4"],8)

asynch(playChord,["D4","Gb4","A4","D5"],2)
playChord(["D3","Gb3","A3","D4"],2)
'''
