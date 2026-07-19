# TechStackRecommender — AI Recommendation Logic 🚀

A content-based recommendation system that maps a user's skills to the most relevant tech job roles using TF-IDF vectorization and Cosine Similarity. Built as Project 3 of the DecodeLabs AI Engineering Internship.

## Project Structure

```
TechStackRecommender/
├── notebook.ipynb    # Full recommendation pipeline — EDA, TF-IDF, similarity, visualization
├── job_roles.csv        # Dataset — 20 job roles with associated skills
└── README.md
```

## Pipeline

```
Load job_roles.csv (20 roles, 150 unique skills)
      ↓
TF-IDF Vectorization — convert skills to weighted vectors
      ↓
User inputs skills
      ↓
Cosine Similarity — compare user vector vs all role vectors
      ↓
Sort by score → return Top N matches with bar chart
```

## Dataset

Custom dataset of 20 tech job roles, each with 10 associated skills.

| Property | Value |
|----------|-------|
| Job Roles | 20 |
| Unique Skills | 150 |
| Format | CSV (job_role, skills) |

Sample roles: Data Scientist, ML Engineer, DevOps Engineer, AI Engineer, Blockchain Developer, NLP Engineer, Cloud Architect, and more.

## How It Works

### TF-IDF (Term Frequency — Inverse Document Frequency)
Converts skill tags into weighted numerical vectors. Rare, specific skills (like "Solidity" or "ROS") receive higher weights than common ones (like "Python" or "Git") that appear across many roles. This ensures specific skills drive better matches.

### Cosine Similarity
Measures the angular alignment between the user's skill vector and each job role vector. Score ranges from 0 (no match) to 1 (perfect match), independent of vector magnitude — so roles with more skills aren't unfairly favored.

```
Score 1.0  →  perfect match
Score 0.5  →  partial match  
Score 0.0  →  no overlap
```

## Sample Results

| Input Skills | Top Match | Score |
|-------------|-----------|-------|
| Python, Machine Learning, SQL | Data Scientist | 57.5% |
| Docker, Kubernetes, AWS | DevOps Engineer | 44.3% |
| JavaScript, React, Node.js | Full Stack Developer | 63.3% |
| Python, NLP, Transformers | NLP Engineer | 43.1% |
| Solidity, Ethereum, Web3 | Blockchain Developer | 60.6% |

## Key Concepts Learned

- **Content-Based Filtering** — recommends based on item attributes, not user history
- **TF-IDF Vectorization** — transforms text skills into weighted numerical vectors
- **Cosine Similarity** — measures directional alignment between vectors, invariant to magnitude
- **Cold Start Problem** — content-based filtering avoids this since it doesn't need user history
- **Vector Space Model** — all skills mapped to a shared 150-dimensional space
- **Why Euclidean distance fails** — sensitive to vector magnitude, cosine similarity is more reliable for text

## Tech Stack

| Tool | Purpose |
|------|---------|
| Python | Core language |
| scikit-learn | TF-IDF vectorization, cosine similarity |
| pandas | Data handling |
| matplotlib / seaborn | Visualization |
| Jupyter Notebook | Interactive pipeline |

## Run Locally

```bash
pip install scikit-learn pandas matplotlib seaborn jupyter
jupyter notebook recommender.ipynb
```

## Author

**Fatimah** — AI Engineering Intern @ DecodeLabs
