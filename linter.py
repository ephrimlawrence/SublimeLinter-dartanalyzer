from SublimeLinter.lint import Linter
import logging


logger = logging.getLogger('SublimeLinter.plugins.dartanalyzer')


class DartAnalyzer(Linter):
    cmd = ('dartanalyzer', '--options', '~/analysis_options.yaml', '.')

    # TODO: improve message group
    regex = r"^Analyzing|\d+|\s+((?P<warning>lint)|(?P<error>error))\s.\s(?P<message>[\w\s\w'].*)\sat\s([\w\|]+.dart:(?P<line>\d+):(?P<col>\d+))"

    multiline = False
    defaults = {
        'selector': 'source.dart'
    }
