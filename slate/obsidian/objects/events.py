"""
Copyright (c) 2020-present Axelancerr

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from __future__ import annotations

from typing import Any

from ...objects.enums import ErrorSeverity, EventType, TrackEndReason


__all__ = ['ObsidianBaseEvent', 'ObsidianTrackStart', 'ObsidianTrackEnd', 'ObsidianTrackStuck', 'ObsidianTrackException', 'ObsidianWebsocketOpen', 'ObsidianWebsocketClosed']


class ObsidianBaseEvent:

    __slots__ = ['_type', '_guild_id']

    def __init__(self, data: dict[str, Any]) -> None:

        self._type: EventType = EventType(data['type'])
        self._guild_id: int = int(data['guild_id'])

    def __repr__(self) -> str:
        return f'<slate.ObsidianBaseEvent guild_id=\'{self.guild_id}\'>'

    #

    @property
    def type(self) -> EventType:
        return self._type

    @property
    def guild_id(self) -> int:
        return self._guild_id

    #


class ObsidianTrackStart(ObsidianBaseEvent):

    __slots__ = ['_type', '_guild_id', '_track_id']

    def __init__(self, data: dict[str, Any]) -> None:
        super().__init__(data)

        self._track_id: str = data['track']

    def __repr__(self) -> str:
        return f'<slate.ObsidianTrackStart guild_id=\'{self.guild_id}\' track_id=\'{self.track_id}\'>'

    #

    @property
    def track_id(self) -> str:
        return self._track_id


class ObsidianTrackEnd(ObsidianBaseEvent):

    __slots__ = ['_type', '_guild_id', '_track_id', '_reason']

    def __init__(self, data: dict[str, Any]) -> None:
        super().__init__(data)

        self._track_id: str = data['track']

        self._reason: TrackEndReason = TrackEndReason(data['reason'])

    def __repr__(self) -> str:
        return f'<slate.ObsidianTrackEnd guild_id=\'{self.guild_id}\' track_id=\'{self.track_id}\' reason={self.reason}>'

    #

    @property
    def track_id(self) -> str:
        return self._track_id

    @property
    def reason(self) -> TrackEndReason:
        return self._reason


class ObsidianTrackStuck(ObsidianBaseEvent):

    __slots__ = ['_type', '_guild_id', '_track_id', '_threshold_ms']

    def __init__(self, data: dict[str, Any]) -> None:
        super().__init__(data)

        self._track_id: str = data['track']

        self._threshold_ms: int = data['threshold_ms']

    def __repr__(self) -> str:
        return f'<slate.ObsidianTrackStuck guild_id=\'{self.guild_id}\' track_id=\'{self.track_id}\' threshold_ms={self.threshold_ms}>'

    #

    @property
    def track_id(self) -> str:
        return self._track_id

    @property
    def threshold_ms(self) -> int:
        return self._threshold_ms


class ObsidianTrackException(ObsidianBaseEvent):

    __slots__ = ['_type', '_guild_id', '_track_id', '_message', '_cause', '_severity']

    def __init__(self, data: dict[str, Any]) -> None:
        super().__init__(data)

        self._track_id: str = data['track']

        exception: dict[str, Any] = data['exception']
        self._message: str = exception['message']
        self._cause: str = exception['cause']
        self._severity: ErrorSeverity = ErrorSeverity(data['severity'])

    def __repr__(self) -> str:
        return f'<slate.ObsidianTrackException guild_id=\'{self.guild_id}\' track_id=\'{self.track_id}\' severity=\'{self.severity}\' cause=\'{self.cause}\' message=\'{self.message}\'>'

    #

    @property
    def track_id(self) -> str:
        return self._track_id

    @property
    def message(self) -> str:
        return self._message

    @property
    def cause(self) -> str:
        return self._cause

    @property
    def severity(self) -> ErrorSeverity:
        return self._severity


class ObsidianWebsocketOpen(ObsidianBaseEvent):

    __slots__ = ['_type', '_guild_id', '_target', '_ssrc']

    def __init__(self, data: dict[str, Any]) -> None:
        super().__init__(data)

        self._target: str = data['target']
        self._ssrc: int = data['ssrc']

    def __repr__(self) -> str:
        return f'<slate.ObsidianWebsocketOpen>'

    #

    @property
    def target(self) -> str:
        return self._target

    @property
    def ssrc(self) -> int:
        return self._ssrc


class ObsidianWebsocketClosed(ObsidianBaseEvent):

    __slots__ = ['_type', '_guild_id', '_code', '_reason', '_by_remote']

    def __init__(self, data: dict[str, Any]) -> None:
        super().__init__(data)

        self._code: int = data['code']
        self._reason: str = data['reason']
        self._by_remote: bool = data['by_remote']

    def __repr__(self) -> str:
        return f'<slate.ObsidianWebsocketOpen>'

    #

    @property
    def code(self) -> int:
        return self._code

    @property
    def reason(self) -> str:
        return self._reason

    @property
    def by_remote(self) -> bool:
        return self._by_remote
