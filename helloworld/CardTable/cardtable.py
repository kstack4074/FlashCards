from Dynamo.dynamo import DynamoTable


class CardTable(DynamoTable):
    def __init__(self):
        self.table = DynamoTable("Cards")

    def getCard(self, topic):
        return self.table.getItems()