�
    5Z@g�  �                   �"  � S SK JrJrJrJrJr  S SKJr  S SKJ	r	  S SK
Jr  S SKJrJr  S SKJr  \" 5       r\R%                  S5      \" S5      \" \	5      4S	\S
\4S jj5       r\R)                  S5      \" S5      \" \	5      4S\S
\4S jj5       rg)�    )�	APIRouter�File�
UploadFile�Depends�Query)�Session)�get_db��search_documents)�upload_to_s3�parse_document_content)�Documentz/upload/.�file�dbc              �   �  #   � [        U 5      I S h  v�N n[        U 5      I S h  v�N n[        U R                  X#S9nUR	                  U5        UR                  5         UR                  U5        SUR                  S.$  Nl N[7f)N)�title�filename�contentzFile uploaded successfully)�message�document_id)r   r   r   r   �add�commit�refresh�id)r   r   �s3_urlr   �new_docs        �I/Users/rishabhkamal/Desktop/fullstack rag/backend/app/routes/documents.py�upload_documentr   
   sj   � � �  ��%�%�F�*�4�0�0�G� �T�]�]�V�M�G��F�F�7�O��I�I�K��J�J�w��3�G�J�J�O�O� &�0�s    �B�A>�B�B �AB� Bz/search/�queryc                 �   � [        U 5      nU$ )Nr
   )r   r   �resultss      r   �searchr"      s   � ��u�%�G��N�    N)�fastapir   r   r   r   r   �sqlalchemy.ormr   �app.models.databaser	   �app.services.search_servicer   �app.services.storage_servicer   r   �app.models.documentr   �router�postr   �get�strr"   � r#   r   �<module>r/      s�   �� ?� ?� "� &� 8� M� (�	������Z��-1�#�Y�g�f�o� P�
� P�G� P� �P� ���J���c�
�'�&�/� �#� �� � �r#   