# %%
# import time module, Observer, FileSystemEventHandler
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os

# %%
excutableExtensions = {'MCR', 'HPF', 'XLM', 'TMS', 'IPA', 'ARSCRIPT', 'HMS', 'PPAM', 'REG', 'EAR', 'LS', 'MS',
                        'QPX', 'XBAP', 'EX4', 'MAM', 'ROX', 'COM', 'MSP', 'BEAM', 'SPR', 'XYS', 'EBM', 'PS1',
                          'SCR', 'UDF', 'CEL', 'IPF', 'MSC', 'PWC', 'SCT', 'AWK', 'PAF', 'VBE', 'ISU', 'GS',
                            'INS', 'RBX', 'XAP', 'SCA', 'U3P', 'SHS', 'SBS', 'AC', 'OBS', 'ZL9', 'AHK', 'JOB',
                              'JAR', 'DOCM', 'FPI', 'CMD', 'ORE', 'PYC', 'JSX', 'AS', 'EHAM', 'ISP', 'ASB', 'VLX',
                                'SMM', 'CELX', 'CSH', 'HTA', 'TCP', 'FAS', 'RGS', 'PYO', 'KIX', 'PIF', 'PPSM', 'WSF',
                                  'ACTM', 'FKY', 'LNK', 'MST', 'WORKFLOW', 'EZS', 'COMMAND', 'SHB', 'RPJ', 'SCRIPT',
                                    'OTM', 'EXE', 'DMC', 'VPM', 'EBS', 'PRG', 'VB', 'ACC', 'ACR', 'CHM', 'OSX', 'IIM',
                                      'XLAM', 'INX', 'DEK', 'DLD', 'PRC', 'XLSM', 'MPX', 'PEX', 'EBS2', 'MRC', 'PLX',
                                        'DOTM', 'LO', 'XQT', 'WCM', 'POTM', 'TLB', 'WPM', 'OUT', '0XE', 'VBS', 'XLTM',
                                          'THM', 'CPL', 'KSH', 'MEL', '89K', 'FRS', 'UPX', 'NEXE', 'ECF', 'APP', 'A6P',
                                            'HAM', 'MXE', 'JSE', 'RUN', 'ES', 'AZW2', 'FXP', 'ELF', 'BAT', 'WS', 'JS', 'PVD',
                                              'SCAR', 'APK', 'VBSCRIPT', 'S2A', 'SCB', 'WPK', 'GADGET', '73K', 'URL', 'AIR', 'WIZ',
                                                'MSI', 'CRT', 'INF1', 'BTM', 'WIDGET', 'BIN', 'DXL', 'EXOPC', 'PPTM', 'COF'}


videoExtensions = set( "WEBM, MPG, MP2, MPEG, MPE, MPV, OGG, MP4, M4P, M4V, AVI, WMV, MOV, QT, FLV, SWF, AVCHD".split(', ') )
imageExtensions = set( "JPG,PNG,GIF,WEBP,TIFF,PSD,RAW,BMP,HEIF,INDD,JPEG2000,SVG,AI,EPS,PDF".split(',') )
documentExtensions = set( "DOC, DOCX, HTML, HTM, ODT, PDF, XLS, XLSX, ODS, PPT, PPTX, TXT".split(', ') )
safeExtensions = videoExtensions.union(imageExtensions).union(documentExtensions)

# %%
watchDirectory = "D:\\Downloads\\"
class OnMyWatch:
	# Set the directory on watch
	watchDirectory = "D:\\Downloads\\"
	def __init__(self):
		self.observer = Observer()

	def run(self):
		event_handler = Handler()
		self.observer.schedule(event_handler, self.watchDirectory, recursive = True)
		self.observer.start()
		try:
			while True:
				time.sleep(5)
		except:
			self.observer.stop()
			print("Observer Stopped")

		self.observer.join()


class Handler(FileSystemEventHandler):

	@staticmethod
	def on_any_event(event):
		if event.is_directory:
			return None

		elif event.event_type == 'created':
			# Event is created, you can process it now
			path = (event.src_path)
			filename = os.path.basename(path)
			extension = os.path.splitext(filename)[-1][1:].upper()
			safePath = watchDirectory + "SafeExecution"
			if(path.startswith(safePath)):# safe
				return None
			elif(extension in excutableExtensions):# unsafe area
				temp = f"ren \"{path}\" \"[BLOCKED]{filename}\""
				os.system(temp) # rename
				path = path[0:len(path)-len(filename)]+"[BLOCKED]"+filename
				emcPath = "ExecutionMaster-x64\\emc.exe"
				command = emcPath + ' ' +'set'+ ' ' + '\"' + path + "\"" + ' ' + 'deny'
				os.system(command)
			

if __name__ == '__main__':
	watch = OnMyWatch()
	watch.run()


# %%



