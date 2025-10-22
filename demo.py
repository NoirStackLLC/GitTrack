#!/usr/bin/env python3
"""
Demo script for GitTrack - Shows what the output looks like with mock data.
This simulates the GitTrack output without making actual API calls.
"""

from datetime import datetime


def display_demo_output():
    """Display a demo of GitTrack output with mock data."""
    
    # Demo 1: Linux kernel repository
    print("\n" + "="*60)
    print("Demo 1: Tracking the Linux kernel repository")
    print("="*60 + "\n")
    print("$ python gittrack.py torvalds/linux\n")
    
    print("="*60)
    print("GitTrack - Repository Activity Tracker")
    print("="*60 + "\n")
    
    print("Fetching information for: torvalds/linux")
    print(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    print("Repository: torvalds/linux")
    print("Description: Linux kernel source tree")
    print("Language: C")
    print("Created: 2011-09-04T22:48:12Z")
    print(f"Last Updated: {datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')}\n")
    print("-"*60 + "\n")
    
    print("Key Metrics:")
    print("  ⭐ Stars:        150,234")
    print("  🍴 Forks:        50,123")
    print("  👁️  Watchers:     150,234")
    print("\n  Fetching commit count...")
    print("  💻 Commits:      1,234,567")
    print("  Fetching issues count...")
    print("  📝 Issues:       500 (Open: 100, Closed: 400)")
    print("  Fetching pull requests count...")
    print("  🔀 Pull Requests: 1,000 (Open: 50, Closed: 950)\n")
    print("-"*60 + "\n")
    print("Repository URL: https://github.com/torvalds/linux\n")
    print("="*60 + "\n")
    
    input("Press Enter to see another example...\n")
    
    # Demo 2: React repository
    print("\n" + "="*60)
    print("Demo 2: Tracking the React repository")
    print("="*60 + "\n")
    print("$ python gittrack.py facebook/react\n")
    
    print("="*60)
    print("GitTrack - Repository Activity Tracker")
    print("="*60 + "\n")
    
    print("Fetching information for: facebook/react")
    print(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    print("Repository: facebook/react")
    print("Description: A declarative, efficient, and flexible JavaScript library for building user interfaces.")
    print("Language: JavaScript")
    print("Created: 2013-05-24T16:15:54Z")
    print(f"Last Updated: {datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')}\n")
    print("-"*60 + "\n")
    
    print("Key Metrics:")
    print("  ⭐ Stars:        220,456")
    print("  🍴 Forks:        45,123")
    print("  👁️  Watchers:     220,456")
    print("\n  Fetching commit count...")
    print("  💻 Commits:      16,789")
    print("  Fetching issues count...")
    print("  📝 Issues:       12,345 (Open: 789, Closed: 11,556)")
    print("  Fetching pull requests count...")
    print("  🔀 Pull Requests: 15,678 (Open: 123, Closed: 15,555)\n")
    print("-"*60 + "\n")
    print("Repository URL: https://github.com/facebook/react\n")
    print("="*60 + "\n")
    
    # Demo 3: Smaller repository
    print("\n" + "="*60)
    print("Demo 3: Tracking a smaller repository")
    print("="*60 + "\n")
    print("$ python gittrack.py NoirStackLLC/GitTrack\n")
    
    print("="*60)
    print("GitTrack - Repository Activity Tracker")
    print("="*60 + "\n")
    
    print("Fetching information for: NoirStackLLC/GitTrack")
    print(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    print("Repository: NoirStackLLC/GitTrack")
    print("Description: Track GitHub repository activity and display key metrics")
    print("Language: Python")
    print("Created: 2025-10-22T00:00:00Z")
    print(f"Last Updated: {datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')}\n")
    print("-"*60 + "\n")
    
    print("Key Metrics:")
    print("  ⭐ Stars:        5")
    print("  🍴 Forks:        2")
    print("  👁️  Watchers:     5")
    print("\n  Fetching commit count...")
    print("  💻 Commits:      3")
    print("  Fetching issues count...")
    print("  📝 Issues:       1 (Open: 1, Closed: 0)")
    print("  Fetching pull requests count...")
    print("  🔀 Pull Requests: 1 (Open: 1, Closed: 0)\n")
    print("-"*60 + "\n")
    print("Repository URL: https://github.com/NoirStackLLC/GitTrack\n")
    print("="*60 + "\n")


def main():
    """Main entry point for demo script."""
    print("\n" + "="*60)
    print("GitTrack Demo - Simulated Output")
    print("="*60)
    print("\nThis demo shows what GitTrack output looks like.")
    print("The data shown is simulated and not from actual API calls.")
    print("\nNote: To use GitTrack with real data, run:")
    print("  python gittrack.py owner/repo")
    print("\nYou may need a GitHub token to avoid rate limits:")
    print("  python gittrack.py owner/repo --token YOUR_TOKEN")
    print("\n" + "="*60)
    
    input("\nPress Enter to start the demo...\n")
    
    display_demo_output()
    
    print("\n" + "="*60)
    print("Demo Complete!")
    print("="*60)
    print("\nTo use GitTrack with real repositories:")
    print("  python gittrack.py owner/repo")
    print("\nFor help:")
    print("  python gittrack.py --help")
    print("\n")


if __name__ == "__main__":
    main()
