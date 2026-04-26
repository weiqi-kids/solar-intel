"""
公司新聞爬蟲
"""

from .base import CompanyFetcher, CompanyDocument

from .array import ArrayFetcher
from .canadian_solar import CanadianSolarFetcher
from .daqo import DaqoFetcher
from .enphase import EnphaseFetcher
from .first_solar import FirstSolarFetcher
from .gcl import GclFetcher
from .ja_solar import JaSolarFetcher
from .jinko import JinkoFetcher
from .longi import LongiFetcher
from .maxeon import MaxeonFetcher
from .meyer_burger import MeyerBurgerFetcher
from .motech import MotechFetcher
from .nextracker import NextrackerFetcher
from .risen import RisenFetcher
from .solaredge import SolaredgeFetcher
from .sungrow import SungrowFetcher
from .tongwei import TongweiFetcher
from .trina import TrinaFetcher
from .xinyi_solar import XinyiSolarFetcher
from .yuan_jing import YuanJingFetcher

FETCHERS = {
    "array": ArrayFetcher,
    "canadian_solar": CanadianSolarFetcher,
    "daqo": DaqoFetcher,
    "enphase": EnphaseFetcher,
    "first_solar": FirstSolarFetcher,
    "gcl": GclFetcher,
    "ja_solar": JaSolarFetcher,
    "jinko": JinkoFetcher,
    "longi": LongiFetcher,
    "maxeon": MaxeonFetcher,
    "meyer_burger": MeyerBurgerFetcher,
    "motech": MotechFetcher,
    "nextracker": NextrackerFetcher,
    "risen": RisenFetcher,
    "solaredge": SolaredgeFetcher,
    "sungrow": SungrowFetcher,
    "tongwei": TongweiFetcher,
    "trina": TrinaFetcher,
    "xinyi_solar": XinyiSolarFetcher,
    "yuan_jing": YuanJingFetcher,
}
