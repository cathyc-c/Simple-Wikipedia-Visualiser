# Simple Wikipedia Visualiser

An interactive knowledge graph generator that scrapes [Simple Wikipedia](https://simple.wikipedia.org) and visualises connections between topics as an expandable node graph. Built for my A-Level Computer Science NEA project.

## What it does

Enter any keyword, and the tool will:
1. Scrape the corresponding Simple Wikipedia article using BeautifulSoup
2. Extract hyperlinks to related topics and filter out irrelevant ones
3. Recursively build a tree of connected concepts
4. Render an interactive knowledge graph using Pyvis
5. Display it in your browser via a local Python web server

The graph is **interactive**: nodes can be dragged, and clicking a node expands it to show its own related topics.

## Demo

<img width="1427" height="1096" alt="demo" src="https://github.com/user-attachments/assets/44f0c79c-c744-4c1e-996d-1e0b26cbb410" />

## Usage

1. Type a keyword into the search bar (e.g. `photosynthesis`)
2. Press **Search**
3. The graph loads with the keyword as the central node and its related topics as connected nodes
4. Drag nodes to rearrange; click to expand further

## Features

- Filters irrelevant hyperlinks so only conceptually related topics appear as nodes
- Interconnected nodes are linked to each other (not just to the root), showing lateral relationships
- Tree pruning limits depth to keep performance reasonable
- Accessibility: high colour contrast UI, large fonts, simple layout
- Error handling for network failures and invalid search terms

## Known limitations / future improvements

- Currently runs locally only, no public hosting
- Single-user, no concurrency support
- No search history or saved graphs
- Potential extension: host on a cloud platform (AWS/GCP) for public access
- Potential extension: add a database (e.g. MySQL) to store user profiles and search history
- Potential extension: use ML (scikit-learn/TensorFlow) to improve node relevance filtering beyond just hyperlinks

## System design

The system is split into several components:

- **`WebScraper`** — Makes GET requests to Simple Wikipedia and parses HTML with BeautifulSoup to extract filtered hyperlinks
- **`Node` / `GraphNodes`** — Represent individual topics and the full collection of nodes in memory
- **`Graph`** — Builds a recursive tree structure from the root keyword outward using depth-limited traversal and tree pruning for performance
- **`UserInterface`** — Generates the Pyvis HTML output and manages browser display
- **`Handler`** — Subclasses `http.server.SimpleHTTPRequestHandler` to serve the page and handle search requests from the browser

## Tech stack

| Layer | Tool |
|---|---|
| Language | Python |
| Web scraping | `requests`, `BeautifulSoup4` |
| Graph generation | `pyvis` |
| Local server | `http.server` |

## Requirements

- Python 3.x
- `requests`
- `beautifulsoup4`
- `pyvis`
