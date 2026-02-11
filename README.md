# 🧠 TRO AI Content Brain

> AI-powered content intelligence system for The Real Ones (TRO) marketing agency

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

## 🎯 What Is This?

TRO AI Content Brain is your intelligent content creation assistant that learns from TRO's past campaigns, understands your brand voice, and helps generate new content ideas in authentic TRO style.

**Think of it as:** Your creative co-pilot that remembers every successful campaign, knows what works, and helps you create more winning content faster.

## ✨ Features

### 📊 Content Analysis Engine
- Analyzes tone, style, and patterns from past TRO content
- Extracts successful hooks and storytelling techniques
- Identifies what makes TRO content unique
- Generates style profiles for different clients

### 💡 AI Prompt Library
- Ready-to-use prompts for reels, captions, calendars
- Campaign strategy templates
- Hook generators and trend analyzers
- Client-specific prompt variations

### 🎨 Interactive Dashboard
- Simple web interface for content generation
- Topic-based idea generation
- Style analysis and recommendations
- Quick content templates

### 📁 Organized Content Storage
- Structured folders for reels, captions, campaigns
- Client-specific strategies
- Case studies and learnings
- Performance-tracked content

## 🚀 Quick Start

### Option 1: Use the Web Dashboard (No Coding Required)

1. Clone this repository:
   ```bash
   git clone https://github.com/Santanumalik1/TRO-AI-Content-Brain.git
   cd TRO-AI-Content-Brain
   ```

2. Open the dashboard:
   ```bash
   # On Windows
   start dashboard/index.html
   
   # On Mac
   open dashboard/index.html
   
   # On Linux
   xdg-open dashboard/index.html
   ```

3. Start generating content! Enter your topic and click the buttons.

### Option 2: Use the Python AI Engine

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the content analyzer:
   ```python
   from ai_engine.content_analyzer import ContentAnalyzer
   
   # Initialize
   analyzer = ContentAnalyzer()
   
   # Load your content
   analyzer.load_content('all')
   
   # Analyze patterns
   patterns = analyzer.analyze_patterns()
   print(patterns)
   
   # Generate ideas
   ideas = analyzer.suggest_content_ideas('social media marketing', count=10)
   for idea in ideas:
       print(idea)
   ```

### Option 3: Use AI Prompts with ChatGPT/Claude

1. Go to `/prompts/tro_prompts.md`
2. Copy the prompt template you need
3. Replace [TOPIC] with your specific topic
4. Paste into ChatGPT, Claude, or Perplexity
5. Get TRO-style content instantly!

## 📁 Repository Structure

```
TRO-AI-Content-Brain/
│
├── data/                  # Store past content samples
│   ├── reels_scripts/    # Instagram/YouTube reel scripts
│   ├── captions/         # Social media captions
│   ├── campaign_ideas/   # Campaign concepts
│   ├── client_strategies/# Client-specific approaches
│   └── case_studies/     # Successful campaign breakdowns
│
├── ai_engine/             # Python AI analysis module
│   └── content_analyzer.py   # Main content analysis engine
│
├── prompts/               # Reusable AI prompts
│   └── tro_prompts.md    # Comprehensive prompt library
│
├── dashboard/             # Web interface
│   └── index.html        # Interactive dashboard
│
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

## 💼 Daily Usage Guide

### For Santanu (Content Strategy)

**Morning Routine:**
1. Open dashboard/index.html
2. Review client needs for the day
3. Generate 5-10 content ideas per client
4. Use prompts to create detailed briefs

**When Planning Campaigns:**
1. Go to `/prompts/tro_prompts.md`
2. Use "Campaign Strategy Generator" prompt
3. Fill in client details
4. Get comprehensive campaign blueprint

**After Successful Content:**
1. Save the content in appropriate `/data` folder
2. Note what worked (hook, style, engagement)
3. Let the AI learn from your wins!

### For the TRO Team

**Need Reel Ideas?**
1. Use dashboard OR prompts/tro_prompts.md
2. Enter topic: "Nature's Cafe smoothie launch"
3. Get 10 reel concepts with hooks and CTAs

**Need Captions?**
1. Copy Instagram/LinkedIn caption prompt
2. Describe your post
3. Get TRO-voice caption ready to post

**Need Content Calendar?**
1. Use "Monthly Content Calendar" prompt
2. Specify client and theme
3. Get 30 days of content planned

## 🎓 How It Works

### The AI Learning Process

1. **Feed the Brain:** Add your successful content to `/data` folders
2. **Analyze Patterns:** The AI studies what makes TRO content unique
3. **Learn Voice:** Identifies energetic, professional, conversational tone
4. **Generate Ideas:** Creates new content matching learned patterns

### TRO Voice Elements (What the AI Learns)

- ✅ Energetic and engaging
- ✅ Professional yet friendly
- ✅ Results-focused storytelling
- ✅ Authentic and relatable
- ✅ Educational without being preachy
- ✅ Strong hooks and clear CTAs

## 🛠️ Advanced Features

### Custom Client Profiles

Create style guides for each client:

```python
analyzer = ContentAnalyzer()

# Load specific client content
client_content = analyzer.load_content('client_strategies')

# Generate client-specific style profile
profile = analyzer.generate_style_profile()
print(f"Energy Level: {profile['energy_level']}%")
print(f"Tone: {profile['conversational_tone']}%")
```

### Trend Integration

Use the "Trend Analyzer" prompt to:
- Spot trending topics
- Adapt trends to TRO voice
- Create timely, relevant content
- Position as thought leader

### Performance Tracking

In `/data`, include metrics:
```
Filename: natures-cafe_smoothie-launch_2026-01-15.txt

Performance:
- Views: 15.2K
- Engagement: 8.3%
- Shares: 234

What Worked:
- Hook: "Stop! Before you buy another smoothie..."
- Personal story angle
- Clear value proposition
```

## 📝 Best Practices

### 1. Regular Content Updates
- Add new successful content weekly
- Include performance metrics
- Note what worked and why

### 2. Customize Prompts
- Modify prompt templates for specific needs
- Create variations for different clients
- Save successful prompts back to library

### 3. Combine Tools
- Use dashboard for quick ideas
- Use prompts for detailed content
- Use Python for analysis and learning

### 4. Team Collaboration
- Share successful content in `/data`
- Update prompts based on what works
- Document client preferences

## 🤝 Contributing

This is TRO's internal tool, but team members can:

1. Add new prompts to `/prompts`
2. Improve the Python analyzer
3. Enhance the dashboard features
4. Share successful content patterns

## 📚 Resources

### Learn More
- [How to Write Better Prompts](https://www.promptingguide.ai/)
- [Content Marketing Best Practices](https://contentmarketinginstitute.com/)
- [TRO Brand Guidelines](#) (Add internal link)

### AI Tools to Use With
- ChatGPT (GPT-4 recommended)
- Claude (Anthropic)
- Perplexity AI
- Google Gemini

## ⚙️ Technical Setup (Optional)

For developers who want to extend functionality:

### Requirements
```bash
pip install -r requirements.txt
```

### Run Tests
```python
python -m pytest tests/
```

### Add New Features
1. Fork the repository
2. Create feature branch
3. Add your improvements
4. Submit pull request

## 🐛 Troubleshooting

**Dashboard not opening?**
- Make sure you're opening `index.html` in a modern browser
- Try Chrome, Firefox, or Edge
- Check browser console for errors

**Python errors?**
- Ensure Python 3.8+ is installed
- Run `pip install -r requirements.txt`
- Check file paths are correct

**Prompts not working?**
- Make sure to replace ALL [BRACKETED] placeholders
- Try different AI tools if one doesn't work well
- Adjust prompt for better results

## 📊 Version History

**v1.0.0** - February 2026
- Initial release
- Content analyzer engine
- AI prompts library
- Interactive dashboard
- Data storage structure

## 📞 Support

Questions? Issues? Ideas?
- Slack: #tro-ai-content-brain
- Email: santanu@thereالrealones.com
- GitHub Issues: [Create an issue](https://github.com/Santanumalik1/TRO-AI-Content-Brain/issues)

## 📄 License

MIT License - Feel free to use and modify for TRO's needs!

---

**Built with ❤️ by The Real Ones team**

*"Your content, amplified by AI. Your voice, authentically TRO."*
