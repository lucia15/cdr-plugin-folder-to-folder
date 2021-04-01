import hashlib

import logging as logger
logger.basicConfig(level=logger.INFO)
import jsondb
class MetadataService:
    def get_metadata(self,file_path):
        # Create metadata json
        try:
            self.file_path=file_path
            metadata={}
            metadata["file_name"]=self.file_path.split("/")[-1]
            metadata["original_file_paths"] = self.file_path
            metadata["original_hash"] = self.get_hash(self.file_path)
            metadata["evidence_file_paths"]=None
            metadata["rebuild_status"] = None
            metadata["xml_report_status"] = None
            metadata["target_path"] = None

            return metadata
        except Exception as error:
            logger.error(f"PreProcessor: get_metadata : {error}")

    def get_hash(self,file_path):
        # Convert filecontent to hash
        try:
            f = open(file_path, mode='rb')
            file_content = f.read()
            sha256_hash = hashlib.sha256(file_content).hexdigest()
            f.close()
            return sha256_hash
        except Exception as error:
            logger.error(f"PreProcessor: get_hash : {error}")

