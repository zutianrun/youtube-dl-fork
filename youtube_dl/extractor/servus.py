# coding: utf-8
from __future__ import unicode_literals

from .common import InfoExtractor


class ServusIE(InfoExtractor):
    _VALID_URL = r'https?://(?:www\.)?servus\.com/tv/videos/(?P<id>aa-\w+|\d+-\d+)'
    _TEST = {
        'url': 'https://www.servus.com/tv/videos/aa-1t6vbu5pw1w12/',
        'md5': '3e1dd16775aa8d5cbef23628cfffc1f4',
        'info_dict': {
            'id': 'AA-1T6VBU5PW1W12',
            'ext': 'mp4',
            'title': r're:^Die Grünen aus Sicht des Volkes.*',
            'description': 'md5:1247204d85783afe3682644398ff2ec4',
            'thumbnail': r're:^https?://.*1080$',
        }
    }

    def _real_extract(self, url):
        video_id = self._match_id(url).upper()

        webpage = self._download_webpage(url, video_id)
        
        title = self._og_search_title(webpage)
        description = self._og_search_description(webpage)
        thumbnail = self._og_search_thumbnail(webpage)

        formats = self._extract_m3u8_formats(
            'https://stv.rbmbtnx.net/api/v1/manifests/%s.m3u8' % video_id,
            video_id, 'mp4', entry_protocol='m3u8_native', m3u8_id='hls')
        self._sort_formats(formats)

        return {
            'id': video_id,
            'title': title,
            'description': description,
            'thumbnail': thumbnail,
            'formats': formats,
        }
