"""
RAG系统核心类 (RAG System Core Class)

实现基于ChromaDB的向量检索增强生成系统

主要功能：
1. 文档向量化存储
2. 语义相似度检索
3. 知识库管理

技术栈：
- 向量数据库: ChromaDB (本地持久化)
- Embedding模型: sentence-transformers (all-MiniLM-L6-v2)
"""

import chromadb
from sentence_transformers import SentenceTransformer
from typing import List, Dict


class RAGSystem:
    """
    检索增强生成 (RAG) 系统类

    使用 ChromaDB 作为向量数据库，sentence-transformers 作为 Embedding 模型

    Attributes:
        embedding_model: SentenceTransformer 嵌入模型实例
        chroma_client: ChromaDB 客户端实例
        collection: ChromaDB 集合，用于存储向量化的文档
    """

    def __init__(self, collection_name: str = "qsh_knowledge_base", db_path: str = "./chroma_db"):
        """
        初始化 RAG 系统

        Args:
            collection_name: ChromaDB 集合名称，默认为 "qsh_knowledge_base"
            db_path: ChromaDB 数据库存储路径，默认为 "./chroma_db"
        """
        print("[RAG] 正在初始化 RAG 系统...")

        # 加载 Embedding 模型 (CPU 友好型)
        print("[RAG] 加载 Embedding 模型: all-MiniLM-L6-v2")
        self.embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

        # 初始化 ChromaDB 客户端 (持久化存储)
        print(f"[RAG] 初始化 ChromaDB 向量数据库 (路径: {db_path})...")
        self.chroma_client = chromadb.PersistentClient(path=db_path)

        # 获取或创建集合
        self.collection = self.chroma_client.get_or_create_collection(
            name=collection_name,
            metadata={"description": "QSH 个人信息知识库"}
        )
        print(f"[RAG] 集合 '{collection_name}' 已就绪")

    def add_document(self, doc_path: str) -> int:
        """
        将文档添加到向量数据库

        Args:
            doc_path: 文档文件路径

        Returns:
            int: 成功添加的段落数量
        """
        print(f"[RAG] 正在读取文档: {doc_path}")

        # 读取文档内容
        with open(doc_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # 将文档分割成段落（按换行符分割）
        paragraphs = [p.strip() for p in content.split('\n') if p.strip()]

        print(f"[RAG] 文档包含 {len(paragraphs)} 个段落")

        # 为每个段落生成嵌入向量并存储
        for i, paragraph in enumerate(paragraphs):
            # 生成嵌入向量
            embedding = self.embedding_model.encode(paragraph).tolist()

            # 添加到 ChromaDB
            self.collection.add(
                ids=[f"doc_{i}"],
                embeddings=[embedding],
                documents=[paragraph],
                metadatas=[{"source": doc_path, "paragraph_id": i}]
            )

        print(f"[RAG] 成功将 {len(paragraphs)} 个段落向量化并存入数据库")
        return len(paragraphs)

    def query(self, question: str, n_results: int = 3) -> str:
        """
        查询知识库

        Args:
            question: 用户问题
            n_results: 返回的结果数量，默认为 3

        Returns:
            检索到的相关文档内容（拼接后的字符串）
        """
        print(f"[RAG] 正在检索: {question}")

        # 将问题向量化
        question_embedding = self.embedding_model.encode(question).tolist()

        # 在 ChromaDB 中检索
        results = self.collection.query(
            query_embeddings=[question_embedding],
            n_results=n_results
        )

        # 提取检索到的文档
        documents = results['documents'][0] if results['documents'] else []

        print(f"[RAG] 检索到 {len(documents)} 条相关记录")

        # 拼接结果
        context = "\n".join(documents)
        return context

    def clear_collection(self):
        """
        清空当前集合的所有数据
        """
        try:
            collection_name = self.collection.name
            self.chroma_client.delete_collection(collection_name)
            self.collection = self.chroma_client.create_collection(
                name=collection_name,
                metadata={"description": "QSH 个人信息知识库"}
            )
            print(f"[RAG] 集合 '{collection_name}' 已清空")
        except Exception as e:
            print(f"[RAG] 清空集合时出错: {e}")

    def get_collection_count(self) -> int:
        """
        获取集合中的文档数量

        Returns:
            int: 文档数量
        """
        return self.collection.count()
