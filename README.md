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
  <pre><code>
pip install -r requirements.txt</code></pre>

<p>Install playwright:</p>
  <pre><code>
playwright install</code></pre>
<pre><code>
playwright install-deps</code></pre>

  <h2>⚡ Usage</h2>
  <p><strong>Example:</strong></p>
  <pre><code># Run the extractor with a YouTube channel ID
python main.py --channel UC_x5XG1OV2P6uZZ5FSM9Ttw --limit 10</code></pre>

  <ul>
        <li>--channel : YouTube channel ID (required)</li>
        <li>--limit : Limit number of videos (must be > 0, optional)</li>
  </ul>

  <p>This will fetch all videos and print/save their details.</p>


  <h2>📜 License</h2>
  <p>This project is licensed under the MIT License.</p>
</body>
</html>
