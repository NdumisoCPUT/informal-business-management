# repositories/cash_flow_entry_repository.py

from repositories.repository import Repository
from src.cash_flow_entry import CashFlowEntry

class CashFlowEntryRepository(Repository[CashFlowEntry, int]):
    pass
