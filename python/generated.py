# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = welcome6_from_dict(json.loads(json_string))

from typing import Any, List, Optional, TypeVar, Callable, Type, cast
from enum import Enum
from uuid import UUID


T = TypeVar("T")
EnumT = TypeVar("EnumT", bound=Enum)


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def to_enum(c: Type[EnumT], x: Any) -> EnumT:
    assert isinstance(x, c)
    return x.value


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass
    assert False


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


class Partition:
    opts: str
    device: str
    fstype: str
    mountpoint: str

    def __init__(self, opts: str, device: str, fstype: str, mountpoint: str) -> None:
        self.opts = opts
        self.device = device
        self.fstype = fstype
        self.mountpoint = mountpoint

    @staticmethod
    def from_dict(obj: Any) -> 'Partition':
        assert isinstance(obj, dict)
        opts = from_str(obj.get("opts"))
        device = from_str(obj.get("device"))
        fstype = from_str(obj.get("fstype"))
        mountpoint = from_str(obj.get("mountpoint"))
        return Partition(opts, device, fstype, mountpoint)

    def to_dict(self) -> dict:
        result: dict = {}
        result["opts"] = from_str(self.opts)
        result["device"] = from_str(self.device)
        result["fstype"] = from_str(self.fstype)
        result["mountpoint"] = from_str(self.mountpoint)
        return result


class Hardware:
    cpu: str
    ram: str
    bios: str
    gp_us: List[str]
    ni_cs: List[str]
    disks: List[str]
    hostname: str
    public_ip: str
    private_ip: str
    timestamp: str
    partitions: List[Partition]

    def __init__(self, cpu: str, ram: str, bios: str, gp_us: List[str], ni_cs: List[str], disks: List[str], hostname: str, public_ip: str, private_ip: str, timestamp: str, partitions: List[Partition]) -> None:
        self.cpu = cpu
        self.ram = ram
        self.bios = bios
        self.gp_us = gp_us
        self.ni_cs = ni_cs
        self.disks = disks
        self.hostname = hostname
        self.public_ip = public_ip
        self.private_ip = private_ip
        self.timestamp = timestamp
        self.partitions = partitions

    @staticmethod
    def from_dict(obj: Any) -> 'Hardware':
        assert isinstance(obj, dict)
        cpu = from_str(obj.get("CPU"))
        ram = from_str(obj.get("RAM"))
        bios = from_str(obj.get("BIOS"))
        gp_us = from_list(from_str, obj.get("GPUs"))
        ni_cs = from_list(from_str, obj.get("NICs"))
        disks = from_list(from_str, obj.get("disks"))
        hostname = from_str(obj.get("Hostname"))
        public_ip = from_str(obj.get("PublicIP"))
        private_ip = from_str(obj.get("PrivateIP"))
        timestamp = from_str(obj.get("timestamp"))
        partitions = from_list(Partition.from_dict, obj.get("partitions"))
        return Hardware(cpu, ram, bios, gp_us, ni_cs, disks, hostname, public_ip, private_ip, timestamp, partitions)

    def to_dict(self) -> dict:
        result: dict = {}
        result["CPU"] = from_str(self.cpu)
        result["RAM"] = from_str(self.ram)
        result["BIOS"] = from_str(self.bios)
        result["GPUs"] = from_list(from_str, self.gp_us)
        result["NICs"] = from_list(from_str, self.ni_cs)
        result["disks"] = from_list(from_str, self.disks)
        result["Hostname"] = from_str(self.hostname)
        result["PublicIP"] = from_str(self.public_ip)
        result["PrivateIP"] = from_str(self.private_ip)
        result["timestamp"] = from_str(self.timestamp)
        result["partitions"] = from_list(lambda x: to_class(Partition, x), self.partitions)
        return result


class AuthConfig:
    token: str

    def __init__(self, token: str) -> None:
        self.token = token

    @staticmethod
    def from_dict(obj: Any) -> 'AuthConfig':
        assert isinstance(obj, dict)
        token = from_str(obj.get("token"))
        return AuthConfig(token)

    def to_dict(self) -> dict:
        result: dict = {}
        result["token"] = from_str(self.token)
        return result


class Plugin(Enum):
    NVCODEC = "nvcodec"
    WASAPI = "wasapi"


class Pipeline:
    plugin: Plugin
    pipeline_hash: str
    pipeline_string: str

    def __init__(self, plugin: Plugin, pipeline_hash: str, pipeline_string: str) -> None:
        self.plugin = plugin
        self.pipeline_hash = pipeline_hash
        self.pipeline_string = pipeline_string

    @staticmethod
    def from_dict(obj: Any) -> 'Pipeline':
        assert isinstance(obj, dict)
        plugin = Plugin(obj.get("Plugin"))
        pipeline_hash = from_str(obj.get("PipelineHash"))
        pipeline_string = from_str(obj.get("PipelineString"))
        return Pipeline(plugin, pipeline_hash, pipeline_string)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Plugin"] = to_enum(Plugin, self.plugin)
        result["PipelineHash"] = from_str(self.pipeline_hash)
        result["PipelineString"] = from_str(self.pipeline_string)
        return result


class Monitor:
    width: int
    height: int
    adapter: str
    pipeline: Optional[Pipeline]
    framerate: int
    is_primary: bool
    device_name: str
    monitor_name: str
    monitor_handle: int

    def __init__(self, width: int, height: int, adapter: str, pipeline: Optional[Pipeline], framerate: int, is_primary: bool, device_name: str, monitor_name: str, monitor_handle: int) -> None:
        self.width = width
        self.height = height
        self.adapter = adapter
        self.pipeline = pipeline
        self.framerate = framerate
        self.is_primary = is_primary
        self.device_name = device_name
        self.monitor_name = monitor_name
        self.monitor_handle = monitor_handle

    @staticmethod
    def from_dict(obj: Any) -> 'Monitor':
        assert isinstance(obj, dict)
        width = from_int(obj.get("Width"))
        height = from_int(obj.get("Height"))
        adapter = from_str(obj.get("Adapter"))
        pipeline = from_union([Pipeline.from_dict, from_none], obj.get("pipeline"))
        framerate = from_int(obj.get("Framerate"))
        is_primary = from_bool(obj.get("IsPrimary"))
        device_name = from_str(obj.get("DeviceName"))
        monitor_name = from_str(obj.get("MonitorName"))
        monitor_handle = from_int(obj.get("MonitorHandle"))
        return Monitor(width, height, adapter, pipeline, framerate, is_primary, device_name, monitor_name, monitor_handle)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Width"] = from_int(self.width)
        result["Height"] = from_int(self.height)
        result["Adapter"] = from_str(self.adapter)
        result["pipeline"] = from_union([lambda x: to_class(Pipeline, x), from_none], self.pipeline)
        result["Framerate"] = from_int(self.framerate)
        result["IsPrimary"] = from_bool(self.is_primary)
        result["DeviceName"] = from_str(self.device_name)
        result["MonitorName"] = from_str(self.monitor_name)
        result["MonitorHandle"] = from_int(self.monitor_handle)
        return result


class API(Enum):
    NONE = "None"
    WASAPI = "wasapi"


class DeviceID(Enum):
    NONE = "none"
    THE_001000000001_F50697_C_67_F6_4861_A965_96_AD30_A49_A41 = "{0.0.1.00000000}.{1f50697c-67f6-4861-a965-96ad30a49a41}"
    THE_0010000000082_D74_B98_01_D3_4_B92_92679_A9349_DE2_F79 = "{0.0.1.00000000}.{82d74b98-01d3-4b92-9267-9a9349de2f79}"


class Name(Enum):
    CABLE_OUTPUT_VB_AUDIO_VIRTUAL_CABLE = "CABLE Output (VB-Audio Virtual Cable)"
    MUTE_AUDIO = "Mute audio"


class Soundcard:
    api: API
    name: Name
    device_id: DeviceID
    pipeline: Optional[Pipeline]

    def __init__(self, api: API, name: Name, device_id: DeviceID, pipeline: Optional[Pipeline]) -> None:
        self.api = api
        self.name = name
        self.device_id = device_id
        self.pipeline = pipeline

    @staticmethod
    def from_dict(obj: Any) -> 'Soundcard':
        assert isinstance(obj, dict)
        api = API(obj.get("Api"))
        name = Name(obj.get("Name"))
        device_id = DeviceID(obj.get("DeviceID"))
        pipeline = from_union([Pipeline.from_dict, from_none], obj.get("pipeline"))
        return Soundcard(api, name, device_id, pipeline)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Api"] = to_enum(API, self.api)
        result["Name"] = to_enum(Name, self.name)
        result["DeviceID"] = to_enum(DeviceID, self.device_id)
        result["pipeline"] = from_union([lambda x: to_class(Pipeline, x), from_none], self.pipeline)
        return result


class MediaConfig:
    monitor: Monitor
    soundcard: Soundcard

    def __init__(self, monitor: Monitor, soundcard: Soundcard) -> None:
        self.monitor = monitor
        self.soundcard = soundcard

    @staticmethod
    def from_dict(obj: Any) -> 'MediaConfig':
        assert isinstance(obj, dict)
        monitor = Monitor.from_dict(obj.get("monitor"))
        soundcard = Soundcard.from_dict(obj.get("soundcard"))
        return MediaConfig(monitor, soundcard)

    def to_dict(self) -> dict:
        result: dict = {}
        result["monitor"] = to_class(Monitor, self.monitor)
        result["soundcard"] = to_class(Soundcard, self.soundcard)
        return result


class MatchSessionMetadata:
    pass

    def __init__(self, ) -> None:
        pass

    @staticmethod
    def from_dict(obj: Any) -> 'MatchSessionMetadata':
        assert isinstance(obj, dict)
        return MatchSessionMetadata()

    def to_dict(self) -> dict:
        result: dict = {}
        return result


class Audio:
    url: str
    path: str
    grpc_port: int

    def __init__(self, url: str, path: str, grpc_port: int) -> None:
        self.url = url
        self.path = path
        self.grpc_port = grpc_port

    @staticmethod
    def from_dict(obj: Any) -> 'Audio':
        assert isinstance(obj, dict)
        url = from_str(obj.get("URL"))
        path = from_str(obj.get("Path"))
        grpc_port = from_int(obj.get("GrpcPort"))
        return Audio(url, path, grpc_port)

    def to_dict(self) -> dict:
        result: dict = {}
        result["URL"] = from_str(self.url)
        result["Path"] = from_str(self.path)
        result["GrpcPort"] = from_int(self.grpc_port)
        return result


class SignalingConfig:
    data: Audio
    audio: Audio
    video: Audio
    host_name: str
    validation_url: str

    def __init__(self, data: Audio, audio: Audio, video: Audio, host_name: str, validation_url: str) -> None:
        self.data = data
        self.audio = audio
        self.video = video
        self.host_name = host_name
        self.validation_url = validation_url

    @staticmethod
    def from_dict(obj: Any) -> 'SignalingConfig':
        assert isinstance(obj, dict)
        data = Audio.from_dict(obj.get("Data"))
        audio = Audio.from_dict(obj.get("Audio"))
        video = Audio.from_dict(obj.get("Video"))
        host_name = from_str(obj.get("HostName"))
        validation_url = from_str(obj.get("ValidationUrl"))
        return SignalingConfig(data, audio, video, host_name, validation_url)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Data"] = to_class(Audio, self.data)
        result["Audio"] = to_class(Audio, self.audio)
        result["Video"] = to_class(Audio, self.video)
        result["HostName"] = from_str(self.host_name)
        result["ValidationUrl"] = from_str(self.validation_url)
        return result


class UserSessionMetadata:
    reference: str

    def __init__(self, reference: str) -> None:
        self.reference = reference

    @staticmethod
    def from_dict(obj: Any) -> 'UserSessionMetadata':
        assert isinstance(obj, dict)
        reference = from_str(obj.get("reference"))
        return UserSessionMetadata(reference)

    def to_dict(self) -> dict:
        result: dict = {}
        result["reference"] = from_str(self.reference)
        return result


class UserSession:
    worker_session_id: int
    user_session_id: int
    user_email: str
    last_check: str
    start_at: str
    metadata: UserSessionMetadata
    is_active: bool

    def __init__(self, worker_session_id: int, user_session_id: int, user_email: str, last_check: str, start_at: str, metadata: UserSessionMetadata, is_active: bool) -> None:
        self.worker_session_id = worker_session_id
        self.user_session_id = user_session_id
        self.user_email = user_email
        self.last_check = last_check
        self.start_at = start_at
        self.metadata = metadata
        self.is_active = is_active

    @staticmethod
    def from_dict(obj: Any) -> 'UserSession':
        assert isinstance(obj, dict)
        worker_session_id = from_int(obj.get("worker_session_id"))
        user_session_id = from_int(obj.get("user_session_id"))
        user_email = from_str(obj.get("user_email"))
        last_check = from_str(obj.get("last_check"))
        start_at = from_str(obj.get("start_at"))
        metadata = UserSessionMetadata.from_dict(obj.get("metadata"))
        is_active = from_bool(obj.get("isActive"))
        return UserSession(worker_session_id, user_session_id, user_email, last_check, start_at, metadata, is_active)

    def to_dict(self) -> dict:
        result: dict = {}
        result["worker_session_id"] = from_int(self.worker_session_id)
        result["user_session_id"] = from_int(self.user_session_id)
        result["user_email"] = from_str(self.user_email)
        result["last_check"] = from_str(self.last_check)
        result["start_at"] = from_str(self.start_at)
        result["metadata"] = to_class(UserSessionMetadata, self.metadata)
        result["isActive"] = from_bool(self.is_active)
        return result


class IceServer:
    urls: str
    username: Optional[str]
    credential: Optional[str]

    def __init__(self, urls: str, username: Optional[str], credential: Optional[str]) -> None:
        self.urls = urls
        self.username = username
        self.credential = credential

    @staticmethod
    def from_dict(obj: Any) -> 'IceServer':
        assert isinstance(obj, dict)
        urls = from_str(obj.get("urls"))
        username = from_union([from_str, from_none], obj.get("username"))
        credential = from_union([from_str, from_none], obj.get("credential"))
        return IceServer(urls, username, credential)

    def to_dict(self) -> dict:
        result: dict = {}
        result["urls"] = from_str(self.urls)
        result["username"] = from_union([from_str, from_none], self.username)
        result["credential"] = from_union([from_str, from_none], self.credential)
        return result


class WebrtcConfig:
    ice_servers: List[IceServer]

    def __init__(self, ice_servers: List[IceServer]) -> None:
        self.ice_servers = ice_servers

    @staticmethod
    def from_dict(obj: Any) -> 'WebrtcConfig':
        assert isinstance(obj, dict)
        ice_servers = from_list(IceServer.from_dict, obj.get("iceServers"))
        return WebrtcConfig(ice_servers)

    def to_dict(self) -> dict:
        result: dict = {}
        result["iceServers"] = from_list(lambda x: to_class(IceServer, x), self.ice_servers)
        return result


class MatchSession:
    worker_session_id: int
    worker_profile_id: int
    account_session_id: UUID
    webrtc_config: WebrtcConfig
    signaling_config: SignalingConfig
    media_config: MediaConfig
    auth_config: AuthConfig
    ended: bool
    start_at: str
    last_check: str
    metadata: MatchSessionMetadata
    url: str
    session_id: int
    is_active: bool
    user_session: List[UserSession]

    def __init__(self, worker_session_id: int, worker_profile_id: int, account_session_id: UUID, webrtc_config: WebrtcConfig, signaling_config: SignalingConfig, media_config: MediaConfig, auth_config: AuthConfig, ended: bool, start_at: str, last_check: str, metadata: MatchSessionMetadata, url: str, session_id: int, is_active: bool, user_session: List[UserSession]) -> None:
        self.worker_session_id = worker_session_id
        self.worker_profile_id = worker_profile_id
        self.account_session_id = account_session_id
        self.webrtc_config = webrtc_config
        self.signaling_config = signaling_config
        self.media_config = media_config
        self.auth_config = auth_config
        self.ended = ended
        self.start_at = start_at
        self.last_check = last_check
        self.metadata = metadata
        self.url = url
        self.session_id = session_id
        self.is_active = is_active
        self.user_session = user_session

    @staticmethod
    def from_dict(obj: Any) -> 'MatchSession':
        assert isinstance(obj, dict)
        worker_session_id = from_int(obj.get("worker_session_id"))
        worker_profile_id = from_int(obj.get("worker_profile_id"))
        account_session_id = UUID(obj.get("account_session_id"))
        webrtc_config = WebrtcConfig.from_dict(obj.get("webrtc_config"))
        signaling_config = SignalingConfig.from_dict(obj.get("signaling_config"))
        media_config = MediaConfig.from_dict(obj.get("media_config"))
        auth_config = AuthConfig.from_dict(obj.get("auth_config"))
        ended = from_bool(obj.get("ended"))
        start_at = from_str(obj.get("start_at"))
        last_check = from_str(obj.get("last_check"))
        metadata = MatchSessionMetadata.from_dict(obj.get("metadata"))
        url = from_str(obj.get("url"))
        session_id = from_int(obj.get("session_id"))
        is_active = from_bool(obj.get("isActive"))
        user_session = from_list(UserSession.from_dict, obj.get("user_session"))
        return MatchSession(worker_session_id, worker_profile_id, account_session_id, webrtc_config, signaling_config, media_config, auth_config, ended, start_at, last_check, metadata, url, session_id, is_active, user_session)

    def to_dict(self) -> dict:
        result: dict = {}
        result["worker_session_id"] = from_int(self.worker_session_id)
        result["worker_profile_id"] = from_int(self.worker_profile_id)
        result["account_session_id"] = str(self.account_session_id)
        result["webrtc_config"] = to_class(WebrtcConfig, self.webrtc_config)
        result["signaling_config"] = to_class(SignalingConfig, self.signaling_config)
        result["media_config"] = to_class(MediaConfig, self.media_config)
        result["auth_config"] = to_class(AuthConfig, self.auth_config)
        result["ended"] = from_bool(self.ended)
        result["start_at"] = from_str(self.start_at)
        result["last_check"] = from_str(self.last_check)
        result["metadata"] = to_class(MatchSessionMetadata, self.metadata)
        result["url"] = from_str(self.url)
        result["session_id"] = from_int(self.session_id)
        result["isActive"] = from_bool(self.is_active)
        result["user_session"] = from_list(lambda x: to_class(UserSession, x), self.user_session)
        return result


class MediaDevice:
    monitors: List[Monitor]
    timestamp: str
    soundcards: List[Soundcard]

    def __init__(self, monitors: List[Monitor], timestamp: str, soundcards: List[Soundcard]) -> None:
        self.monitors = monitors
        self.timestamp = timestamp
        self.soundcards = soundcards

    @staticmethod
    def from_dict(obj: Any) -> 'MediaDevice':
        assert isinstance(obj, dict)
        monitors = from_list(Monitor.from_dict, obj.get("monitors"))
        timestamp = from_str(obj.get("timestamp"))
        soundcards = from_list(Soundcard.from_dict, obj.get("soundcards"))
        return MediaDevice(monitors, timestamp, soundcards)

    def to_dict(self) -> dict:
        result: dict = {}
        result["monitors"] = from_list(lambda x: to_class(Monitor, x), self.monitors)
        result["timestamp"] = from_str(self.timestamp)
        result["soundcards"] = from_list(lambda x: to_class(Soundcard, x), self.soundcards)
        return result


class Active:
    proxy_profile_id: int
    worker_profile_id: int
    inserted_at: str
    last_check: str
    hardware: Hardware
    media_device: MediaDevice
    metadata: MatchSessionMetadata
    public_ip: str
    private_ip: str
    is_active: bool
    match_sessions: List[MatchSession]

    def __init__(self, proxy_profile_id: int, worker_profile_id: int, inserted_at: str, last_check: str, hardware: Hardware, media_device: MediaDevice, metadata: MatchSessionMetadata, public_ip: str, private_ip: str, is_active: bool, match_sessions: List[MatchSession]) -> None:
        self.proxy_profile_id = proxy_profile_id
        self.worker_profile_id = worker_profile_id
        self.inserted_at = inserted_at
        self.last_check = last_check
        self.hardware = hardware
        self.media_device = media_device
        self.metadata = metadata
        self.public_ip = public_ip
        self.private_ip = private_ip
        self.is_active = is_active
        self.match_sessions = match_sessions

    @staticmethod
    def from_dict(obj: Any) -> 'Active':
        assert isinstance(obj, dict)
        proxy_profile_id = from_int(obj.get("proxy_profile_id"))
        worker_profile_id = from_int(obj.get("worker_profile_id"))
        inserted_at = from_str(obj.get("inserted_at"))
        last_check = from_str(obj.get("last_check"))
        hardware = Hardware.from_dict(obj.get("hardware"))
        media_device = MediaDevice.from_dict(obj.get("media_device"))
        metadata = MatchSessionMetadata.from_dict(obj.get("metadata"))
        public_ip = from_str(obj.get("public_ip"))
        private_ip = from_str(obj.get("private_ip"))
        is_active = from_bool(obj.get("isActive"))
        match_sessions = from_list(MatchSession.from_dict, obj.get("match_sessions"))
        return Active(proxy_profile_id, worker_profile_id, inserted_at, last_check, hardware, media_device, metadata, public_ip, private_ip, is_active, match_sessions)

    def to_dict(self) -> dict:
        result: dict = {}
        result["proxy_profile_id"] = from_int(self.proxy_profile_id)
        result["worker_profile_id"] = from_int(self.worker_profile_id)
        result["inserted_at"] = from_str(self.inserted_at)
        result["last_check"] = from_str(self.last_check)
        result["hardware"] = to_class(Hardware, self.hardware)
        result["media_device"] = to_class(MediaDevice, self.media_device)
        result["metadata"] = to_class(MatchSessionMetadata, self.metadata)
        result["public_ip"] = from_str(self.public_ip)
        result["private_ip"] = from_str(self.private_ip)
        result["isActive"] = from_bool(self.is_active)
        result["match_sessions"] = from_list(lambda x: to_class(MatchSession, x), self.match_sessions)
        return result


class Welcome6:
    active: List[Active]

    def __init__(self, active: List[Active]) -> None:
        self.active = active

    @staticmethod
    def from_dict(obj: Any) -> 'Welcome6':
        assert isinstance(obj, dict)
        active = from_list(Active.from_dict, obj.get("active"))
        return Welcome6(active)

    def to_dict(self) -> dict:
        result: dict = {}
        result["active"] = from_list(lambda x: to_class(Active, x), self.active)
        return result


def welcome6_from_dict(s: Any) -> Welcome6:
    return Welcome6.from_dict(s)


def welcome6_to_dict(x: Welcome6) -> Any:
    return to_class(Welcome6, x)
