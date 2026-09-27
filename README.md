# 🏋️ AI Gym Trainer

An intelligent real-time gym coach powered by **MediaPipe Pose Detection** and **LLM-based voice coaching**. The app detects your body posture via webcam, counts reps, tracks form, and gives live voice feedback — just like having a personal trainer!

## 🚀 Features

- 🎯 Real-time pose detection using **MediaPipe Pose Landmarker**
- 💪 Supports 5 exercises: **Bicep Curls, Push-ups, Squats, Lunges, Shoulder Press**
- 🗣️ Live **voice coaching** via LLM + Text-to-Speech pipeline
- 📊 Rep counting & form correction feedback
- 🔐 User authentication system
- 💾 Session persistence & workout history
- 🎨 Clean Streamlit UI with custom styling

## 🛠️ Tech Stack

| Component | Technology |
|-----------|-----------|
| Pose Detection | MediaPipe Pose Landmarker |
| UI | Streamlit |
| Voice Coaching | LLM + gTTS |
| Language | Python 3.12 |

## 📁 Project Structure

```
Ai_Gym_Trainer/
├── core/               # Base exercise classes
├── detectors/          # Per-exercise pose detectors
│   ├── biceps_curl.py
│   ├── pushup.py
│   ├── squat.py
│   ├── lunges.py
│   └── shoulder_press.py
├── services/
│   ├── auth/           # Login system
│   ├── coaching/       # LLM + TTS pipeline
│   ├── tracking/       # Metrics & rep counting
│   ├── vision/         # Video processing
│   ├── ui/             # Style loader
│   └── persistence/    # Workout history
├── ml_models/          # MediaPipe model (not tracked)
├── static/             # CSS & fonts
└── main.py             # Entry point
```

## ⚙️ Setup

```bash
# 1. Clone the repo
git clone https://github.com/AbdullahSaif-194/ai-gym-trainer.git
cd ai-gym-trainer

# 2. Create virtual environment
python -m venv .venv
.venv\Scripts\activate

# 3. Install dependencies
pip install -r tutorial_info/requirements.txt

# 4. Add your API key
cp .env.example .env
# Edit .env and add your GOOGLE_API_KEY

# 5. Run the app
streamlit run main.py
```

## 📋 Requirements

See [`tutorial_info/requirements.txt`](tutorial_info/requirements.txt)

> **Note:** The MediaPipe `.task` model file must be downloaded separately and placed in `ml_models/`.
