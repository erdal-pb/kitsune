from django.utils.translation import ugettext_lazy as _lazy


WHERE_WIKI = 1
WHERE_SUPPORT = 2
WHERE_BASIC = WHERE_WIKI | WHERE_SUPPORT
WHERE_DISCUSSION = 4

HIGHLIGHT_TAG = "strong"
SNIPPET_LENGTH = 500

NO_MATCH = _lazy("No pages matched the search criteria")

default_app_config = "kitsune.search.apps.SearchConfig"
