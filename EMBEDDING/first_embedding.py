#pip install sentence-transfromers numpy
from sentence_transformers import SentenceTransformer
def main():
    model = SentenceTransformer("all-MiniLM-L6-v2")
    sentence = "I love AI"
    vector = model.encode(sentence)
    print(vector)
if __name__ == "__main__":
   main()    
    
    