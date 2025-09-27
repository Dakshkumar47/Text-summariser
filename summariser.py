import networkx as nx
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.tokenize import sent_tokenize

class summariser_class:
    def __init__(self):
        print("hey welcome to the free tool for summarising documents")
        




    def extractive_summariser(self):

        self.input_str=input("please enter the path of file or text ")

        if "/" in self.input_str:
            self.path=self.input_str
            with open(self.path,'r') as file:
                data=file.readlines()
                self.text="".join([line.strip() for line in data])
        else:
            self.text=self.input_str.lower()
        sentences=[sentence.strip() for sentence in sent_tokenize(self.text)]

        vectoriser=TfidfVectorizer(stop_words='english')
        vector_matrix=vectoriser.fit_transform(sentences)

        similarity_matrix=cosine_similarity(vector_matrix)

        graph = nx.Graph()
        num_sentences = similarity_matrix.shape[0]

        # Add nodes (sentences) to the graph
        for i in range(num_sentences):
            graph.add_node(i)

        # Add edges based on similarity (e.g., if similarity > threshold)
        # A common approach for TextRank is to add edges for all pairs
        # and use the similarity as edge weights.
        for i in range(num_sentences):
            for j in range(i + 1, num_sentences):
                if similarity_matrix[i, j] > 0: # Only add edge if there's some similarity
                    graph.add_edge(i, j, weight=similarity_matrix[i, j])



        scores=nx.pagerank(graph,weight='weight')
        # Sorting by values (descending order)
        sorted_scores = dict(sorted(scores.items(), key=lambda item: item[1], reverse=True))

        print("-"*30)
        self.__summary=''
        iter=0
        for idx in sorted_scores.keys():
            self.__summary += sentences[idx]
            iter +=1
            if iter ==len(sentences)//3:
                break
        

        return self.__summary
    


summariser = summariser_class()
summary = summariser.extractive_summariser()

print(summary)

