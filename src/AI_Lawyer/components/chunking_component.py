from pathlib import Path
from AI_Lawyer.entity.config_entity import ChunkingConfig
from AI_Lawyer.entity.config_entity import DataConfig
from AI_Lawyer.utils.logging_setup import logger
from langchain_community.document_loaders import PDFPlumberLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter



class Data_Loader:
    def __init__(self, config: DataConfig):
        self.config = config
        self.pdf_dir = Path(self.config.pdf_directory)

    def load_pdfs(self):
        documents = []

        # Iterate through all PDF files in directory
        for pdf_file in self.pdf_dir.glob("*.pdf"):
            try:
                loader = PDFPlumberLoader(str(pdf_file))
                docs = loader.load()
                documents.extend(docs)

                logger.info(f"Successfully loaded: {pdf_file}")

            except Exception as e:
                logger.error(f"Error loading file: {pdf_file} | Error: {e}")

        return documents

    def main(self):
        return self.load_pdfs()
    

class Chunking_text:
    def __init__(self, config: ChunkingConfig):
        self.config = config


    def create_chunks(self,documents):

        try:
            tex_spillter = RecursiveCharacterTextSplitter(
            chunk_size = self.config.chunk_size,
            chunk_overlap = self.config.chunk_overlap,
            add_start_index = self.config.add_start_index)

            text_chunks = tex_spillter.split_documents(documents)

            return text_chunks
        
        except Exception as e:
            logger.error(f"Error while chunking documents: {e}")
            raise e
        
    def main(self, documents):
     """
      Main method for pipeline compatibility.
     """
     return self.create_chunks(documents)
    

        


        
