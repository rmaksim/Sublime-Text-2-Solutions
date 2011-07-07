import sublime, sublime_plugin, re

class IncDecNumberCommand(sublime_plugin.TextCommand):

    def run(self, edit, delta):
        for region in self.view.sel():

            word_reg = self.view.word(region)
            if not word_reg.empty():

                # expand region if previous symbol is "-"
                prev_sym_pos = word_reg.begin() - 1
                prev_sym_reg = sublime.Region(prev_sym_pos, prev_sym_pos + 1)
                if self.view.substr(prev_sym_reg) == "-":
                    word_reg = sublime.Region(prev_sym_pos, word_reg.end())

                word = self.view.substr(word_reg)
                match = re.compile('(-*[0-9]+)([a-zA-Z%]+)?').match(word)

                if match:
                    result = int(match.group(1)) + int(delta)
                    match2 = match.group(2) if match.group(2) else ""
                    self.view.replace(edit, word_reg, str(result) + match2)
