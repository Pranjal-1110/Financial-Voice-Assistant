# Multi-Agent Voice-Enabled Finance Assistant

**A multi-source, multi-agent financial assistant that delivers spoken market briefs via a Streamlit app.**

---

## Overview

This project builds an advanced financial assistant that leverages multiple data sources and specialized agents to provide daily market insights through voice and text interactions.

The system integrates:

- Real-time & historical market data ingestion via APIs and web scraping  
- Vector store indexing and Retrieval-Augmented Generation (RAG)  
- Microservices orchestration with FastAPI  
- Voice interaction using open-source speech-to-text and text-to-speech pipelines  

---

## Features

- **Data Ingestion:** Fetch market data from AlphaVantage, Yahoo Finance, and scrape financial filings with Python loaders.  
- **Indexing & Retrieval:** Store and retrieve embeddings with FAISS or Pinecone.  
- **Multi-Agent Microservices:**  
  - API Agent for market data  
  - Scraping Agent for filings  
  - Retriever Agent for information retrieval  
  - Analysis Agent for quantitative insights  
  - Language Agent for narrative synthesis via LLM  
  - Voice Agent for speech input/output  
- **Voice Interaction:** Users can ask for market briefs and receive spoken responses summarizing portfolio risk exposure, earnings surprises, and market sentiment.  
- **Orchestration:** Seamless routing from voice input through analysis to voice/text output, with fallback mechanisms for clarifications.

---


