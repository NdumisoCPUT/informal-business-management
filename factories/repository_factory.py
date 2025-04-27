# factories/repository_factory.py

from repositories.inmemory.order_repository import InMemoryOrderRepository
from repositories.inmemory.inventory_item_repository import InMemoryInventoryItemRepository
from repositories.inmemory.payment_repository import InMemoryPaymentRepository
from repositories.inmemory.cash_flow_entry_repository import InMemoryCashFlowEntryRepository
from repositories.inmemory.sales_report_repository import InMemorySalesReportRepository
from repositories.inmemory.system_settings_repository import InMemorySystemSettingsRepository
from repositories.inmemory.promotional_message_repository import InMemoryPromotionalMessageRepository
from repositories.inmemory.user_account_repository import InMemoryUserAccountRepository

from repositories.filesystem.order_repository import FileSystemOrderRepository
from repositories.filesystem.inventory_item_repository import FileSystemInventoryItemRepository
from repositories.filesystem.payment_repository import FileSystemPaymentRepository
from repositories.filesystem.cash_flow_entry_repository import FileSystemCashFlowEntryRepository
from repositories.filesystem.sales_report_repository import FileSystemSalesReportRepository
from repositories.filesystem.system_settings_repository import FileSystemSystemSettingsRepository
from repositories.filesystem.promotional_message_repository import FileSystemPromotionalMessageRepository
from repositories.filesystem.user_account_repository import FileSystemUserAccountRepository

from repositories.database.order_repository import DatabaseOrderRepository
from repositories.database.inventory_item_repository import DatabaseInventoryItemRepository
from repositories.database.payment_repository import DatabasePaymentRepository
from repositories.database.cash_flow_entry_repository import DatabaseCashFlowEntryRepository
from repositories.database.sales_report_repository import DatabaseSalesReportRepository
from repositories.database.system_settings_repository import DatabaseSystemSettingsRepository
from repositories.database.promotional_message_repository import DatabasePromotionalMessageRepository
from repositories.database.user_account_repository import DatabaseUserAccountRepository

class RepositoryFactory:

    @staticmethod
    def create_order_repository(storage_type="inmemory"):
        if storage_type == "inmemory":
            return InMemoryOrderRepository()
        elif storage_type == "filesystem":
            return FileSystemOrderRepository()
        elif storage_type == "database":
            return DatabaseOrderRepository()
        raise ValueError("Invalid storage type specified for Order repository.")

    @staticmethod
    def create_inventory_item_repository(storage_type="inmemory"):
        if storage_type == "inmemory":
            return InMemoryInventoryItemRepository()
        elif storage_type == "filesystem":
            return FileSystemInventoryItemRepository()
        elif storage_type == "database":
            return DatabaseInventoryItemRepository()
        raise ValueError("Invalid storage type specified for Inventory Item repository.")

    @staticmethod
    def create_payment_repository(storage_type="inmemory"):
        if storage_type == "inmemory":
            return InMemoryPaymentRepository()
        elif storage_type == "filesystem":
            return FileSystemPaymentRepository()
        elif storage_type == "database":
            return DatabasePaymentRepository()
        raise ValueError("Invalid storage type specified for Payment repository.")

    @staticmethod
    def create_cash_flow_entry_repository(storage_type="inmemory"):
        if storage_type == "inmemory":
            return InMemoryCashFlowEntryRepository()
        elif storage_type == "filesystem":
            return FileSystemCashFlowEntryRepository()
        elif storage_type == "database":
            return DatabaseCashFlowEntryRepository()
        raise ValueError("Invalid storage type specified for Cash Flow Entry repository.")

    @staticmethod
    def create_sales_report_repository(storage_type="inmemory"):
        if storage_type == "inmemory":
            return InMemorySalesReportRepository()
        elif storage_type == "filesystem":
            return FileSystemSalesReportRepository()
        elif storage_type == "database":
            return DatabaseSalesReportRepository()
        raise ValueError("Invalid storage type specified for Sales Report repository.")

    @staticmethod
    def create_system_settings_repository(storage_type="inmemory"):
        if storage_type == "inmemory":
            return InMemorySystemSettingsRepository()
        elif storage_type == "filesystem":
            return FileSystemSystemSettingsRepository()
        elif storage_type == "database":
            return DatabaseSystemSettingsRepository()
        raise ValueError("Invalid storage type specified for System Settings repository.")

    @staticmethod
    def create_promotional_message_repository(storage_type="inmemory"):
        if storage_type == "inmemory":
            return InMemoryPromotionalMessageRepository()
        elif storage_type == "filesystem":
            return FileSystemPromotionalMessageRepository()
        elif storage_type == "database":
            return DatabasePromotionalMessageRepository()
        raise ValueError("Invalid storage type specified for Promotional Message repository.")

    @staticmethod
    def create_user_account_repository(storage_type="inmemory"):
        if storage_type == "inmemory":
            return InMemoryUserAccountRepository()
        elif storage_type == "filesystem":
            return FileSystemUserAccountRepository()
        elif storage_type == "database":
            return DatabaseUserAccountRepository()
        raise ValueError("Invalid storage type specified for User Account repository.")



