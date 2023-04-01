# Import necessary packages
from llama_index import GPTSimpleVectorIndex, Document, SimpleDirectoryReader
import os

os.environ['OPENAI_API_KEY'] = 'hidden'

# Loading from a directory
documents = SimpleDirectoryReader('/Users/engramarbollas/Projects/hello_llamaindex/data').load_data()

# Loading from strings, assuming you saved your data to strings text1, text2, ...
#text_list = [invoices.txt,proposals.txt,supportcalls.txt]
#documents = [Document(t) for t in text_list]
print('Loading finished ----> ',documents)
print('Loading finished type ----> ',type(documents))


# Construct a simple vector index
#index = GPTSimpleVectorIndex(documents)
index = GPTSimpleVectorIndex.from_documents(documents)
print('Index creation finished')

# Save your index to a index.json file
index.save_to_disk('index.json')
# Load the index from your saved index.json file
index = GPTSimpleVectorIndex.load_from_disk('index.json')
print('Saving index finished')

# Querying the index
response = index.query("How's Customer A invoicing and support tickets?")
print(response)