from .sortbase import ConditionWithSort

class TorrentNumberCondition(ConditionWithSort):
    def __init__(self, settings):
        ConditionWithSort.__init__(self, settings['action'])
        self._max_limit = settings['limit']

    def apply(self, torrents):
        ConditionWithSort.sort_torrents(self, torrents)
        if self._max_limit == 0:
            self.remove = torrents
        elif self._max_limit < len(torrents):
            self.remain = torrents[0:self._max_limit-1]
            self.remove = torrents[self._max_limit:]
        else:
            self.remain = torrents