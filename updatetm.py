import sublime, sublime_plugin
import time, datetime
from xml.etree import ElementTree as ET

class UpdatetmCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		meta_info = sublime.packages_path() + '/User/Default.tmPreferences'
		tree = ET.parse(meta_info)
		eles = tree.getroot().find('dict').find('dict').find('array').findall('dict')
		timestamp = "[%s]\t" % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))
		for ele in eles:
			kvs = ele.getchildren()
			if kvs[1].text == 'TM_YEAR':
				if kvs[3].text != y:
					kvs[3].text = y
					continue
			elif kvs[1].text == 'DATE':
				if kvs[3].text != timestamp:
					kvs[3].text = timestamp
					continue

		tree.write(meta_info)

	