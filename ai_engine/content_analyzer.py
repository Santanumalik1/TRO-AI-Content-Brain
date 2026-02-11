"""TRO AI Content Analyzer

This module analyzes TRO's past content to learn patterns, tone, and style.
It uses NLP and machine learning to understand what makes TRO content unique.
"""

import os
import json
from pathlib import Path
from typing import List, Dict, Any
import re
from collections import Counter


class ContentAnalyzer:
    """Analyzes TRO content to extract patterns and insights."""
    
    def __init__(self, data_path: str = "../data"):
        self.data_path = Path(data_path)
        self.content_database = []
        self.patterns = {}
        
    def load_content(self, content_type: str = "all") -> List[Dict[str, Any]]:
        """Load content from data folder.
        
        Args:
            content_type: Type of content to load (reels_scripts, captions, etc.)
        
        Returns:
            List of content items with metadata
        """
        content_items = []
        
        if content_type == "all":
            folders = ["reels_scripts", "captions", "campaign_ideas", 
                      "client_strategies", "case_studies"]
        else:
            folders = [content_type]
        
        for folder in folders:
            folder_path = self.data_path / folder
            if folder_path.exists():
                for file_path in folder_path.glob("*.txt"):
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content_items.append({
                            "type": folder,
                            "filename": file_path.name,
                            "content": f.read(),
                            "path": str(file_path)
                        })
        
        self.content_database.extend(content_items)
        return content_items
    
    def analyze_tone(self, text: str) -> Dict[str, Any]:
        """Analyze the tone and sentiment of content.
        
        Args:
            text: Content text to analyze
        
        Returns:
            Dictionary with tone analysis
        """
        # Simple tone analysis - can be enhanced with NLP libraries
        words = text.lower().split()
        
        # TRO-specific tone indicators
        energetic_words = ['amazing', 'incredible', 'awesome', 'wow', 
                          'exciting', 'powerful', 'game-changer']
        professional_words = ['strategy', 'solution', 'professional', 
                             'innovative', 'results', 'growth']
        conversational_words = ['you', 'your', 'let\'s', 'we', 'hey', 
                               'check', 'imagine']
        
        return {
            "energy_level": sum(1 for w in words if w in energetic_words) / len(words) * 100,
            "professionalism": sum(1 for w in words if w in professional_words) / len(words) * 100,
            "conversational": sum(1 for w in words if w in conversational_words) / len(words) * 100,
            "word_count": len(words)
        }
    
    def extract_hooks(self, content_list: List[str]) -> List[str]:
        """Extract opening hooks from content.
        
        Args:
            content_list: List of content texts
        
        Returns:
            List of opening hooks (first line/sentence)
        """
        hooks = []
        for content in content_list:
            lines = content.strip().split('\n')
            if lines:
                # Get first non-empty line
                first_line = next((line for line in lines if line.strip()), "")
                if first_line:
                    hooks.append(first_line.strip())
        return hooks
    
    def analyze_patterns(self) -> Dict[str, Any]:
        """Analyze patterns across all loaded content.
        
        Returns:
            Dictionary with pattern analysis
        """
        if not self.content_database:
            return {"error": "No content loaded"}
        
        all_content = " ".join([item["content"] for item in self.content_database])
        words = re.findall(r'\b\w+\b', all_content.lower())
        
        # Common words (excluding stopwords)
        stopwords = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 
                    'to', 'for', 'of', 'with', 'is', 'are', 'was', 'were'}
        meaningful_words = [w for w in words if w not in stopwords and len(w) > 3]
        
        word_freq = Counter(meaningful_words)
        
        self.patterns = {
            "total_content_pieces": len(self.content_database),
            "total_words": len(words),
            "unique_words": len(set(words)),
            "most_common_words": word_freq.most_common(20),
            "avg_content_length": len(words) / len(self.content_database) if self.content_database else 0
        }
        
        return self.patterns
    
    def generate_style_profile(self) -> Dict[str, Any]:
        """Generate a comprehensive style profile for TRO content.
        
        Returns:
            Dictionary with style characteristics
        """
        if not self.content_database:
            return {"error": "No content loaded. Please load content first."}
        
        # Analyze each piece
        tone_analyses = []
        for item in self.content_database:
            tone = self.analyze_tone(item["content"])
            tone_analyses.append(tone)
        
        # Average tones
        avg_energy = sum(t["energy_level"] for t in tone_analyses) / len(tone_analyses)
        avg_professional = sum(t["professionalism"] for t in tone_analyses) / len(tone_analyses)
        avg_conversational = sum(t["conversational"] for t in tone_analyses) / len(tone_analyses)
        
        return {
            "style_summary": {
                "energy_level": round(avg_energy, 2),
                "professionalism": round(avg_professional, 2),
                "conversational_tone": round(avg_conversational, 2)
            },
            "content_count": len(self.content_database),
            "average_length": round(sum(t["word_count"] for t in tone_analyses) / len(tone_analyses), 0)
        }
    
    def suggest_content_ideas(self, topic: str, count: int = 5) -> List[str]:
        """Generate content ideas based on learned patterns.
        
        Args:
            topic: Topic for content ideas
            count: Number of ideas to generate
        
        Returns:
            List of content ideas
        """
        # This is a simple template-based approach
        # Can be enhanced with GPT API or more sophisticated ML
        
        templates = [
            f"Why {topic} is changing the game for businesses",
            f"5 ways {topic} can transform your marketing strategy",
            f"The truth about {topic} that no one talks about",
            f"How TRO uses {topic} to deliver results",
            f"{topic}: Your complete guide to getting started",
            f"Stop doing {topic} wrong - here's the right way",
            f"The {topic} strategy that 10x'd our results",
            f"Behind the scenes: How we approach {topic}",
            f"{topic} trends you need to know in 2026",
            f"Real talk: Our experience with {topic}"
        ]
        
        return templates[:count]


def main():
    """Example usage of ContentAnalyzer."""
    analyzer = ContentAnalyzer()
    
    print("TRO AI Content Analyzer")
    print("=" * 50)
    print("\nNote: Add content files to /data folder first")
    print("\nExample usage:")
    print("  analyzer.load_content('all')")
    print("  analyzer.analyze_patterns()")
    print("  analyzer.generate_style_profile()")
    print("  analyzer.suggest_content_ideas('social media marketing')")
    print("\nReady to analyze TRO content!")


if __name__ == "__main__":
    main()
