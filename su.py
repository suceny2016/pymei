import numpy as np
from ctypes import Structure, BigEndianStructure
from ctypes import c_int32, c_int16, c_float, c_uint16, c_char
from codecs import decode


class SEGYTraceHeader (BigEndianStructure):
    _fields_ = [('tracl', c_int32),
                ('tracr', c_int32),
                ('fldr', c_int32),
                ('tracf', c_int32),
                ('ep', c_int32),
                ('cdp', c_int32),
                ('cdpt', c_int32),
                ('trid', c_int16),
                ('nvs', c_int16),
                ('nhs', c_int16),
                ('duse', c_int16),
                ('offset', c_int32),
                ('gelev', c_int32),
                ('selev', c_int32),
                ('sdepth', c_int32),
                ('gdel', c_int32),
                ('sdel', c_int32),
                ('swdep', c_int32),
                ('gwdep', c_int32),
                ('scalel', c_int16),
                ('scalco', c_int16),
                ('sx', c_int32),
                ('sy', c_int32),
                ('gx', c_int32),
                ('gy', c_int32),
                ('counit', c_int16),
                ('wevel', c_int16),
                ('swevel', c_int16),
                ('sut', c_int16),
                ('gut', c_int16),
                ('sstat', c_int16),
                ('gstat', c_int16),
                ('tstat', c_int16),
                ('laga', c_int16),
                ('lagb', c_int16),
                ('delrt', c_int16),
                ('muts', c_int16),
                ('mute', c_int16),
                ('ns', c_uint16),
                ('dt', c_uint16),
                ('gain', c_int16),
                ('igc', c_int16),
                ('igi', c_int16),
                ('corr', c_int16),
                ('sfs', c_int16),
                ('sfe', c_int16),
                ('slen', c_int16),
                ('styp', c_int16),
                ('stas', c_int16),
                ('stae', c_int16),
                ('tatyp', c_int16),
                ('afilf', c_int16),
                ('afils', c_int16),
                ('nofilf', c_int16),
                ('nofils', c_int16),
                ('lcf', c_int16),
                ('hcf', c_int16),
                ('lcs', c_int16),
                ('hcs', c_int16),
                ('year', c_int16),
                ('day', c_int16),
                ('hour', c_int16),
                ('minute', c_int16),
                ('sec', c_int16),
                ('timebas', c_int16),
                ('trwf', c_int16),
                ('grnors', c_int16),
                ('grnofr', c_int16),
                ('grnlof', c_int16),
                ('gaps', c_int16),
                ('otrav', c_int16),
                ('cdpx', c_int32),
                ('cdpy', c_int32),
                ('Inline3D', c_int32),
                ('Crossline3D', c_int32),
                ('Unassigned', c_char*44)]


class BinaryHeader (BigEndianStructure):
    _fields_ = [('jobid', c_int32),
                ('lino', c_int32),
                ('reno', c_int32),
                ('ntrpt', c_int16),
                ('nart', c_int16),
                ('hdt', c_uint16),
                ('dto', c_uint16),
                ('hns', c_uint16),
                ('nso', c_uint16),
                ('format', c_int16),
                ('fold', c_int16),
                ('tsort', c_int16),
                ('vscode', c_int16),
                ('hsfs', c_int16),
                ('hsfe', c_int16),
                ('hslen', c_int16),
                ('hstyp', c_int16),
                ('schn', c_int16),
                ('hstas', c_int16),
                ('hstae', c_int16),
                ('htatyp', c_int16),
                ('hcorr', c_int16),
                ('bgrcv', c_int16),
                ('rcvm', c_int16),
                ('mfeet', c_int16),
                ('polyt', c_int16),
                ('vpol', c_int16),
                ('Unsigned340', c_char*340)]


class SUTraceHeader(Structure):
    _fields_ = [('tracl', c_int32),
                ('tracr', c_int32),
                ('fldr', c_int32),
                ('tracf', c_int32),
                ('ep', c_int32),
                ('cdp', c_int32),
                ('cdpt', c_int32),
                ('trid', c_int16),
                ('nvs', c_int16),
                ('nhs', c_int16),
                ('duse', c_int16),
                ('offset', c_int32),
                ('gelev', c_int32),
                ('selev', c_int32),
                ('sdepth', c_int32),
                ('gdel', c_int32),
                ('sdel', c_int32),
                ('swdep', c_int32),
                ('gwdep', c_int32),
                ('scalel', c_int16),
                ('scalco', c_int16),
                ('sx', c_int32),
                ('sy', c_int32),
                ('gx', c_int32),
                ('gy', c_int32),
                ('counit', c_int16),
                ('wevel', c_int16),
                ('swevel', c_int16),
                ('sut', c_int16),
                ('gut', c_int16),
                ('sstat', c_int16),
                ('gstat', c_int16),
                ('tstat', c_int16),
                ('laga', c_int16),
                ('lagb', c_int16),
                ('delrt', c_int16),
                ('muts', c_int16),
                ('mute', c_int16),
                ('ns', c_uint16),
                ('dt', c_uint16),
                ('gain', c_int16),
                ('igc', c_int16),
                ('igi', c_int16),
                ('corr', c_int16),
                ('sfs', c_int16),
                ('sfe', c_int16),
                ('slen', c_int16),
                ('styp', c_int16),
                ('stas', c_int16),
                ('stae', c_int16),
                ('tatyp', c_int16),
                ('afilf', c_int16),
                ('afils', c_int16),
                ('nofilf', c_int16),
                ('nofils', c_int16),
                ('lcf', c_int16),
                ('hcf', c_int16),
                ('lcs', c_int16),
                ('hcs', c_int16),
                ('year', c_int16),
                ('day', c_int16),
                ('hour', c_int16),
                ('minute', c_int16),
                ('sec', c_int16),
                ('timbas', c_int16),
                ('trwf', c_int16),
                ('grnors', c_int16),
                ('grnofr', c_int16),
                ('grnlof', c_int16),
                ('gaps', c_int16),
                ('otrav', c_int16),
                ('d1', c_float),
                ('f1', c_float),
                ('d2', c_float),
                ('f2', c_float),
                ('ungpow', c_float),
                ('unscale', c_float),
                ('ntr', c_int32),
                ('mark', c_int16),
                ('shortpad', c_int16),
                ('unass', c_int16 * 14)]


class SeimicData(object):
    def __init__(self, stream):
        if type(stream) == str:
            self.stream = open(stream, 'rb')
        else:
            self.stream = stream

    def __iter__(self):
        return self

    def __next__(self):
        t = self.readTrace()
        if t is not None:
            return t
        else:
            raise StopIteration


class SU(SeimicData):
    def __init__(self, stream):
        super(SU, self).__init__(stream)

    def readTrace(self):
        header = SUTraceHeader()
        size = self.stream.readinto(header)
        if size is not None and size > 0:
            tdata = (c_float * header.ns)()
            self.stream.readinto(tdata)
            data = np.ctypeslib.as_array(tdata)
            return Trace(header, data)
        else:
            return None


class SEGY(SeimicData):
    def __init__(self, stream):
        super(SEGY, self).__init__(stream)
        s = decode(self.stream.read(3200), 'cp500')
        v = [s[i:i+80] for i in range(0, len(s), 80)]
        self.textual_header = "\n".join(v)
        self.binary_header = self.stream.read(400)

    def readTrace(self):
        header = SEGYTraceHeader()
        size = self.stream.readinto(header)
        if size is not None and size > 0:
            tdata = (c_float * header.ns)()
            self.stream.readinto(tdata)
            data = np.ctypeslib.as_array(tdata)
            return Trace(header, data)
        else:
            return None


def load(path):
    if path.endswith("su"):
        return SU(path)
    else:
        return SEGY(path)


class Trace(object):
    def __init__(self, header, data):
        self.header = header
        self.data = data
        if header.scalco > 0:
            self.mult = header.scalco
        elif header.scalco < 0:
            self.mult = -1 / header.scalco
        else:
            self.mult = 1

    @property
    def gx(self):
        return self.header.gx * self.mult

    @property
    def gy(self):
        return self.header.gy * self.mult

    @property
    def sx(self):
        return self.header.sx * self.mult

    @property
    def sy(self):
        return self.header.sy * self.mult

    @property
    def mx(self):
        return (self.header.gx + self.header.sx) * 0.5 * self.mult

    @property
    def my(self):
        return (self.header.gy + self.header.sy) * 0.5 * self.mult

    @property
    def hx(self):
        return (self.header.gx - self.header.sx) * 0.5 * self.mult

    @property
    def hy(self):
        return (self.header.gy - self.header.sy) * 0.5 * self.mult

    @property
    def cdp(self):
        return self.header.cdp

    @property
    def ns(self):
        return self.header.ns

    @property
    def dt(self):
        return float(self.header.dt) / 1000000
