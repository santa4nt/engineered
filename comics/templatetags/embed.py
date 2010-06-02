import re

from django.template.defaultfilters import stringfilter
from django import template


register = template.Library()

YOUTUBE_RE = re.compile(r"^(http://)?(www\.)?(youtube\.com/watch\?v=)?(?P<id>[A-Za-z0-9\-=_]{11})")
YOUTUBE_EMBED = """
<object width="425" height="344">
<param name="movie" value="http://www.youtube.com/v/%s"></param>
<param name="allowFullScreen" value="true"></param>
<embed src="http://www.youtube.com/v/%s" type="application/x-shockwave-flash" allowfullscreen="true" width="425" height="344"></embed>
</object>
"""


@register.filter
@stringfilter
def youtube(url):
    """Match the given URL against a YouTube regex, then generate an embeddable
    HTML snippet for that URL.

    """
    match = YOUTUBE_RE.match(url)
    if not match:
        return ''

    video_id = match.group('id')
    return YOUTUBE_EMBED % (video_id, video_id)

youtube.is_safe = True  # Don't escape HTML
