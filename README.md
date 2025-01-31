# Campusx Course Analysis

### Overview

This project analyzes the video views of three CampusX courses on YouTube: Machine Learning (ML), Deep Learning (DL), and Natural Language Processing (NLP). The analysis includes total views, drop-off rates, and statistical insights.

### Data Gathering

We used the **yt_dlp** package to extract video view counts from YouTube playlists.
Need for pip install:

```bash
!pip install yt-dlp
```

### Playlists:

**Machine Learning:** <a href='https://www.youtube.com/playlist?list=PLKnIA16_Rmvbr7zKYQuBfsVkjoLcJgxHH'>ML Playlist</a>

**Deep Learning:** <a href='https://www.youtube.com/playlist?list=PLKnIA16_RmvYuZauWaPlRTC54KxSNLtNn'>DL Playlist</a>

**NLP:** <a href='https://www.youtube.com/playlist?list=PLKnIA16_RmvZo7fp5kkIth6nRTeQQsjfX'>NLP Playlist</a>

### Extracted Views Data

```python
machine_learning_views = np.array([1000000, 193000, 231000, 151000, 130000, 120000, 106000, 90000, 108000,
                                  83000, 157000, 123000, 149000, 97000, 124000, 84000, 127000, 141000,
                                  96000, 134000, 112000, 78000, 156000, 151000, 111000, 116000, 125000,
                                  105000, 142000, 87000, 67000, 66000, 45000, 47000, 76000, 68000, 51000,
                                  53000, 56000, 42000, 69000, 60000, 64000, 38000, 40000, 62000, 120000,
                                  98000, 61000, 188000, 127000, 119000, 92000, 71000, 50000, 193000, 70000,
                                  52000, 30000, 72000, 78000, 94000, 53000, 35000, 32000, 43000, 28000, 25000,
                                  136000, 57000, 70000, 60000, 30000, 53000, 70000, 60000, 48000, 24000, 32000,
                                  114000, 54000, 39000, 30000, 93000, 33000, 30000, 21000, 55000, 32000, 23000,
                                  65000, 33000, 33000, 36000, 43000, 25000, 41000, 46000, 49000, 30000, 22000,
                                  39000, 103000, 60000, 45000, 73000, 36000, 32000, 26000, 45000, 64000, 54000,
                                  122000, 103000, 57000, 35000, 44000, 62000, 24000, 20000, 21000, 23000, 24000,
                                  22000, 23000, 18000, 53000, 25000, 20000, 20000, 28000, 26000, 15000])

deep_learning_views = np.array([463000, 161000, 110000, 146000, 119000, 107000, 51000, 64000, 86000, 74000,
                               91000, 77000, 41000, 96000, 103000, 64000, 41000, 37000, 71000, 51000,
                               43000, 43000, 32000, 44000, 29000, 56000, 77000, 38000, 42000, 29000,
                               62000, 62000, 40000, 44000, 34000, 34000, 28000, 54000, 46000, 122000,
                               50000, 68000, 61000, 68000, 68000, 42000, 50000, 33000, 199000, 53000,
                               51000, 34000, 90000, 32000, 77000, 87000, 63000, 40000, 46000, 39000,
                               80000, 64000, 55000, 47000, 24000, 28000, 94000, 67000, 53000, 29000,
                               92000, 45000, 63000, 32000, 24000, 22000, 29000, 33000, 24000, 28000,
                               20000, 16000, 16000, 17000])

nlp_views = np.array([242000, 119000, 126000, 107000, 91000, 70000, 67000, 82000])
```

### **Combined Analysis of Machine Learning, Deep Learning, and NLP Courses**  

---

### **1. Overall Course Engagement**  
- **Total Videos Across All Courses**: **225**  
- **Total Views Across All Courses**: **16.38M**  
- **Average Views Per Video**: **72.8K**  
- **Median Views Per Video**: **55.0K**  

---

### **2. Drop-off Rate Across Courses**  

| Course                | First Video Views | Last Video Views | Drop-off Rate (%) |
|-----------------------|-------------------|------------------|-------------------|
| Machine Learning (ML)  | **1000K**         | **15K**          | **98.5%**         |
| Deep Learning (DL)     | **463K**          | **17K**          | **96.3%**         |
| NLP                    | **242K**          | **82K**          | **66.1%**         |

<img src="Drop-off Rate Across Courses.png" alt="Drop-off Rate Across Courses" />

💡 **Key Insight:**  
The **drop-off rate is extremely high (~97-98%)** for ML and DL, while NLP retains more engagement with **only a 66.1% drop**.

---

### **3. Course Length vs Retention**  

| Course                | Total Videos | Average Views per Video | Median Views per Video | Total Views |
|-----------------------|--------------|-------------------------|------------------------|-------------|
| Machine Learning (ML)  | 133          | 767.7K                  | 570.0K                 | **10.21M**  |
| Deep Learning (DL)     | 84           | 626.8K                  | 505.0K                 | **5.26M**   |
| NLP                    | 8            | 1130.0K                 | 990.0K                 | **9040.0K** |

<img src="Views Across Courses Over Time.png" alt="Views Across Courses Over Time" />

💡 **Key Insight:**  
- **Longer courses (ML & DL) suffer high drop-offs**, while shorter courses (NLP) maintain better engagement.  
- **NLP has the highest average & median views per video**, suggesting students prefer shorter, more concise courses.

---

### **4. Views Distribution and Trends**
- **First videos of each course receive significantly higher views** than subsequent ones, indicating strong initial interest.
- **Mid-course videos experience a sharp decline**, suggesting that many students start but don’t finish.
- **Courses with fewer videos (like NLP) retain more users until the end**, reinforcing the idea that **shorter courses might be more effective**.

---

### **Final Insights and Recommendations**

✅ **Shorter courses retain more students**:  
The NLP course, with only 8 videos, has a **much lower drop-off rate (66.1%)**, whereas ML and DL lose **~97-98% of their viewers** over time.

✅ **Longer courses might benefit from segmentation**:  
Instead of one long playlist, breaking ML and DL into **smaller, targeted mini-courses** might improve retention. For example:

1. **ML Prerequisites**  
2. **Working with Data**  
3. **Data Preprocessing**  
4. **ML Regression Algorithms**  
5. **ML Classification Algorithms**  
6. **ML Clustering Algorithms**
**etc**
