<!DOCTYPE html>
<html lang="en">
<body>
  <h1>YouTube Video Extractor</h1>

  <p>
    A tool that takes a <strong>YouTube Channel ID</strong> and extracts information about all the videos from that channel.
  </p>

  <h2>🚀 Features</h2>
  <ul>
    <li>Fetch videos from a YouTube channel by <strong>Channel ID</strong></li>
    <li>Extract useful video information such as:
      <ul>
        <li>Video ID</li>
        <li>Title</li>
        <li>Thumbnail</li>
        <li>Transcript (if available)</li>
        <li>Published Date</li>
        <li>Duration</li>
        <li>View Count (if available)</li>
        <li>Like Count (if available)</li>
      </ul>
    </li>
    <li>Output results in a structured format (JSON/CSV, depending on implementation)</li>
  </ul>

  <h2>📦 Installation</h2>
  <pre><code>git clone https://github.com/sarrarmohcin/youtube-video-extractor.git</code></pre>

  <p>Install dependencies:</p>
  <pre><code>npm install
# or
pip install -r requirements.txt</code></pre>

  <h2>⚡ Usage</h2>
  <p><strong>Example:</strong></p>
  <pre><code># Run the extractor with a YouTube channel ID
node index.js --channel UC_x5XG1OV2P6uZZ5FSM9Ttw</code></pre>

  <p>or</p>
  <pre><code>python extractor.py --channel UC_x5XG1OV2P6uZZ5FSM9Ttw</code></pre>

  <p>This will fetch all videos and print/save their details.</p>

  <h3>Output Example</h3>
  <pre><code>[
  {
    "videoId": "dQw4w9WgXcQ",
    "title": "Example Video",
    "description": "This is a sample video description.",
    "publishedAt": "2023-08-01T12:34:56Z",
    "duration": "PT12M30S",
    "views": 120345
  }
]</code></pre>

  <h2>🔑 Requirements</h2>
  <ul>
    <li>YouTube Data API v3 key</li>
    <li>Node.js / Python (depending on version of this repo)</li>
  </ul>
  <p>You can get an API key from <a href="https://console.cloud.google.com/">Google Cloud Console</a>.</p>

  <h2>🛠️ Configuration</h2>
  <p>Set your YouTube API key as an environment variable:</p>
  <pre><code>export YT_API_KEY="your_api_key_here"</code></pre>

  <p>Or place it in a <code>.env</code> file:</p>
  <pre><code>YT_API_KEY=your_api_key_here</code></pre>

  <h2>📜 License</h2>
  <p>This project is licensed under the MIT License.</p>
</body>
</html>
