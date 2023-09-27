import pymongo
# client 
def connectDatabase(obj):
    # Connect to the MongoDB server
    client = pymongo.MongoClient("mongodb://localhost:27017/")  # Replace with your MongoDB connection URI

    # Create or access a database
    db = client["file_ip_database"]  # Replace with your database name

    # Create a collection (similar to a table in relational databases)
    collection = db["file_ip_collection"]  # Replace with your collection name

    # Define a document (a record in MongoDB) with filename and IP address fields
    # obj = {"filename": "file1.txt", "ip_address": "192.168.1.1"}
    # document2 = {"filename": "file2.txt", "ip_address": "192.168.1.2"}

    # Insert documents into the collection
    collection.insert_one(obj)

    # Close the MongoDB connection
    client.close()



