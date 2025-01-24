from abc import ABC, abstractmethod

class AbstractClass(ABC):
    @abstractmethod
    def update_entity(self,data, table_name):
        pass

    def delete_entity(self,data, table_name):
        pass

    def display_entity(self,data, table_name):
        pass

    def insert_entity(self, data, table_name):
        pass