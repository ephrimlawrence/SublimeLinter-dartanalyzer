from SublimeLinter.lint import Linter
import logging


logger = logging.getLogger('SublimeLinter.plugins.dartanalyzer')


class DartAnalyzer(Linter):
    cmd = ('dartanalyzer', '--options', 'analysis_options.yaml', '.')

    regex = (
            r"(^Analyzing.*)|\s+"
            r"((?P<warning>[lh]int)|(?P<error>error))"
            r"\s.\s(?P<message>.*)"
            r":(?P<line>\d{1,})"
            r":(?P<col>\d{1})"
        )

    multiline = False
    defaults = {
        'selector': 'source.dart'
    }
