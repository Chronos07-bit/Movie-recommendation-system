# 🎬 Content-Based Movie Recommendation System

This project recommends movies based on **genre similarity** using content-based filtering. It was developed as part of the Capstone-I project for the Hybrid UG program at IIT Patna.

---

## 🚀 Features

- 🎯 Content-based movie recommendations (no user ratings needed)
- 🧠 TF-IDF Vectorization + Cosine Similarity
- 🔍 Genre filter dropdown to refine results
- 🌐 Interactive UI built with Streamlit
- 📊 Genre frequency chart for data insight

---

## 🗂 Dataset Used

- Source: [MovieLens Small Dataset](https://grouplens.org/datasets/movielens/)
- File: `movies.csv`
- Includes movie `title` and `genres`

---

## ⚙️ Setup Instructions

### 1️⃣ Install Dependencies

```bash
pip install streamlit pandas scikit-learn
```

### 2️⃣ Run the App

```bash
streamlit run app.py
```

Make sure `movies.csv` is in the same folder as `app.py`.

---

## 🧪 Sample Screenshot

> *(Optional: add `top_10_genres_chart.png` here if available)*

![Genre Chart](top_10_genres_chart.png)

---

## 👥 Team Contributions

| Name                   | Email                                | Contributions |
|------------------------|----------------------------------------|---------------|
| **Arka Bhattacharya** | arka_24a12res133@iitp.ac.in           | TF-IDF logic, CLI version, full report, project coordination |
| **Debabrata Bhowmik** | debabrata_24a12res213@iitp.ac.in      | Data preprocessing, genre filter |
| **Debajyoti Bhunia**  | debajyoti_24a12res214@iitp.ac.in      | Streamlit UI, dropdown integration, visualization |

📄 *See full breakdown in* `team_contributions.txt`

---

## 🧠 Learnings & Reflection

- Understood how content-based filtering works
- Gained practical experience with TF-IDF and cosine similarity
- Learned Streamlit for interactive UI development
- Improved teamwork and version control using GitHub

---

## 🔮 Future Scope

- Add collaborative filtering (user-based)
- Use NLP on movie plots/descriptions
- Deploy full app using Streamlit Cloud or Render

---

## 📚 References

- [MovieLens Dataset](https://grouplens.org/datasets/movielens/)
- [Streamlit Docs](https://streamlit.io)
- [scikit-learn Docs](https://scikit-learn.org)
- [TF-IDF Explanation](https://en.wikipedia.org/wiki/Tf%E2%80%93idf)

---

## 📎 Project Status

✅ Completed for Capstone-I Submission  
📌 Maintained by: [Arka Bhattacharya](https://github.com/Chronos07-bit)
                   [Debabrata Bhowmik](https://github.com/Debabrata1904/movie_recommendation_system)
                   [Debajyoti Bhunia ](https://github.com/debajyoticss)                   
