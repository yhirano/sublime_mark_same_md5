import sublime, sublime_plugin

# Mark same MD5 text
class MarkSameMd5Command(sublime_plugin.TextCommand):
	def run(self, edit):
		view = self.view
		md5Dic = {}
		edit = view.begin_edit()
		for region in view.find_all('([a-fA-F\d]{32})') :
			md5text = view.substr(region)
			v = md5Dic.get(md5text, [])
			v.append(region)
			md5Dic[md5text] = v
		duplicatedMd5 = []
		for key, value in md5Dic.iteritems():
			if len(value) >= 2:
				duplicatedMd5 += value
		view.add_regions('same_md5_regions', duplicatedMd5, 'comment')
		view.end_edit(edit)
